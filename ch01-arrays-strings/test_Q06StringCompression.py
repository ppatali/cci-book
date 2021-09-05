from Q06StringCompression import *

def test_Cases():
    data = [ 
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("a", "a")
    ]

    for (input, excepted) in data:
        assert Compress(input) == excepted
