from LinkedList import *

def PartitionList(head: LinkedListNode, x: int) -> LinkedListNode:
    beforHead = beforeTail = afterHead = afterTail = None

    current = head
    while current != None:
        next = current.next
        current.next = None
        if current.value < x:
            if beforHead == None:
                beforHead = beforeTail = current
            else:
                beforeTail.next = current
                beforeTail = current
        else:
            if afterHead == None:
                afterHead = afterTail = current
            else:
                afterTail.next = current
                afterTail = current
        
        current = next
    
    if beforHead == None:
        return afterHead
    
    beforeTail.next = afterHead
    return beforHead

def PartitionList2(head: LinkedListNode, x: int) -> LinkedListNode:
    newHead = newTail = head
    current = head
    
    while current != None:
        next = current.next
        if current.value < x:
            current.next = newHead
            newHead = current
        else:
            newTail.next = current
            newTail = current
            newTail.next = None
        current = next
    
    return newHead
