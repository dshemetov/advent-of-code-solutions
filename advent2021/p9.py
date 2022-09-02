"""Smoke Basin https://adventofcode.com/2021/day/9"""
from advent_tools import get_top_n, get_valid_neighbor_ixs, get_neighbor_values
from itertools import product
import numpy as np
from typing import List, Set, Tuple


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    15
    """
    mat = np.array([list(x) for x in s.split("\n")], dtype=int)
    n, m = mat.shape
    return sum(mat[i, j] + 1 for i, j in product(range(n), range(m)) if is_lowest_point(np.array([i, j]), mat))


def is_lowest_point(ix: np.ndarray, mat: List[List[int]]) -> bool:
    return all(mat[tuple(ix)] < v for v in get_neighbor_values(ix, mat))


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    1134
    """
    mat = np.array([list(x) for x in s.split("\n")], dtype=int)
    a, b, c = get_top_n((len(basin) for basin in get_basins(mat)), 3)
    return a * b * c


def get_basins(mat: np.ndarray) -> List[Set[Tuple[Tuple[int, int], ...]]]:
    basins = set()
    explored = set()
    possible_locations = (ix for ix in np.ndindex(mat.shape) if mat[ix] != 9)
    for ix in possible_locations:
        if ix not in explored:
            basin = get_basin_at_index(ix, mat)
            basins |= {tuple(basin)}
            explored |= basin
    return basins


def get_basin_at_index(ix: Tuple[int, int], mat: np.ndarray) -> Set[Tuple[int, int]]:
    explored_ixs = set()
    unexplored_ixs = set({ix})
    while len(unexplored_ixs) > 0:
        ix_ = unexplored_ixs.pop()
        explored_ixs |= {ix_}
        neighbor_ixs_vals = zip(get_valid_neighbor_ixs(ix_, mat.shape), get_neighbor_values(ix_, mat))
        unexplored_ixs |= {x for x, val in neighbor_ixs_vals if val != 9} - explored_ixs
    return explored_ixs


test_string = """2199943210
3987894921
9856789892
8767896789
9899965678"""
