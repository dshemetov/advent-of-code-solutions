import pytest
from .p1a import solve

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

def test_solve():
    assert solve(test_string) == 7
