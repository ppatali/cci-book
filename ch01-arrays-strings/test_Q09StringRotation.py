from Q09StringRotation import *

def test_Cases():
    data = [
        ("waterbottle", "erbottlewat", True),
        ("waterbottle", "erbottlewta", False),
        ("", "", True),
        (" ", " ", True),
        ("Hello world!", "orld!Hello w", True)
    ]

    for (string1, string2, expected) in data:
        assert StringRotation(string1, string2) == expected
    