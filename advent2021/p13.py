from advent_tools import Puzzle
import numpy as np
import re
from typing import List

def solve_a(s: str) -> int:
    ixs, folds = s.split("\n\n")
    ixs = np.array([line.split(",") for line in ixs.strip("\n").split("\n")], dtype=int)[:,::-1].T
    n, m = ixs.max(axis=1) + 1
    mat = np.zeros((n, m), dtype=bool)
    mat[ixs[0], ixs[1]] = True

    folds = [re.match("fold along (\w)=(\d+)", line).groups() for line in folds.split("\n")][0:1]
    for along, _ in folds:
        mat = fold_mat(along, mat)

    return mat.sum()

def fold_mat(along: str, mat: List[List[str]]) -> List[List[str]]:
    n, m = mat.shape
    if along == "y":
        new_mat = mat[0:n//2, :] | mat[:n//2:-1, :]
    if along == "x":
        new_mat = mat[:, 0:m//2] | mat[:, :m//2:-1]
    return new_mat

def solve_b(s: str) -> str:
    ixs, folds = s.split("\n\n")
    ixs = [line.split(",") for line in ixs.strip("\n").split("\n")]
    ixs = [(int(x), int(y)) for y, x in ixs]

    n, m = max(x for x, _ in ixs) + 1, max(y for _, y in ixs) + 1
    mat = np.zeros((n, m), dtype=bool)
    for i, j in ixs:
        mat[i][j] = True

    folds = [re.match("fold along (\w)=(\d+)", line).groups() for line in folds.split("\n")]
    for along, _ in folds:
        mat = fold_mat(along, mat)

    return "\n".join(["".join(["1" if x else " " for x in row]) for row in mat])


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(13, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(13, 2021).input_data)
