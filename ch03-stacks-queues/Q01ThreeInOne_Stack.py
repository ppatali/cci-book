
class MultiStack:
    def __init__(self, capacity: int, stack_count: int) -> None:
        self.capacity = capacity
        self.stack_count = stack_count
        self.array = [0] * (self.capacity * self.stack_count)
        self.sizes = [0] * self.stack_count

    def push(self, value, stack_num):
        if self.isFull(stack_num):
            raise FullStackError(f"stack #{stack_num} is full")
        self.sizes[stack_num] += 1
        self.array[self.get_top_index(stack_num)] = value
    
    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            raise EmptyStackError(f"stack #{stack_num} is empty")
        
        value = self.array[self.get_top_index(stack_num)]
        self.array[self.get_top_index(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        return self.array[self.get_top_index(stack_num)]

    def isEmpty(self, stack_num):
        self._valid_stack_num_(stack_num)
        return self.sizes[stack_num] == 0

    def isFull(self, stack_num):
        self._valid_stack_num_(stack_num)
        return self.sizes[stack_num] == self.capacity
    
    def get_top_index(self, stack_num):
        self._valid_stack_num_(stack_num)
        offset = self.sizes[stack_num] - 1
        return stack_num * self.capacity + offset 

    def _valid_stack_num_(self, stack_num):
        if (stack_num < 0 or stack_num >= self.stack_count):
            raise UnknownStackError(F"stack #{stack_num} does not exists")


class MultiStackError(Exception):
    """MultiStack operation error""" 

class FullStackError(MultiStackError):
    """stack is full""" 

class EmptyStackError(MultiStackError):
    """stack is empty""" 

class UnknownStackError(MultiStackError):
    """stack not found""" 
