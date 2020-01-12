# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from phonology_engine import PhonologyEngine

def test_process_1():
    pe = PhonologyEngine()
    pe.process('Laba diena')

def test_process_2():
    pe = PhonologyEngine()
    pe.process('Laba diena, kaip laikais?')

def test_process_and_collapse_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse('Laba diena, kaip laikais?')
    assert_equal(res, u'Laba diena, kaip laikais?')

def test_process_and_collapse_word_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?', 'word')
    assert_equal(res, u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?')

def test_process_and_collapse_word_with_syllables_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?', 'word_with_syllables')
    assert_equal(res, u'I-šti-ki-ma sa-vo dva-si-niam ir do-ro-vi-niam pa-vel-dui Są-jun-ga re-mia-si nedalomomis ir vi-suo-ti-nė-mis ver-ty-bė-mis: la-ba die-na. Kur bu-vai?')

def test_process_and_collapse_word_with_all_numeric_stresses_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: Laba diena. Kur buvai?', 'word_with_all_numeric_stresses')
    assert_equal(res, u'I0štikima sa0vo dva2siniam ir doro1viniam pa2veldui Są1junga re2miasi nedalomomis ir visu1otinėmis verty1bėmis: La2ba0 diena0. Kur2 buvai2?')

def test_process_and_collapse_word_with_only_multiple_numeric_stresses_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: Laba diena. Kur buvai?', 'word_with_only_multiple_numeric_stresses')
    assert_equal(res, u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: La2ba0 diena. Kur buvai?')

def test_process_and_collapse_number_stressed_word_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?', 'number_stressed_word')
    assert_equal(res, u'I0štikima sa0vo dva2siniam ir doro1viniam pa2veldui Są1junga re2miasi nedalomomis ir visu1otinėmis verty1bėmis: la2ba diena0. Kur2 buvai2?')

def test_process_and_collapse_utf8_stressed_word_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?', 'utf8_stressed_word')
    assert_equal(res, u'Ìštikima sàvo dvãsiniam ir doróviniam pãveldui Są́junga rẽmiasi nedalomomis ir visúotinėmis vertýbėmis: lãba dienà. Kur̃ buvaĩ?')

def test_process_and_collapse_ascii_stressed_word_1():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?', 'ascii_stressed_word')
    assert_equal(res, u'I`štikima sa`vo dva~siniam ir doro^viniam pa~veldui Są^junga re~miasi nedalomomis ir visu^otinėmis verty^bėmis: la~ba diena`. Kur~ buvai~?')

def test_normalize_text_1():
    pe = PhonologyEngine()
    pe.normalize(u'1 žmogus. Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?')

def test_normalize_and_collapse_text_1():
    pe = PhonologyEngine()
    res = pe.normalize_and_collapse(u'1 žmogus. Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?')
    assert_equal(res, u'VIENAS žmogus. Ištikima savo dvasiniam ir doroviniam paveldui Sąjunga remiasi nedalomomis ir visuotinėmis vertybėmis: laba diena. Kur buvai?')

def test_normalize_and_collapse_text_2():
    pe = PhonologyEngine()
    res = pe.process_and_collapse(u'31 kačiukas perbėgo kelią.', 'ascii_stressed_word')
    assert_equal(res, u'TRI`SDEŠIMT VI^ENAS kačiu`kas pe^rbėgo ke~lią.')

def test_normalize_and_collapse_abbr_1():
    pe = PhonologyEngine()
    pe.phrase_separators = ''
    res = pe.normalize_and_collapse(u'proc.')
    assert_equal(res, u'PROCENTAS')

def test_normalize_and_collapse_text_roman_num_1():
    pe = PhonologyEngine()
    pe.phrase_separators = ''
    res = pe.normalize_and_collapse(u'IV.')
    assert_equal(res, u'KETVIRTAS')
