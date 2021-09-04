from Q02CheckPermutation import *

def test_EmptyOrNone():
    assert not CheckPermutation(None, "")

def test_UnequalLength():
    assert not CheckPermutation("abc", "bc")

def test_3Letter():
    assert CheckPermutation("god", "dog")

def test_MixedCaseTrue():
    assert CheckPermutation("Dog", "goD")

def test_MixedCaseFalse():
    assert not CheckPermutation("Dog", "god")

def test_WhiteSpaceAndSpecialChar():
    assert CheckPermutation("I am happy! ", "may I app h!")