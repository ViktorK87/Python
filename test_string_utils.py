import pytest
from String_utils import StringUtils

@pytest.mark.parametrize('word , result', [("skypro", "Skypro"), ("hello world", "Hello world")])
def test_capitalize_positive(word, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(word)
    assert res == result

@pytest.mark.parametrize('word , result', [("Skypro", "Skypro"), ("TEST", "TEST"), ("!!hello world", "!!hello world")])
def test_capitalize_negative(word, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(word)
    assert res == result

@pytest.mark.parametrize('string , result', [("   skypro", "skypro"), (" ! sky pro", "! sky pro")])
def test_trim_positive(string, result):
    string_Utils = StringUtils()
    res = string_Utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string , result', [("   ", ""), ("! !   sky pro", "! !   sky pro")])
def test_trim_negative(string, result):
    string_Utils = StringUtils()
    res = string_Utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("SkyPro", "S", True), ("Test", "e", True)])
def test_contains_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("SkyPro", "Y", False), ("Test", "a", False)])
def test_contains_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [("SkyPro", "y", "SkPro"), ("Test", "e", "Tst")])
def test_delete_symbol_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("SkyPro", "Y", "SkyPro"), ("Test", "E", "Test")])
def test_delete_symbol_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result