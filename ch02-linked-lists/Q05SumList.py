from LinkedList import *

def SumList(l1: LinkedListNode, l2:LinkedListNode) -> LinkedListNode:
    carry = 0
    l3Head = l3Tail = None
    while l1 != None or l2 != None or carry == 1:
        value = carry
        if l1:
            value += l1.value
            l1 = l1.next
        if l2:
            value += l2.value
            l2 = l2.next

        node = LinkedListNode(value % 10)
        carry = 1 if value >= 10 else 0
        if l3Head == None:
            l3Head = l3Tail = node
        else:
            l3Tail.next = node
            l3Tail = node
    
    return l3Head

def SumListReverse(l1: LinkedListNode, l2:LinkedListNode) -> LinkedListNode:
    
    len1 = listlength(l1)
    len2 = listlength(l2)

    # Make them equal by padding 0 to smaller list
    if len1 < len2:
        l1 = padLeft(l1, len2 - len1)
    elif len1 > len2:
        l2 = padLeft(l2, len1 - len2)
    
    sum = 0
    while l1 != None and l2 != None:
        sum = (sum * 10) + l1.value + l2.value
        l1 = l1.next
        l2 = l2.next
    
    l3Head = l3Tail = None
    for c in str(sum):
        node = LinkedListNode(int(c))
        if l3Head == None:
            l3Head = l3Tail = node
        else:
            l3Tail.next = node
            l3Tail = node

    return l3Head

def listlength(l: LinkedListNode) -> int:
    length = 0
    while l != None:
        length += 1
        l = l.next
    return length

def padLeft(l: LinkedListNode, padding: int) -> LinkedListNode:
    head = l
    for i in range(padding):
        head = insertBefore(head, 0)
    return head

def insertBefore(l: LinkedListNode, value: int) -> LinkedListNode:
    node = LinkedListNode(value)
    if l:
        node.next = l
    return node

