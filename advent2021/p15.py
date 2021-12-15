from typing import Tuple
from advent_tools import Puzzle, get_valid_neighbor_ixs
import numpy as np
from heapq import heappush, heappop

def solve_a(s: str) -> int:
    mat = np.array([list(line) for line in s.split("\n")], dtype=int)
    n, m = mat.shape
    actual_cost, _ = get_minimum_path((0, 0), (n-1, m-1), mat)
    return actual_cost

def get_minimum_path(start: Tuple[int, int], end: Tuple[int, int], mat: np.ndarray) -> np.ndarray:
    i, j = start
    cost = 0
    priority_queue = []
    best_cost = dict()

    while end != (i, j):
        for i_, j_ in get_valid_neighbor_ixs(i, j, mat):
            cost_ = cost + mat[i_, j_]
            if (i_, j_) in best_cost and best_cost[(i_, j_)] <= cost_:
                continue
            best_cost[(i_, j_)] = min(best_cost[(i_, j_)] if (i_, j_) in best_cost else cost_, cost_)
            heappush(priority_queue, (cost_, (i_, j_)))
        cost, (i, j) = heappop(priority_queue)

    return cost, (i, j)

def solve_b(s: str) -> int:
    mat = np.array([list(line) for line in s.split("\n")], dtype=int)
    big_mat = expand_mat(mat)
    n, m = big_mat.shape
    actual_cost, _ = get_minimum_path((0, 0), (n-1, m-1), big_mat)
    return actual_cost

def expand_mat(mat):
    n, _ = mat.shape
    ntile = 5
    nxp = ntile * n
    graph_tiled = np.zeros((nxp, nxp), dtype=int)
    for xtile in range(ntile):
        for ytile in range(ntile):
            xs, ys = xtile * n, ytile * n
            xe, ye = (xtile+1)* n, (ytile+1) * n
            z_offset = xtile + ytile
            graph_tiled[xs:xe, ys:ye] = (mat + z_offset - 1) % 9 + 1

    return graph_tiled


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(15, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(15, 2021).input_data)
