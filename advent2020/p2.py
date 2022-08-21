from advent_tools import Puzzle
import re


def solve_a(s: str) -> int:
    lines = (m.groups() for m in re.finditer("(\d+)-(\d+) (\w): (\w+)", s))
    return sum(1 if int(cmin) <= password.count(char) <= int(cmax) else 0 for cmin, cmax, char, password in lines)


def solve_b(s: str) -> int:
    lines = (m.groups() for m in re.finditer("(\d+)-(\d+) (\w): (\w+)", s))
    return sum(1 if (password[int(cmin) - 1] == char) ^ (password[int(cmax) - 1] == char) else 0 for cmin, cmax, char, password in lines)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(2, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(2, 2020).input_data)
