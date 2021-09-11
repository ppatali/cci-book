from LinkedList import *
from Q04Partition import *

def test_Cases():
    data = [
        (generateLinkedList([3,5,8,5,10,2,1]), 5, generateLinkedList([3,2,1,5,8,5,10]))
    ]

    for (input, x, expected) in data:
        assert PartitionList(input, x) == expected 


def test_Cases2():
    data = [
        (generateLinkedList([3,5,8,5,10,2,1]), 5, generateLinkedList([1,2,3,5,8,5,10]))
    ]

    for (input, x, expected) in data:
        assert PartitionList2(input, x) == expected 