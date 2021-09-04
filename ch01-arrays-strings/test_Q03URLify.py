from Q03URLify import *

def test_Test1():
    assert URLify(None, None) == None

def test_Test2():
    assert URLify([c for c in "Mr John Smith    "], 13) == [c for c in "Mr%20John%20Smith"]

def test_Test3():
    assert URLify(list("This is much easier way!!        "), 25) == list("This%20is%20much%20easier%20way!!")

# https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/3_URLify/URLify.py
# Some nice use of tuples and iterating over the values
def test_Test4():
    data = [
        (list("Hello World!  "), 12, list("Hello%20World!")),
        (list("What an elgant way      "), 18, list("What%20an%20elgant%20way"))
    ]

    for (input, truelength, expected) in data:
        actual = URLify(input, truelength)
        assert actual == expected
    