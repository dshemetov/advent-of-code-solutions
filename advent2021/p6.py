from advent_tools import Puzzle
from collections import Counter
import numpy as np

def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    5934
    """
    fish_ages = Counter(int(x) for x in s.split(","))
    return get_number_fish_after_days(fish_ages, 80)

def get_number_fish_after_days(fish_ages: Counter, n: int) -> int:
    """
    Examples:
    >>> get_number_fish_after_days(test_string, 18)
    26
    """
    return pass_days(fish_ages, n).sum()

def pass_days(fish_ages: Counter, n: int = 1) -> np.ndarray:
    A = np.diag([1] * 8, k=1); A[8, 0] = A[6, 0] = 1
    v = np.array([fish_ages[i] for i in range(9)])
    for _ in range(n):
        v = A @ v
    return v

def solve_b(s: str) -> int:
    fish_ages = Counter(int(x) for x in s.split(","))
    return get_number_fish_after_days(fish_ages, 256)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(6, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(6, 2021).input_data)

test_string = """3,4,3,1,2
"""