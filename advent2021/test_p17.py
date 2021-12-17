import pytest
from .p17 import solve_a, solve_b

test_string = """target area: x=20..30, y=-10..-5"""

def test_solve_a():
    assert solve_a(test_string) == 45

def test_solve_b():
    assert solve_b(test_string) == 112
