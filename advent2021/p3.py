from advent_tools import Puzzle, binary_to_int
from copy import copy
import numpy as np

def solve_a(s: str) -> int:
    mat = np.array([list(line) for line in s.split("\n")], dtype=int)
    n, _ = mat.shape
    max_rows = mat.sum(axis=0) >= n / 2
    min_rows = ~max_rows
    gamma_rate, epsilon_rate = binary_to_int(max_rows), binary_to_int(min_rows)
    return gamma_rate * epsilon_rate

def solve_b(s: str) -> int:
    mat = np.array([list(line) for line in s.split("\n")], dtype=int)
    _, m = mat.shape

    mat_ = copy(mat)
    for ix in range(m):
        if len(mat_) == 1:
            break
        n, _ = mat_.shape
        mat_ = mat_[mat_[:, ix] == int(mat_[:, ix].sum() >= n / 2)]
    oxygen_rating = binary_to_int(mat_[0])

    mat_ = copy(mat)
    for ix in range(m):
        if len(mat_) == 1:
            break
        n, _ = mat_.shape
        mat_ = mat_[mat_[:, ix] == int(mat_[:, ix].sum() < n / 2)]
    co2_rating = binary_to_int(mat_[0])

    return oxygen_rating * co2_rating


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(3, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(3, 2021).input_data)
