
from app import add, sub

# Test function for add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test function for sub
def test_sub():
    assert sub(3, 2) == 1
    assert sub(10, 5) == 5
    assert sub(0, 0) == 0