# -*- coding: utf-8 -*-
from os.path import join, dirname, abspath
from .pe_output import PhonologyEngineOutput, PhonologyEngineNormalizedPhrases
from .pe_native import phonology_engine_process_phrase, phonology_engine_normalize_text
import re

_phrase_separators = '.?!;:\r\n,'
_max_prase_length = 200
_valid_word_formats = [None, 'word', 'word_with_syllables', 'word_with_all_numeric_stresses', 'word_with_only_multiple_numeric_stresses', 'number_stressed_word', 'utf8_stressed_word', 'ascii_stressed_word']

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
                    'word_with_all_numeric_stresses' :output.get_word_with_all_numeric_stresses(i, include_syllables=include_syllables),
                    'word_with_only_multiple_numeric_stresses' :output.get_word_with_only_multiple_numeric_stresses(i, include_syllables=include_syllables),
                    'syllables': output.get_word_syllables(i),
                    'stress_options': output.get_word_stress_options(i)
                    }

                    for i in range(output.get_word_count())
                ]
                                
            return res

    def _get_norm_index_spans(self, letter_map):
        span_first, span_last = -1, -1
        last_v = None
        for i, v in enumerate(letter_map):
            if v != last_v or i == len(letter_map) - 1:
                if i - span_first > 1:
                    yield span_first, i
                span_first = i
            last_v = v

    def _process(self, text, separators, normalize=True, include_syllables=True, normalize_only=False, letter_map=None):
        pattern = re.compile(r'[^%s]+' % separators)
        if len(text.strip()) == 0:
            yield text

        last_span_end = 0
        for m in pattern.finditer(text):
            span = m.span()
            if span[0] > last_span_end:
                yield text[last_span_end, span[0]]
            last_span_end = span[1]
            phrase = m.group()

            if normalize:
                handle = phonology_engine_normalize_text(phrase)
                with PhonologyEngineNormalizedPhrases(handle) as normalized_phrases:
                    if normalize_only:
                        yield ' '.join([p for p,_ in normalized_phrases])
                    else:
                        for nornalized_phrase, letter_map in normalized_phrases:
                            if len(nornalized_phrase) != len(letter_map):
                                t = ''.join([pair[0] + str(pair[1]) for pair in zip(nornalized_phrase, letter_map)])
                                print (t)
                                raise Exception("Phrase length differs from phrase letter map length (%d != %d)." % (len(nornalized_phrase), len(letter_map)))

                            processed_phrase = self._process_phrase(nornalized_phrase, include_syllables)

                            yield processed_phrase, phrase, nornalized_phrase, letter_map
            else:
                processed_phrase = self._process_phrase(phrase, include_syllables)

                yield processed_phrase, phrase, phrase, list(range(len(phrase)))

    def get_collapse_formats(self):
        return _valid_word_formats

    def process(self, s, include_syllables=False):
        return self._process(s.upper(), separators=self.phrase_separators, normalize=True, include_syllables=include_syllables, normalize_only=False)

    def process_and_collapse(self, s, word_format='word', normalize=True, include_syllables=False):
        return self.collapse(self._process(s, separators=self.phrase_separators, normalize=normalize, include_syllables=include_syllables, normalize_only=False), word_format)

    def collapse(self, output, word_format='word'):
        if word_format not in _valid_word_formats:
            raise Exception('Invalide word format "%s". Can be one of: %s.' % (word_format, str(_valid_word_formats)))

        res = ''
        for element in output:
            if isinstance(element, tuple):
                processed_phrase, phrase, normalized_phrase, letter_map = element
                res += self.collapsor(processed_phrase, phrase, normalized_phrase, letter_map, word_format)
            else:
                res += element
        
        return res

    def normalize(self, text):
        return self._process(text, separators=self.phrase_separators, normalize=True, include_syllables=False, normalize_only=True)

    def normalize_and_collapse(self, text):
        return self.collapse(self._process(text, separators=self.phrase_separators, normalize=True, include_syllables=False, normalize_only=True))


