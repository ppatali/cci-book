from LinkedList import *
from Q01RemoveDuplicate import *

def test_Cases():
    data = [
        (getLinkedList(["abc"]), getLinkedList("abc")),
        (getLinkedList(["aac"]), getLinkedList("ac")),
        (getLinkedList(["aaa"]), getLinkedList("a")),
        (getLinkedList(["aba"]), getLinkedList("ab")),
        (getLinkedList(["abab"]), getLinkedList("ab"))
    ]

    for (input, expected) in data:
        RemoveDuplicate(input)
        assert input == expected

def test_CasesV2():
    data = [
        (getLinkedList(["abc"]), getLinkedList("abc")),
        (getLinkedList(["aac"]), getLinkedList("ac")),
        (getLinkedList(["aaa"]), getLinkedList("a")),
        (getLinkedList(["aba"]), getLinkedList("ab")),
        (getLinkedList(["abab"]), getLinkedList("ab"))
    ]

    for (input, expected) in data:
        RemoveDuplicateV2(input)
        assert input == expected