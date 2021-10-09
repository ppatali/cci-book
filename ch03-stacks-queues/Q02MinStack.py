import sys
from stack import Stack

class MinStack(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.minStack = Stack()
    
    def min(self):
        if (self.minStack.isEmpty()):
            return sys.maxsize
        else:
            return self.minStack.peek()
    
    def push(self, value):
        if value <= self.min():
            self.minStack.push(value)
        super().push(value)
    
    def pop(self):
        value = super().pop()
        if value == self.min():
            self.minStack.pop()
        return value
    