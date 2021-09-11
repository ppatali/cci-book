from LinkedList import *
from Q02KthToLast import *

def test_Cases():
    data = [
        (None, 10102, None),
        (generateLinkedList("a"), 2, None),
        (generateLinkedList("a"), 1, "a"),
        (generateLinkedList("abc"), 2, "b"),
        (generateLinkedList("987654321"), 7, "7")
    ]

    for (input, k, expected) in data:
        kthnode = KthToLast(input, k)
        if kthnode != None:
            kthnode = kthnode.value
        assert kthnode == expected #Currently doing value comparision

