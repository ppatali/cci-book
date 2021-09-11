from LinkedList import *
from Q01RemoveDuplicate import *

def test_Cases():
    data = [
        (generateLinkedList(["abc"]), generateLinkedList("abc")),
        (generateLinkedList(["aac"]), generateLinkedList("ac")),
        (generateLinkedList(["aaa"]), generateLinkedList("a")),
        (generateLinkedList(["aba"]), generateLinkedList("ab")),
        (generateLinkedList(["abab"]), generateLinkedList("ab"))
    ]

    for (input, expected) in data:
        RemoveDuplicate(input)
        assert input == expected

def test_CasesV2():
    data = [
        (generateLinkedList(["abc"]), generateLinkedList("abc")),
        (generateLinkedList(["aac"]), generateLinkedList("ac")),
        (generateLinkedList(["aaa"]), generateLinkedList("a")),
        (generateLinkedList(["aba"]), generateLinkedList("ab")),
        (generateLinkedList(["abab"]), generateLinkedList("ab"))
    ]

    for (input, expected) in data:
        RemoveDuplicateV2(input)
        assert input == expected