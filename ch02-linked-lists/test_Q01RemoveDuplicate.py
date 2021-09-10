from LinkedList import *
from Q01RemoveDuplicate import *

def test_Cases():
    data = [
        (LinkedListNode("a", LinkedListNode("b", LinkedListNode("c"))), LinkedListNode("a", LinkedListNode("b", LinkedListNode("c")))),
        (LinkedListNode("a", LinkedListNode("a", LinkedListNode("c"))), LinkedListNode("a", LinkedListNode("c"))),
        (LinkedListNode("a", LinkedListNode("a", LinkedListNode("a"))), LinkedListNode("a")),
        (LinkedListNode("a", LinkedListNode("b", LinkedListNode("a"))), LinkedListNode("a", LinkedListNode("b"))),
        (LinkedListNode("a", LinkedListNode("b", LinkedListNode("a", LinkedListNode("b")))), LinkedListNode("a", LinkedListNode("b")))        
    ]

    for (input, expected) in data:
        RemoveDuplicate(input)
        assert input == expected

def test_CasesV2():
    data = [
        (LinkedListNode("a", LinkedListNode("b", LinkedListNode("c"))), LinkedListNode("a", LinkedListNode("b", LinkedListNode("c")))),
        (LinkedListNode("a", LinkedListNode("a", LinkedListNode("c"))), LinkedListNode("a", LinkedListNode("c"))),
        (LinkedListNode("a", LinkedListNode("a", LinkedListNode("a"))), LinkedListNode("a")),
        (LinkedListNode("a", LinkedListNode("b", LinkedListNode("a"))), LinkedListNode("a", LinkedListNode("b"))),
        (LinkedListNode("a", LinkedListNode("b", LinkedListNode("a", LinkedListNode("b")))), LinkedListNode("a", LinkedListNode("b")))        
    ]

    for (input, expected) in data:
        RemoveDuplicateV2(input)
        assert input == expected