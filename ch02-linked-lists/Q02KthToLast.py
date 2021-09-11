from LinkedList import *

def KthToLast(head : LinkedListNode, k : int) -> LinkedListNode:
    runner = head
    while runner != None and k > 0:
        k -= 1
        runner = runner.next
    
    if runner == None and k > 0:
        return None
    
    kth = head
    while runner != None:
        kth = kth.next
        runner = runner.next
    
    return kth

    



