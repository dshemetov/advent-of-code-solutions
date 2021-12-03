from advent_tools import Puzzle

def solve(s: str) -> int:
    nums = list(int(x) for x in s.split("\n"))
    return sum(1 if y > x else 0 for x, y in zip(nums[:-1], nums[1:]))

class Solution:
    @property
    def answer(self):
        return solve(Puzzle(1, 2021).input_data)