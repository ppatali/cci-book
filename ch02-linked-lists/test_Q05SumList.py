from LinkedList import *
from Q05SumList import *

def test_Cases():
    data = [
        (generateLinkedList([7,1,6]), generateLinkedList([5,9,2]), generateLinkedList([2,1,9])),
        (generateLinkedList([7,1,6]), generateLinkedList([5,9]), generateLinkedList([2,1,7])),
        (generateLinkedList([7,1,6]), generateLinkedList([5,9,6]), generateLinkedList([2,1,3,1])),
    ]

    for (l1, l2, l3) in data:
        assert SumList(l1, l2) == l3

def test_CasesReverse():
    data = [
        (generateLinkedList([7,1,6]), generateLinkedList([5,9,2]), generateLinkedList([1,3,0,8])),
        (generateLinkedList([7,1,6]), generateLinkedList([5,9]), generateLinkedList([7,7,5])),
        (generateLinkedList([7,1,6]), generateLinkedList([5,9,6]), generateLinkedList([1,3,1,2])),
    ]

    for (l1, l2, l3) in data:
        assert SumListReverse(l1, l2) == l3