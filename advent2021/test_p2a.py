import pytest
from .p2a import solve

test_string = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def test_solve():
    assert solve(test_string) == 150
