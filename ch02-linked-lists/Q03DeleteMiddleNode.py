from LinkedList import * 

def DeleteMiddleNode(node: LinkedListNode):
    deleted = False
    if node != None and node.next != None:
        node.value = node.next.value # copy data
        next = node.next 
        node.next = next.next 
        next.next = None # Removing the reference
        deleted = True
    
    return deleted

