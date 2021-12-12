import pytest
from .p12 import solve_a, solve_b

test_strings = [
"""start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
"""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
"""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
]

def test_solve_a():
    assert solve_a(test_strings[0]) == 10
    assert solve_a(test_strings[1]) == 19
    assert solve_a(test_strings[2]) == 226

def test_solve_b():
    assert solve_b(test_strings[0]) == 36
    assert solve_b(test_strings[1]) == 103
    assert solve_b(test_strings[2]) == 3509
