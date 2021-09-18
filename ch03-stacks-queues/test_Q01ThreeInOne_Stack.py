import pytest
from Q01ThreeInOne_Stack import *

def test_Cases1():
    s = MultiStack(2, 2)
    
    assert s.isEmpty(0)
    assert s.isEmpty(1)
    assert not s.isFull(0)
    assert not s.isFull(1)
    
    s.push(100, 1)
    assert s.isEmpty(0)
    assert not s.isEmpty(1)
    assert not s.isFull(0)
    assert not s.isFull(1)
    
    s.push(200, 1)
    assert s.isEmpty(0)
    assert not s.isEmpty(1)
    assert not s.isFull(0)
    assert s.isFull(1)

    with pytest.raises(FullStackError):
        s.push(300, 1)
    
    with pytest.raises(EmptyStackError):
        s.pop(0)
    
    assert s.pop(1) == 200
    assert s.pop(1) == 100

    s.push(111, 0)
    s.push(222, 0)
    
    assert s.pop(0) == 222
    assert s.pop(0) == 111
