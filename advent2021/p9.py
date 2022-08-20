from typing import List, Set, Tuple
from advent_tools import get_valid_neighbor_ixs, get_neighbor_values
from itertools import product

def solve_a(s: str) -> int:
    mat = [[int(x) for x in list(line)] for line in s.split("\n")]
    n, m = len(mat), len(mat[0])
    return sum(mat[i][j]+1 for i, j in product(range(n), range(m)) if is_lowest_point(i, j, mat))

def is_lowest_point(i: int, j: int, mat: List[List[int]]) -> bool:
    return all(mat[i][j] < v for v in get_neighbor_values(i, j, mat))

def solve_b(s: str) -> int:
    mat = [[int(x) for x in list(line)] for line in s.split("\n")]
    a, b, c = sorted([len(basin) for basin in get_basins(mat)], reverse=True)[:3]
    return a * b * c

def get_basins(mat: List[List[int]]) -> List[Set[Tuple[Tuple[int, int], ...]]]:
    basins = set()
    explored = set()
    n, m = len(mat), len(mat[0])
    possible_locations = ((i, j) for i, j in product(range(n), range(m)) if mat[i][j] != 9)
    for i, j in possible_locations:
        if (i, j) not in explored:
            basin = get_basin_at_index(i, j, mat)
            basins |= {tuple(basin)}
            explored |= basin
    return basins

def get_basin_at_index(i: int, j: int, mat: List[List[int]]) -> Set[Tuple[int, int]]:
    explored_ixs = set()
    unexplored_ixs = set({(i, j)})
    while len(unexplored_ixs - explored_ixs) > 0:
        i_, j_ = unexplored_ixs.pop()
        neighbor_ixs_vals = zip(get_valid_neighbor_ixs(i_, j_, mat), get_neighbor_values(i_, j_, mat))
        unexplored_ixs |= {x for x, val in neighbor_ixs_vals if val != 9} - explored_ixs
        explored_ixs |= {(i_, j_)}
    return explored_ixs
