from LinkedList import *
from Q03DeleteMiddleNode import *

def test_Cases1():
    inputList = generateLinkedList("abcdef")
    toDelete = inputList.next.next
    expectDeleted = True
    expectedList = generateLinkedList("abdef")
    
    deleted = DeleteMiddleNode(toDelete)
    
    assert deleted == expectDeleted and inputList == expectedList

def test_CasesCantDeleteLastNode():
    inputList = generateLinkedList("abcd")
    toDelete = inputList.next.next.next
    expectDeleted = False
    expectedList = generateLinkedList("abcd")
    
    deleted = DeleteMiddleNode(toDelete)
    
    assert deleted == expectDeleted and inputList == expectedList

def test_Cases2():
    inputList = generateLinkedList("abcdefg")
    toDelete = inputList.next.next.next.next.next
    expectDeleted = True
    expectedList = generateLinkedList("abcdeg")
    
    deleted = DeleteMiddleNode(toDelete)
    
    assert deleted == expectDeleted and inputList == expectedList