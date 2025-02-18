import pytest
from string_utils import StringUtils

string_utils = StringUtils()


#Позитивные проверки capitalize:
res = string_utils.test_capitalize("error")
assert res == "Error"

res = string_utils.test_capitalize("Test")
assert res == "Test"

#Негативные проверки capitalize:
res = string_utils.test_capitalize("12345")
assert res == "12345"

res = string_utils.test_capitalize("!проверка")
assert res == "!проверка"

res = string_utils.test_capitalize(".%:!!()")
assert res == ".%:!!()"


#Позитивная проверка contains:
res4 = string_utils.test_contains("Error", "r")
assert res4 == True
res4 = string_utils.test_contains("1234567", "23")
assert res4 == True

#Негативная проверка containscontains:
res4 = string_utils.test_contains("Error", "А")
assert res4 == True
res4 = string_utils.test_contains("Error", "R")
assert res4 == True
res4 = string_utils.test_contains("Error", "y")
assert res4 == True
res4 = string_utils.test_contains("Error", "")
assert res4 == True
res4 = string_utils.test_contains("", "")
assert res4 == True
res4 = string_utils.test_contains("", " ")
assert res4 == True

#Позитивная проверка test_delete_symbol:
res2 = string_utils.test_delete_symbol("Тестировщики","и")
assert res2 == "Тестровщк"
res2 = string_utils.test_delete_symbol("Тестировщики","ест")
assert res2 == "Тировщики"

#Негативные проверки test_delete_symbol:
res2 = string_utils.test_delete_symbol("Тестировщики","а")
assert res2 == "Тестировщики"
res2 = string_utils.test_delete_symbol("Тестировщики","1")
assert res2 == "Тестировщики"
res2 = string_utils.test_delete_symbol("Тестировщики","а")
assert res2 == "Тестировщики"


#Позитивная проверка test_trim:
res3 = string_utils.test_trim( "    Test")
assert res3 == "Test"
res3 = string_utils.test_trim( "   ")
assert res3 == ""

#Негативная проверка test_trim:
res3 = string_utils.test_trim( "    Test")
assert res3 == "   Test"
res3 = string_utils.test_trim( "Test  ")
assert res3 == "Test  "
res3 = string_utils.test_trim( "Test    test")
assert res3 == "Test    test"