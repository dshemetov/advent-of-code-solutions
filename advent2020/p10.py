from advent_tools import Puzzle
from functools import reduce
from itertools import chain, islice, tee
from functools import reduce
from sympy import symbols, Poly

def solve_a(s: str) -> int:
    nums = [int(line) for line in s.split("\n")]
    nums = [0] + sorted(nums) + [max(nums) + 3]
    diffs = [y-x for x,y in zip(nums[:-1], nums[1:])]
    return diffs.count(1) * diffs.count(3)

def solve_b(s: str) -> int:
    # Get the sorted adapter sequence
    nums = [int(line) for line in s.split("\n")]
    nums = chain([0], sorted(nums), [max(nums) + 3])
    # Find the diffs, add a 3 at the beginning and end to cap off edge 1-sequences
    diffs = chain([3], diff(nums), [3])
    # Find the end points of the 1-sequences
    ixs = (i for i, x in enumerate(diffs) if x == 3)
    # The length of the 1-sequence [a, b] is (b - a - 1)
    diffs = (integer_composition(x-1) for x in diff(ixs))
    return reduce(lambda x, y: x * y, diffs)

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    return zip(a, islice(b, 1, None))

def diff(iterable):
    """s -> s1-s0, s2-s1, s3-s2, ..."""
    return (y-x for x, y in pairwise(iterable))

def integer_composition(n):
    x = symbols('x')
    f = 0
    for k in range(n+1):
        f += (x + x**2 + x**3)**k
    return Poly(f, x).coeff_monomial(x**n)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(10, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(10, 2020).input_data)
