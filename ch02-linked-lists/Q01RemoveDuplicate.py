from typing import Optional
from LinkedList import *

def RemoveDuplicate(head : Optional[LinkedListNode]) -> None:
    current = head

    if (current == None or current.next == None):
        return
    
    seen = set([current.value])
    
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

def RemoveDuplicateV2(head : Optional[LinkedListNode]) -> None:
    current = head

    if (current == None or current.next == None):
        return

    while current:
        runner = current
        while runner.next:
            if (current.value == runner.next.value):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
