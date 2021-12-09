import pytest
from .p9 import solve_a, solve_b

test_string = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def test_solve_a():
    assert solve_a(test_string) == 15

def test_solve_b():
    assert solve_b(test_string) == 1134