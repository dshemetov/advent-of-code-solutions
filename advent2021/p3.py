from copy import copy
from typing import List
from advent_tools import Puzzle

def binary_to_num(ls: List[int]) -> int:
    return sum(2**i * j for i, j in enumerate(reversed(ls)))

def majority_bit(ls: List[int]) -> int:
    return 1 if sum(ls) >= (len(ls) / 2) else 0

def minority_bit(ls: List[int]) -> int:
    return 0 if sum(ls) >= (len(ls) / 2) else 1

def extract_column(mat: List[List[int]], col_ix: int) -> int:
    return [mat[row_ix][col_ix] for row_ix in range(len(mat))]

def filter_rows(mat: List[List[int]], ix: int, val: int) -> List[List[int]]:
    new_list = [row for row in mat if row[ix] == val]
    return new_list

def solve_a(s: str) -> int:
    mat = [list(line) for line in s.split("\n")]
    n, m = len(mat), len(mat[0])
    mat = [[int(mat[i][j]) for j in range(m)] for i in range(n)]

    max_rows = [majority_bit(extract_column(mat, ix)) for ix in range(m)]
    min_rows = [0 if bit == 1 else 1 for bit in max_rows]

    gamma_rate, epsilon_rate = binary_to_num(max_rows), binary_to_num(min_rows)
    return gamma_rate * epsilon_rate

def solve_b(s: str) -> int:
    mat = [list(line) for line in s.split("\n")]
    n, m = len(mat), len(mat[0])
    mat = [[int(mat[i][j]) for j in range(m)] for i in range(n)]

    filtered_mat = copy(mat)
    for ix in range(m):
        if len(filtered_mat) == 1:
            break

        maj_bit = majority_bit(extract_column(filtered_mat, ix))
        filtered_mat = filter_rows(filtered_mat, ix, maj_bit)
    oxygen_rating = binary_to_num(filtered_mat[0])

    filtered_mat = copy(mat)
    for ix in range(m):
        if len(filtered_mat) == 1:
            break

        min_bit = minority_bit(extract_column(filtered_mat, ix))
        filtered_mat = filter_rows(filtered_mat, ix, min_bit)
    co2_rating = binary_to_num(filtered_mat[0])

    return oxygen_rating * co2_rating


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(3, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(3, 2021).input_data)