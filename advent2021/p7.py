from advent_tools import Puzzle
import numpy as np

def solve_a(s: str) -> int:
    nums = np.array([s.split(",")], dtype=int)
    point = int(np.median(nums))
    return np.abs(point - nums).sum()

def solve_b(s: str) -> int:
    nums = np.array([int(x) for x in s.split(",")])
    options = (np.mean(nums) + np.array([-2, -1, 0, 1, 2])).astype(int)
    return min(point_cost(x, nums) for x in options)

def point_cost(n: int, nums: np.ndarray) -> int:
    return sum(i*(i+1)//2 for i in np.abs(n - nums))


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(7, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(7, 2021).input_data)
