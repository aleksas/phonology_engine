[![Build status](https://ci.appveyor.com/api/projects/status/pd61vbwpawr3yejs?svg=true)](https://ci.appveyor.com/project/aleksas/phonology-engine)
[![PyPI](https://img.shields.io/pypi/v/phonology_engine.svg)](https://pypi.org/project/phonology-engine)

# About

At the core of this library is text normalization and word stressing processor from [LIEPA speach synthesizer](https://www.raštija.lt/liepa). The native code related to text processing was cut out of [the synthesizer library code](https://www.raštija.lt/liepa/infrastrukturines-paslaugos/elektroninio-teksto-skaitytuvas/7563) and wrapped in Python.

# License

- [BSD liscense](https://raw.githubusercontent.com/aleksas/phonology_engine/master/LICENSE)

# Intro

The library takes text in Lithuanian and does following:
- Normalizes it. Converts numbers to word reprezentations (e.g. "1" > "vienas").
- Splits text into phrases/sentences.
- Splits phrases into words
- Identifies word syllables
- Identifies possible grammar forms of the word, and identifies stressed letter and stress type according the grammar form
- Chooses one rule
- Returns either structured results or collapsed 

Library supports following environments:
- Python: 2.7, 3.*
- OS: Linux, Windows
- Architecture: 32bit, 64bit

# Installing

```
pip install phonology_engine
```

# Using 

## Normalize text
Conversion from numbers to word representation.

```
from phonology_engine import PhonologyEngine
pe = PhonologyEngine()
res = pe.normalize_and_collapse('31 kačiukas perbėgo kelią.')
print(res)
```
Would result in 
```
TRISDEŠIMT VIENAS KAČIUKAS PERBĖGO KELIĄ.
```

## Process
Determining word stresses.

```
from phonology_engine import PhonologyEngine
pe = PhonologyEngine()
res = pe.process_and_collapse('31 kačiukas perbėgo kelią.', 'utf8_stressed_word')
print(res)
```
Would result in 
```
TRÌSDEŠIMT VÍENAS KAČIÙKAS PÉRBĖGO KẼLIĄ.
```
------

Determining word stresses, syllables, grammar form from word.

```
from phonology_engine import PhonologyEngine
from pprint import pprint
pe = PhonologyEngine()
res = pe.process('31 kačiukas perbėgo kelią.', include_syllables=True)
pprint(res)
```
Would result in 
```
('.',
 [('',
   [[{'ascii_stressed_word': 'TRI`-SDE-ŠIMT',
      'number_stressed_word': 'TRI0-SDE-ŠIMT',
      'stress_options': {'decoded_options': [{'rule': 'Nekaitomas žodis'}],
                         'options': [(2, 0, 1, 1688)],
                         'selected_index': 0},
      'syllables': [0, 3, 6],
      'utf8_stressed_word': 'TRÌ-SDE-ŠIMT',
      'word': 'TRI-SDE-ŠIMT'},
     {'ascii_stressed_word': 'VI^E-NAS',
      'number_stressed_word': 'VI1E-NAS',
      'stress_options': {'decoded_options': [{'grammatical_case': 'Vardininkas',
                                              'number': 'vienaskaita',
                                              'rule': 'Linksnis ir kamieno '
                                                      'tipas',
                                              'stem_type': 16,
                                              'stress_type': 1,
                                              'stressed_letter_index': 1}],
                         'options': [(1, 1, 2, 4096)],
                         'selected_index': 0},
      'syllables': [0, 3],
      'utf8_stressed_word': 'VÍE-NAS',
      'word': 'VIE-NAS'},
     {'ascii_stressed_word': 'KA-ČIU`-KAS',
      'number_stressed_word': 'KA-ČIU0-KAS',
      'stress_options': {'decoded_options': [{'grammatical_case': 'Vardininkas',
                                              'number': 'vienaskaita',
                                              'rule': 'Linksnis ir kamieno '
                                                      'tipas',
                                              'stem_type': 0,
                                              'stress_type': 0,
                                              'stressed_letter_index': 4}],
                         'options': [(4, 0, 2, 0)],
                         'selected_index': 0},
      'syllables': [0, 2, 5],
      'utf8_stressed_word': 'KA-ČIÙ-KAS',
      'word': 'KA-ČIU-KAS'},
     {'ascii_stressed_word': 'PE^R-BĖ-GO',
      'number_stressed_word': 'PE1R-BĖ-GO',
      'stress_options': {'decoded_options': [{'rule': 'Veiksmazodžių kamienas '
                                                      'ir galune (taisytina)'}],
                         'options': [(1, 1, 0, 465)],
                         'selected_index': 0},
      'syllables': [0, 3, 5],
      'utf8_stressed_word': 'PÉR-BĖ-GO',
      'word': 'PER-BĖ-GO'},
     {'ascii_stressed_word': 'KE~-LIĄ',
      'number_stressed_word': 'KE2-LIĄ',
      'stress_options': {'decoded_options': [{'grammatical_case': 'Galininkas',
                                              'number': 'vienaskaita',
                                              'rule': 'Linksnis ir kamieno '
                                                      'tipas',
                                              'stem_type': 2,
                                              'stress_type': 2,
                                              'stressed_letter_index': 1}],
                         'options': [(1, 2, 2, 515)],
                         'selected_index': 0},
      'syllables': [0, 2],
      'utf8_stressed_word': 'KẼ-LIĄ',
      'word': 'KE-LIĄ'}]],
   ['TRISDEŠIMT VIENAS KAČIUKAS PERBĖGO KELIĄ']),
  ''])
```

# References
- [Kirčiavimas internetu](http://kirtis.info) - Online dictionarry with word stresses and grammar annotation, has a [GitHub repo](https://github.com/Sistemium/krc-angular). It is likely based on [VDU dictionary](https://github.com/aleksas/phonology_engine/tree/resources/VDU). 