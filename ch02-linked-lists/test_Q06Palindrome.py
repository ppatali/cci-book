from LinkedList import *
from Q06Palindrome import *

def test_Cases():
    data = [
        (generateLinkedList([0,1,2,1,0]), True),
        (generateLinkedList([0,1,1,0]), True),
        (generateLinkedList([0,1,2,0]), False)
    ]

    for (input, expected) in data:
        assert expected == PalindromeByReversing(input)

def test_Cases():
    data = [
        (generateLinkedList([0,1,2,1,0]), True),
        (generateLinkedList([0,1,1,0]), True),
        (generateLinkedList([0,1,2,0]), False)
    ]

    for (input, expected) in data:
        assert expected == PalindromeByHalf(input)