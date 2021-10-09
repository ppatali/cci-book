class Stack:
    def __init__(self) -> None:
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()        
    def peek(self):
        if self.items:
            return self.items[- 1]
        return None
    def __len__(self):
        return len(self.items)
    def __bool__(self):
        return bool(self.items)
    