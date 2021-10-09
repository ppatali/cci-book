import pytest
from Q02MinStack import *

def test_Cases1():
    s1 = MinStack()
    assert s1.isEmpty()

    s1.push(5)
    s1.push(6)
    assert s1.min() == 5

    s1.push(3)
    assert s1.min() == 3

    s1.push(7)
    assert s1.min() == 3

    s1.pop()
    s1.pop()
    assert s1.min() == 5
    