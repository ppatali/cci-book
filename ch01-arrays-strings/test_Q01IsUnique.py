from Q01IsUnique import *

def test_NotUnique():
    assert not IsUnique("aba")

def test_UniqueNoSpaces():
    assert IsUnique("abc")

def test_UniqueTwoWords():
    assert IsUnique("hey world")

def test_SingleChar():
    assert IsUnique("#")

def test_UniqueCaseSensitive():
    assert IsUnique("Check 123!")

def test_NotUniqueLongString():
    assert not IsUnique("QuickBrownFox")

def test_UniqueSpecialChar():
    assert IsUnique("Pond %?!][")
