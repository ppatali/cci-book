from LinkedList import *
from Q08Intersection import *

def test_Cases():
    head1 = generateLinkedList([3,1,5,9,7,2,1])
    head2 = generateLinkedList([4,6])
    head2.next.next = head1.next.next.next.next
    expected = generateLinkedList([7,2,1])

    assert FindIntersection(head1, head2) == expected