from LinkedList import *

def PalindromeByReversing(head: LinkedListNode) -> bool:
    clone = ReverseAndClone(head)
    return clone == head

def ReverseAndClone(head:LinkedListNode) -> LinkedListNode:
    node = head
    newHead = None

    while node:
        newNode = LinkedListNode(node.value)
        newNode.next = newHead
        newHead = newNode
        node = node.next

    return newHead

def PalindromeByHalf(head: LinkedListNode) -> bool:
    fast = slow = head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next
    
    while slow:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next
    
    return True
