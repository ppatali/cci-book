import pytest
from Q03StackOfPlates import *

def test_stack():
    stacks = SetOfStacks(5)
    for i in range(35):
        stacks.push(i)
    lst = []
    for _ in range(35):
        lst.append(stacks.pop())

    assert lst == list(reversed(range(35))) 

def test_popAt():
    stacks = SetOfStacks(5)
    for i in range(35):
        stacks.push(i)
    lst = []
    for _ in range(31):
        lst.append(stacks.pop_At(0))
    
    assert lst == list(range(4,35))

