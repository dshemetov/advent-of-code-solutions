from advent_tools import Puzzle
import numpy as np

def solve_a(s: str) -> int:
    lines = [line.split("->") for line in s.split("\n")]
    lines = np.array([[start.split(","), end.split(",")] for start, end in lines], dtype=int)
    n, m = lines.max(axis=(0, 1)) + 1
    grid = np.zeros((n, m))

    for pt1, pt2 in lines:
        if (pt1 == pt2).any():
            xs, ys = make_line(pt1, pt2).T
            grid[xs, ys] += 1

    return (grid > 1).flatten().sum()

def make_line(pt1: np.ndarray, pt2: np.ndarray) -> np.ndarray:
    n = np.abs(pt1 - pt2).max()
    d = (pt1 - pt2) // n
    return np.vstack([pt2 + d * i for i in range(n+1)])

def solve_b(s: str) -> int:
    lines = [line.split("->") for line in s.split("\n")]
    lines = np.array([[start.split(","), end.split(",")] for start, end in lines], dtype=int)
    n, m = lines.max(axis=(0, 1)) + 1
    grid = np.zeros((n, m))

    for pt1, pt2 in lines:
        xs, ys = make_line(pt1, pt2).T
        grid[xs, ys] += 1

    return (grid > 1).flatten().sum()


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(5, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(5, 2021).input_data)