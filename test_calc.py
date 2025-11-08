import pytest

from calc import add, sub, multi, div

def test_add():
    # Compare actaul o/p and expected o/p
    assert add(2, 3) == 5

def test_sub():
    assert sub(3, 1) == 2

def test_multi():
    assert multi(4, 2) == 8

def test_div():
    assert div(4, 2) == 2
    