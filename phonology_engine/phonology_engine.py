# -*- coding: utf-8 -*-
from os.path import join, dirname, abspath
from .pe_output import PhonologyEngineOutput, PhonologyEngineNormalizedPhrases
from .pe_output import _syllable_chars, _numeric_stress_map, _utf8_stress_map, _ascii_stress_map
from .pe_native import phonology_engine_process_phrase, phonology_engine_normalize_text
import re

_phrase_separators = u'.?!;:\r\n,'
_truncated_chars = u'„“"\''
_max_prase_length = 200
_word_format_symbols = {
    None:'',
    'word': '',
    'word_with_syllables': _syllable_chars,
    'word_with_all_numeric_stresses': [_syllable_chars] + list(_numeric_stress_map.values()),
    'word_with_only_multiple_numeric_stresses': _numeric_stress_map.values(),
    'number_stressed_word': _numeric_stress_map.values(),
    'utf8_stressed_word': _utf8_stress_map.values(),
    'ascii_stressed_word': _ascii_stress_map.values()
}

class PhonologyEngine:
    def __init__(self):
        def _collapsor(processed_phrase, phrase, normalized_phrase, letter_map, word_format=None):
            if word_format:
                return processed_phrase[word_format]
            else:
                return processed_phrase

        self.collapsor = _collapsor
        self.phrase_separators = _phrase_separators

    def _process_phrase(self, phrase, include_syllables):
        if len(phrase) > _max_prase_length:
            raise Exception('Phrase "%s" length exceeds %d char limit' % (phrase, _max_prase_length))
        
        handle = phonology_engine_process_phrase(phrase)
        
        with PhonologyEngineOutput(handle) as output:
            res = [
                    {
                    'word': output.get_word(i, include_syllables=False),
                    'word_with_syllables': output.get_word(i, include_syllables=True),
                    'number_stressed_word': output.get_word_with_numeric_stress(i, include_syllables=include_syllables),
                    'utf8_stressed_word': output.get_word_with_utf8_stress(i, include_syllables=include_syllables),
                    'ascii_stressed_word': output.get_word_with_ascii_stress(i, include_syllables=include_syllables),
                    'word_with_all_numeric_stresses': output.get_word_with_all_numeric_stresses(i, include_syllables=include_syllables),
                    'word_with_only_multiple_numeric_stresses': output.get_word_with_only_multiple_numeric_stresses(i, include_syllables=include_syllables),
                    'syllables': output.get_word_syllables(i),
                    'stress_options': output.get_word_stress_options(i)
                    }

                    for i in range(output.get_word_count())
                ]
                                
            return res

    def _consolidate_normalized_words(self, phrase):
        last_word_details = None
        for word_details in phrase:
            if last_word_details == None:
                last_word_details = word_details
            else:
                if word_details['span_source'] == last_word_details['span_source']:
                    last_word_details['span_normalized'] = (
                        min(last_word_details['span_normalized'][0], word_details['span_normalized'][0]),
                        max(last_word_details['span_normalized'][1], word_details['span_normalized'][1]),
                    )

                    for word_format in _word_format_symbols.keys():
                        if word_format:
                            last_word_details[word_format] += ' ' + word_details[word_format]
                else:
                    yield last_word_details
                    last_word_details = word_details
        if last_word_details:
            yield last_word_details

    def _process(self, text, separators, normalize=True, include_syllables=True, normalize_only=False):
        p = (r'[^' + re.escape(separators) + r']+') if separators else r'^.*$'
        pattern = re.compile(p)
        if len(text.strip()) == 0:
            yield text

        for m in pattern.finditer(text):
            phrase = m.group()

            if normalize:
                handle = phonology_engine_normalize_text(phrase)
                with PhonologyEngineNormalizedPhrases(handle) as normalized_phrases:
                    if normalize_only:
                        for normalized_phrase, letter_map in normalized_phrases:
                            yield normalized_phrase, phrase, normalized_phrase, letter_map
                    else:
                        for normalized_phrase, letter_map in normalized_phrases:
                            processed_phrase = self._process_phrase(normalized_phrase, include_syllables)
                            yield processed_phrase, phrase, normalized_phrase, letter_map
            else:
                processed_phrase = self._process_phrase(phrase, include_syllables)
                yield processed_phrase, phrase, phrase, list(range(len(phrase)))

    def get_collapse_formats(self):
        return _word_format_symbols.keys()

    def process(self, s, include_syllables=False):
        return self._process(s, separators=self.phrase_separators, normalize=True, include_syllables=include_syllables, normalize_only=False)

    def process_and_collapse(self, s, word_format='word', normalize=True, include_syllables=False):
        processed = self._process(s, separators=self.phrase_separators, normalize=normalize, include_syllables=include_syllables, normalize_only=False)
        processed = list(processed)
        return self.collapse(s, processed, word_format)

    def collapse(self, original_text, output, word_format='word'):
        if word_format not in _word_format_symbols:
            raise Exception('Invalide word format "%s". Can be one of: %s.' % (word_format, str(_word_format_symbols.keys())))

        processed_words = []
        for processed_phrase, _, _, _ in output:
            if isinstance(processed_phrase, str):
                processed_words.append(processed_phrase)
            else:
                for word_details in processed_phrase:
                    if isinstance(word_details, str):
                        processed_words.append(word_details)
                    else:
                        processed_words.append(word_details[word_format]) 

        return ' '.join(processed_words)

    def normalize(self, text):
        return self._process(text, separators=self.phrase_separators, normalize=True, include_syllables=False, normalize_only=True)

    def normalize_and_collapse(self, text):
        return self.collapse(text, self._process(text, separators=self.phrase_separators, normalize=True, include_syllables=False, normalize_only=True))


