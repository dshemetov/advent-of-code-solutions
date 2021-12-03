from advent_tools import Puzzle

def solve(s: str) -> int:
    x, y = 0, 0
    for dir, n in (line.split(" ") for line in s.split("\n")):
        if dir == "forward":
            x += int(n)
        if dir == "up":
            y += int(n)
        if dir == "down":
            y -= int(n)
    return abs(x * y)

class Solution:
    @property
    def answer(self):
        return solve(Puzzle(2, 2021).input_data)
