from typing import Tuple
from LinkedList import *


def FindIntersection(head1: LinkedListNode, head2: LinkedListNode) -> LinkedListNode:
    tail1, len1 = FindLenAndLastNode(head1)
    tail2, len2 = FindLenAndLastNode(head2)

    if tail1 is not tail2: #reference comparison
        return None
    
    short = head1
    long = head2
    diff = len2 - len1
    if len1 > len2:
        short = head2
        long = head1
        diff = -diff

    while diff > 0: # Skip nodes
        long = long.next
        diff -= 1

    while short is not long: #reference comparison
        short = short.next
        long = long.next
    
    return short


def FindLenAndLastNode(head: LinkedListNode) -> Tuple[LinkedListNode, int]:
    node = head
    length = 0

    while node and node.next:
        length += 1
        node = node.next
    
    return (node, length)