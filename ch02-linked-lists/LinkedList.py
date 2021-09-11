class LinkedListNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
   
    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, o: object) -> bool:
        if type(self) != type(o):
            return False
        
        s1 = self
        s2 = o
        while (s1 != None and s2 != None):
            if (s1.value != s2.value):
                return False
            s1 = s1.next
            s2 = s2.next

        return s1 == None and s2 == None
    
def generateLinkedList(values: str) -> LinkedListNode:
    head = tail = None
    for i in range(len(values)):
        node = LinkedListNode(values[i], None, tail)       
        if head == None:
            head = node
        else:
            tail.next = node
        tail = node
    
    return head