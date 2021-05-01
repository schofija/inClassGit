import calc
import pytest

def test_add():
    assert calc.add(10, 5) == 15
    
def test_sub():
    assert calc.sub(10, 5) == 5
    
def test_mul():
    assert calc.mul(10, 5) == 50

def test_div():
    assert calc.div(10,5) == 2