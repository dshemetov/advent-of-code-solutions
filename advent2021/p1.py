from advent_tools import Puzzle

def solve_a(s: str) -> int:
    nums = list(int(x) for x in s.split("\n"))
    return sum(1 if y > x else 0 for x, y in zip(nums[:-1], nums[1:]))

def solve_b(s: str) -> int:
    nums = list(int(x) for x in s.split("\n"))
    windowed_sums = list(sum(triple) for triple in zip(nums[:-2], nums[1:-1], nums[2:]))
    return sum(1 if y > x else 0  for x, y in zip(windowed_sums[:-1], windowed_sums[1:]))


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(1, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(1, 2021).input_data)
