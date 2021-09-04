from Q04PalindromePermutation import *

def test_PalidromePermutation():
    data = [
        ("abc", False),
        ("taco cat", True),
        ("taco CAT", True)
    ]
    for (input, expected) in data:
        assert IsPalindromePermutation(input) == expected

def test_IsPalindromePermutationV2():
    data = [
        ("abc", False),
        ("taco cat", True),
        ("taco CAT", True)
    ]
    for (input, expected) in data:
        assert IsPalindromePermutationV2(input) == expected
