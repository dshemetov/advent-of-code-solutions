import pytest
from .p7 import solve_a, solve_b

test_string = """16,1,2,0,4,2,7,1,2,14
"""

def test_solve_a():
    assert solve_a(test_string) == 37

def test_solve_b():
    assert solve_b(test_string) == 168