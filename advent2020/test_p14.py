import pytest
from .p14 import int_to_bits, solve_a, solve_b

test_string = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

test_string2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

def test_solve_a():
    assert int_to_bits(11) == 32 * [0] + [1, 0, 1, 1]
    assert solve_a(test_string) == 165

def test_solve_b():
    assert solve_b(test_string2) == 208