from advent_tools import Puzzle, get_valid_neighbor_ixs
from typing import Tuple
import numpy as np
from itertools import product

def solve_a(s: str) -> int:
    mat = parse_input(s)
    _, flashes = run_octopus_steps(mat, 100)
    return flashes

def parse_input(s: str) -> np.ndarray:
    return np.array([list(line) for line in s.split("\n")], dtype=int)

def run_octopus_step(mat: np.ndarray) -> Tuple[np.ndarray, int]:
    mat = mat.copy()
    mat += 1
    n, m = mat.shape
    already_flashed = set()
    ixs_to_check = set((i, j) for i, j in product(range(n), range(m)) if mat[i, j] > 9)
    while len(ixs_to_check) > 0:
        i, j = ixs_to_check.pop()
        if mat[i, j] > 9 and (i, j) not in already_flashed:
            already_flashed |= {(i, j)}
            for i_, j_ in get_valid_neighbor_ixs(i, j, mat, diagonals=True):
                mat[i_, j_] += 1
                ixs_to_check |= {(i_, j_)}
    mat[np.where(mat > 9)] = 0
    return mat, len(already_flashed)

def run_octopus_steps(mat: np.ndarray, n: int) -> Tuple[np.ndarray, int]:
    flash_counter = 0
    mat_ = mat.copy()
    for _ in range(n):
        mat_, flashes = run_octopus_step(mat_)
        flash_counter += flashes
    return mat_, flash_counter

def solve_b(s: str) -> int:
    mat = parse_input(s)
    i = 1
    while True:
        mat, _ = run_octopus_step(mat)
        if (mat == 0).all():
            break
        i += 1
    return i


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(11, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(11, 2021).input_data)
