import IsUnique11

def test_NotUnique():
    assert not IsUnique11.IsUnique("aba")

def test_UniqueNoSpaces():
    assert IsUnique11.IsUnique("abc")

def test_UniqueTwoWords():
    assert IsUnique11.IsUnique("hey world")

def test_SingleChar():
    assert IsUnique11.IsUnique("#")

def test_UniqueCaseSensitive():
    assert IsUnique11.IsUnique("Check 123!")

def test_NotUniqueLongString():
    assert not IsUnique11.IsUnique("QuickBrownFox")

def test_UniqueSpecialChar():
    assert IsUnique11.IsUnique("Pond %?!][")
