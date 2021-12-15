import pytest
from .p14 import solve_a, solve_b

test_string = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

def test_solve_a():
    assert solve_a(test_string) == 1588

def test_solve_b():
    assert solve_b(test_string) == 2188189693529
