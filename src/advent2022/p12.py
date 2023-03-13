# %%
"""Hill Climbing Algorithm
https://adventofcode.com/2022/day/12

TODO: The solution to part a is very slow. Would benefit from optimizations.
- A heuristic function didn't help.
- Writing this in Cython is hard because of the use of heapq -- I don't easy access to a resizable array.
TODO: The solution to b depends on a and is also very slow. Would have additional optimizations, after a is optimized.
"""
from heapq import heappop, heappush
from typing import Tuple

import numba as nb
import numpy as np
from advent_tools import get_valid_neighbor_ixs


def solve_a(s: str) -> int:
    """
    Examples:
    >> solve_a(test_string)
    31
    """
    m = np.array([[ord(c) for c in e] for e in s.splitlines()], dtype=np.int32)
    start_ix = np.where(m == ord("S"))
    end_ix = np.where(m == ord("E"))
    m[start_ix] = ord("a")
    m[end_ix] = ord("z")
    return get_minimum_path(m, (start_ix[0][0], start_ix[1][0]), (end_ix[0][0], end_ix[1][0]))


@nb.jit(nopython=True)
def get_minimum_path_nb(mat: np.ndarray, start_ix: Tuple[int, int], end_ix: Tuple[int, int]) -> int:
    ix = start_ix
    priority_queue = [(0, ix)]
    min_path_lengths = np.ones_like(mat)
    min_path_lengths = min_path_lengths * 10e9
    min_path_lengths[start_ix] = 0

    while end_ix != ix:
        for ix_ in [(ix[0] + 1, ix[1]), (ix[0] - 1, ix[1]), (ix[0], ix[1] + 1), (ix[0], ix[1] - 1)]:
            if not (0 <= ix[0] < mat.shape[0] and 0 <= ix[1] < mat.shape[1]):
                continue

            if mat[ix_[0], ix_[1]] - mat[ix[0], ix[1]] > 1:
                continue

            path_length = min_path_lengths[ix] + 1

            if min_path_lengths[ix_] <= path_length:
                continue

            min_path_lengths[ix_] = path_length
            heuristic_cost = abs(end_ix[0] - ix_[0]) + abs(end_ix[1] - ix_[1])
            heappush(priority_queue, (path_length + heuristic_cost, ix_))

        if priority_queue:
            _, ix = heappop(priority_queue)
        else:
            break

    if end_ix != ix:
        return np.inf

    return min_path_lengths[ix]


def get_minimum_path(mat: np.ndarray, start_ix: Tuple[int, int], end_ix: Tuple[int, int]) -> int:
    ix = start_ix
    priority_queue = []
    min_path_lengths = {(start_ix[0], start_ix[1]): 0}

    while end_ix != ix:
        for ix_ in get_valid_neighbor_ixs(ix, mat.shape):
            if ord(mat[ix_[0], ix_[1]]) - ord(mat[ix[0], ix[1]]) > 1:
                continue
            path_length = min_path_lengths[ix] + 1
            if ix_ in min_path_lengths and min_path_lengths[ix_] <= path_length:
                continue
            min_path_lengths[ix_] = path_length
            heuristic_cost = np.abs(end_ix[0] - ix_[0]) + np.abs(end_ix[1] - ix_[1])
            heappush(priority_queue, (path_length + heuristic_cost, ix_))

        if priority_queue:
            _, ix = heappop(priority_queue)
        else:
            break

    if end_ix != ix:
        return np.inf

    return min_path_lengths[ix]


def print_path_lengths(mat: np.ndarray, best_cost: dict):
    t = np.empty(mat.shape, dtype=int)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if (i, j) in best_cost:
                t[i, j] = best_cost[(i, j)]
            else:
                t[i, j] = np.inf
    np.set_printoptions(linewidth=400, infstr=".")
    print(t)


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    29
    """
    m = np.array([list(e) for e in s.splitlines()], dtype=str)
    start_ix = np.where(m == "S")
    end_ix = np.where(m == "E")
    m[start_ix] = "a"
    m[end_ix] = "z"
    start_pos_x, start_pos_y = np.where(m == "a")
    return min(get_minimum_path(m, (x, y), (end_ix[0][0], end_ix[1][0])) for x, y in zip(start_pos_x, start_pos_y))


test_string = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip("\n")


# %%
# from advent_tools import get_puzzle_input

# solve_a(test_string)
# # solve_a(get_puzzle_input(2022, 12).strip("\n"))
# # solve_b(test_string)
# # solve_b(get_puzzle_input(2022, 12).strip("\n"))
# # %%
# m = np.arange(25).reshape(5, 5)
# m[1, 1] = 100
# m[3, 3] = -1

# # %%
# # - Resizable
# # - Smart insertion
# priority_queue_costs = np.array([0], dtype=np.int64)
# priority_queue_ixs = np.array([[0, 0]], dtype=np.int64)

# def priority_queue_push(pq_costs, pq_ixs, cost, ix):
#     pq_costs = np.append(pq_costs, cost)
#     pq_ixs = np.append(pq_ixs, ix, axis=1)
#     ix = pq_costs.size - 1
#     while ix > 0:
#         parent_ix = (ix - 1) // 2
#         if pq_costs[parent_ix] > pq_costs[ix]:
#             pq_costs[parent_ix], pq_costs[ix] = pq_costs[ix], pq_costs[parent_ix]
#             pq_ixs[parent_ix], pq_ixs[ix] = pq_ixs[ix], pq_ixs[parent_ix]
#             ix = parent_ix
#         else:
#             break
#     return pq_costs, pq_ixs

# priority_queue_push(priority_queue_costs, priority_queue_ixs, 1, (0, 1))
