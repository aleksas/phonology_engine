# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from phonology_engine import PhonologyEngine

def test_process_1():
    pe = PhonologyEngine()
    text = u'1 katinas važiavo viešuoju transportu. Jis išlipo Siesikų stotelėje lygiai po 2 minučių.'

    for elem in pe.process(text):
        if 'span_source' in elem and len(elem['word']) == elem['span_source']:
            assert_equal(elem['word'].lower(),  elem['span_source'][1] - elem['span_source'][0])


