import pytest
from .p2 import solve_a, solve_b

test_string = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def test_solve_a():
    assert solve_a(test_string) == 150

def test_solve_b():
    assert solve_b(test_string) == 900