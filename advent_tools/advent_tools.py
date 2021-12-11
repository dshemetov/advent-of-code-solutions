import os
from os.path import join
from typing import Dict, List, Tuple, Union

from dotenv import load_dotenv
from joblib import Memory
import requests
import numpy as np

ADVENT_TOOLS_PATH = join(os.environ["HOME"], ".advent_tools")
memory = Memory(join(ADVENT_TOOLS_PATH, "joblib_cache"), verbose=0)
try:
    load_dotenv(dotenv_path=join(ADVENT_TOOLS_PATH, ".env"))
    AUTH = {"session": os.environ["AOC_TOKEN"]}
except KeyError:
    raise Exception(".env file with Advent of Code user cookie not found.")


class Puzzle:
    def __init__(self, day: int, year: int, auth: Dict[str, str] = AUTH):
        if year < 2015 or year > 2021:
            raise ValueError("Year outside valid range [2015, 2021].")
        if day < 1 or day > 31:
            raise ValueError("Day outside valid range [1, 31].")
        self.day = day
        self.year = year
        self.auth = auth

    @property
    def input_data(self) -> str:
        return puzzle_input(self.day, self.year, self.auth).strip("\n")

    @property
    def input_lines(self) -> List[str]:
        return self.input_data.split("\n")

@memory.cache
def puzzle_input(day: int, year: int, auth: Dict[str, str] = AUTH) -> str:
    print(f"Downloading puzzle input for day {day}, year {year}...")
    request = requests.get(url=f"https://adventofcode.com/{year}/day/{day}/input", cookies=auth)
    return request.text

def apply_until_fixed(func):
    """Repeatedly compose a function until the output does not change.

    Assumes func has a single non-keyword argument.
    """
    def new_func(*args, **kwargs):
        new_val, old_val = func(*args, **kwargs), object()
        while new_val != old_val:
            new_val, old_val = func(new_val, **kwargs), new_val
        return new_val
    return new_func

def apply_until_fixed_list(func):
    def new_func(*args, **kwargs):
        new_val, old_val = func(*args, **kwargs), object()
        vals = [new_val]
        while new_val != old_val:
            new_val, old_val = func(new_val, **kwargs), new_val
            vals.append(new_val)
        return new_val, vals
    return new_func

def reverse_dict(d: dict) -> dict:
    """This thing better be a bijection."""
    return {value: key for key, value in d.items()}

def get_gcd(a: int, b: int) -> int:
    # Euclidean algorithm
    r, r_ = a, b
    while r_ > 0:
        r, r_ = r_, r % r_
    return r

def get_bezout_coefficients(a: int, b: int) -> int:
    # Extended Euclidean algorithm
    s, s_ = 0, 1
    t, t_ = 1, 0
    r, r_ = a, b
    while r_ > 0:
        q = r // r_
        r, r_ = r_, r - q * r_
        s, s_ = s_, s - q * s_
        t, t_ = t_, t - q * t_
    return (t, s)

def get_neighbor_values(i: int, j: int, mat: Union[List[List[int]], np.ndarray], radius: int = 1, diagonals: bool = False) -> List[int]:
    return (mat[i][j] for i, j in get_valid_neighbor_ixs(i, j, mat, radius, diagonals))

def get_valid_neighbor_ixs(i: int, j: int, mat: Union[List[List[int]], np.ndarray], radius: int = 1, diagonals: bool = False) -> List[Tuple[int, int]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if diagonals:
        directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return ((i + r * di, j + r * dj) for di, dj in directions for r in range(1, radius + 1) if 0 <= i + r * di < len(mat) and 0 <= j + r * dj < len(mat[0]))
