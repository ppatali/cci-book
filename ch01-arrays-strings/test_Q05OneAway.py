from Q05OneAway import *

def test_Cases():
    data = [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False)
    ]

    for (string1, string2, expected) in data:
        assert IsOneEditAway(string1, string2) == expected