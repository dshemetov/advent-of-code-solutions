from advent_tools import Puzzle


def solve_a(s: str) -> int:
    return max(get_seatid(line) for line in s.split("\n"))


def get_seatid(s: str) -> int:
    return 8 * get_row(s[:7]) + get_col(s[7:])


def get_row(s: str) -> int:
    return int(s.replace("B", "1").replace("F", "0"), 2)


def get_col(s: str) -> int:
    return int(s.replace("R", "1").replace("L", "0"), 2)


def solve_b(s: str) -> int:
    ids = set([get_seatid(line) for line in s.split("\n")])
    for x in ids:
        if x + 1 not in ids and x + 2 in ids:
            break
    return x + 1


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(5, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(5, 2020).input_data)
