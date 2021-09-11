from LinkedList import *

def FindLoopStart(head: LinkedListNode) -> LinkedListNode:
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            break
    
    if fast is not slow:
        return None
    
    slow = head
    while fast is not slow:
        slow = slow.next
        fast = fast.next
    
    return slow

    