import pytest
from .p15 import solve_a, solve_b

test_string = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

def test_solve_a():
    assert solve_a(test_string) == 40

def test_solve_b():
    assert solve_b(test_string) == 315
