from LinkedList import *
from Q08LoopDetection import *

def test_Cases():
    head = generateLinkedList("ABCDE")
    head.next.next.next.next = head.next.next

    loopStart = FindLoopStart(head)
    assert loopStart.value == "C"

def test_CasesNoLoop():
    head = generateLinkedList("ABCDE")

    loopStart = FindLoopStart(head)
    assert loopStart == None

def test_CasesFromHead():
    head = generateLinkedList("ABCDE")
    head.next.next.next.next = head

    loopStart = FindLoopStart(head)
    assert loopStart.value == "A"