"""Chiton
https://adventofcode.com/2021/day/15
"""
from heapq import heappop, heappush
from typing import Tuple

import numpy as np
from advent_tools import get_valid_neighbor_ixs


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    40
    """
    mat = np.array([list(line) for line in s.split("\n")], dtype=int)
    n, m = mat.shape
    actual_cost, _ = get_minimum_path(mat, (0, 0), (n - 1, m - 1))
    return actual_cost


def get_minimum_path(mat: np.ndarray, start_ix: Tuple[int, int], end_ix: Tuple[int, int]) -> np.ndarray:
    ix = start_ix
    cost = 0
    priority_queue = []
    best_cost = dict()

    while end_ix != ix:
        for ix_ in get_valid_neighbor_ixs(ix, mat.shape):
            cost_ = cost + mat[ix_]
            if ix_ in best_cost and best_cost[ix_] <= cost_:
                continue
            best_cost[ix_] = min(best_cost.get(ix_, cost_), cost_)
            heappush(priority_queue, (cost_, ix_))
        cost, ix = heappop(priority_queue)

    return cost, ix


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    315
    """
    mat = np.array([list(line) for line in s.split("\n")], dtype=int)
    big_mat = expand_mat(mat)
    n, m = big_mat.shape
    actual_cost, _ = get_minimum_path(big_mat, (0, 0), (n - 1, m - 1))
    return actual_cost


def expand_mat(mat):
    n, _ = mat.shape
    ntile = 5
    nxp = ntile * n
    graph_tiled = np.zeros((nxp, nxp), dtype=int)
    for xtile in range(ntile):
        for ytile in range(ntile):
            xs, ys = xtile * n, ytile * n
            xe, ye = (xtile + 1) * n, (ytile + 1) * n
            graph_tiled[xs:xe, ys:ye] = (mat + xtile + ytile - 1) % 9 + 1

    return graph_tiled


test_string = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
