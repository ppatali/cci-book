class Node(object):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.above = None
        self.below = None

class Stack(object):
    def __init__(self, capacity) -> None:
        super().__init__()
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        if self.is_full():
            return False
        
        node = Node(value)
        self.size += 1
        if self.size == 1:
            self.bottom = node
            self.top = node
        else:
            node.below = self.top
            self.top.above = node
            self.top = node

        return True
    
    def pop(self):
        if self.is_empty():
            return None
        
        node = self.top
        if node.below:
            node.below.above = None
        self.top = node.below

        self.size -= 1        
        return node.value
    
    def remove_bottom(self):
        if self.is_empty():
            return None
        
        node = self.bottom
        node.above.below = None
        self.bottom = node.above

        self.size -= 1
        return node.value

class SetOfStacks(object):
    def __init__(self, capacity) -> None:
        super().__init__()
        self.capacity = capacity
        self.stacks = []
    
    def get_last_stack(self) -> Stack:
        if not self.stacks:
            return None
        return self.stacks[-1]
    
    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()
    
    def push(self, value):
        last = self.get_last_stack()
        if not last or last.is_full():
            last = Stack(self.capacity)
            self.stacks.append(last)
        
        last.push(value)
    
    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        
        value = last.pop()
        if last.is_empty():
            del self.stacks[-1]

        return value
    
    def pop_At(self, index):
        return self.shiftLeft(index, True)
    
    def shiftLeft(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stacks[index]
        elif index + 1 < len(self.stacks):
            v = self.shiftLeft(index + 1, False)
            stack.push(v)
        return removed_item
    
