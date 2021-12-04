import pytest
from .p1 import solve_a, solve_b

test_string = """199
200
208
210
200
207
240
269
260
263"""

def test_solve_a():
    assert solve_a(test_string) == 7

def test_solve_b():
    assert solve_b(test_string) == 5