from advent_tools import Puzzle, reverse_dict
from enum import Enum
from typing import Optional, Tuple

close_to_open = dict({
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
})
open_to_close = reverse_dict(close_to_open)

class LineType(Enum):
    VALID = 0
    CORRUPTED = 1
    INCOMPLETE = 2

def solve_a(s: str) -> int:
    return sum(y for x, y in (parse_line(line) for line in s.split("\n")) if x == LineType.CORRUPTED)

def get_corrupted_line_score(x: str) -> str:
    char_scores = dict({")": 3, "]": 57, "}": 1197, ">": 25137})
    return char_scores[x]

def parse_line(s: str) -> Tuple[LineType, Optional[int]]:
    stack = []
    for x in s:
        if x in {"(", "[", "<", "{"}:
            stack.append(x)
        else:
            c = stack.pop()
            if close_to_open[x] != c:
                return (LineType.CORRUPTED, get_corrupted_line_score(x))
    if len(stack) > 0:
        return (LineType.INCOMPLETE, get_completion_string_score("".join(open_to_close[x] for x in reversed(stack))))
    return (LineType.VALID, None)

def solve_b(s: str) -> int:
    scores = [y for x, y in (parse_line(line) for line in s.split("\n")) if x == LineType.INCOMPLETE]
    return sorted(scores)[len(scores) // 2]

def get_completion_string_score(s: str) -> int:
    char_scores = dict({")": 1, "]": 2, "}": 3, ">": 4})
    score = 0
    for x in s:
        score *= 5
        score += char_scores[x]
    return score


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(10, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(10, 2021).input_data)
