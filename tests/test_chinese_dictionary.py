from subtitles import chinese_dictionary
import pytest
import os

@pytest.fixture
def _dictionary():
    yield chinese_dictionary.ChineseDictionary(os.environ['DICT_PATH'], 3)

# Pass chinese characters to dictionary and get back translation
def test_translate(_dictionary):
    translation = _dictionary.translate('我是中国人')
    assert translation == [('我', 'wǒ', 'I'), ('是', 'shì', 'is'), ('中国人', 'zhōngguórén', 'Chinese person')]

def test_group_sentence(_dictionary):
    chinese_sentence = '我是中国人'
    assert _dictionary.translate_to_pinyin(chinese_sentence) == 'wǒ shì zhōngguórén'
    assert _dictionary.translate_to_english(chinese_sentence) == 'I is Chinese person'