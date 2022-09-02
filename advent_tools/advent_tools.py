from bisect import insort
from functools import reduce
from itertools import product
import os
from typing import Any, Callable, Dict, Iterable, List, Tuple
from numpy.typing import ArrayLike

from dotenv import load_dotenv
from joblib import Memory
import requests
import numpy as np

memory = Memory(".joblib_cache", verbose=0)
try:
    load_dotenv()
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
    """Repeatedly compose a function until the output does not change; return the list of intermediate values.

    Assumes func has a single non-keyword argument.
    """

    def new_func(*args, **kwargs):
        new_val, old_val = func(*args, **kwargs), object()
        vals = [new_val]
        while new_val != old_val:
            new_val, old_val = func(new_val, **kwargs), new_val
            vals.append(new_val)
        return new_val, vals

    return new_func


def binary_to_int(ls: List[int]) -> int:
    """Convert a list of 0's and 1's to an integer.

    Examples:
    >>> binary_to_int([1, 0, 1])
    5
    """
    return sum(2**i * j for i, j in enumerate(reversed(ls)))


def reverse_dict(d: dict) -> dict:
    """This thing better be a bijection.

    Examples:
    >>> reverse_dict({'a': 2, 'b': 3})
    {2: 'a', 3: 'b'}
    """
    return {value: key for key, value in d.items()}


def get_gcd(a: int, b: int) -> int:
    """Euclidean algorithm greatest common divisor.

    Returns the largest integer d such that d | a and d | b.

    Examples:
    >>> get_gcd(6, 4)
    2
    >>> get_gcd(4, 6)
    2
    >>> get_gcd(5, 17)
    1
    """
    r, r_ = a, b
    while r_ > 0:
        r, r_ = r_, r % r_
    return r


def get_bezout_coefficients(a: int, b: int) -> int:
    """Extended Euclidean algorithm.

    Returns integer coefficients x and y such that x * a + y * b = gcd(a, b).

    Examples:
    >>> get_bezout_coefficients(6, 4)
    (1, -1)
    >>> get_bezout_coefficients(4, 6)
    (-1, 1)
    >>> get_bezout_coefficients(5, 17)
    (7, -2)
    """
    s, s_ = 0, 1
    t, t_ = 1, 0
    r, r_ = a, b
    while r_ > 0:
        q = r // r_
        r, r_ = r_, r - q * r_
        s, s_ = s_, s - q * s_
        t, t_ = t_, t - q * t_
    return (t, s)


def get_units(n: int) -> np.ndarray:
    return np.concatenate([np.eye(n, dtype=int), -np.eye(n, dtype=int)])


def get_units_and_diagonals(n: int) -> np.ndarray:
    """
    Examples:
    >>> get_units_and_diagonals(2)
    array([[-1, -1],
           [-1,  0],
           [-1,  1],
           [ 0, -1],
           [ 0,  1],
           [ 1, -1],
           [ 1,  0],
           [ 1,  1]])
    """
    zeros = tuple([0] * n)
    return np.array([tup for tup in product([-1, 0, 1], repeat=n) if tup != zeros])


def get_neighbor_values(ix: ArrayLike, mat: np.ndarray, radius: int = 1, diagonals: bool = False) -> Iterable:
    return (mat[new_ix] for new_ix in get_valid_neighbor_ixs(ix, mat.shape, radius, diagonals))


def get_valid_neighbor_ixs(ix: ArrayLike, mat_shape: ArrayLike, radius: int = 1, diagonals: bool = False) -> Iterable[Tuple[int, ...]]:
    """
    Examples:
    >>> list(get_valid_neighbor_ixs(np.array([0, 1]), np.array([2, 2])))
    [(1, 1), (0, 0)]
    """
    if diagonals:
        directions = get_units_and_diagonals(len(ix))
    else:
        directions = get_units(len(ix))

    if isinstance(ix, tuple):
        ix = np.array(ix, dtype=int)
    if isinstance(mat_shape, tuple):
        mat_shape = np.array(mat_shape, dtype=int)

    min_ix = np.zeros(len(ix), dtype=int)
    return (tuple(r * new_ix) for new_ix in (ix + directions) for r in range(1, radius + 1) if all((min_ix <= (r * new_ix)) & ((r * new_ix) < mat_shape)))


def compose_multivar_2(f: Callable, g: Callable) -> Callable:
    """
    Examples:
    >>> def f(x, y):
    ...     return x + y, x - y
    >>> compose_multivar_2(f, f)(1, 1)
    (2, 2)
    """
    return lambda *a, **kw: f(*g(*a, **kw))


def compose_multivar(*fs: List[Callable]) -> Callable:
    """
    Examples:
    >>> def f(x, y):
    ...     return x + y, x - y
    >>> compose_multivar(*[f] * 3)(1, 1)
    (4, 0)
    """
    return reduce(compose_multivar_2, fs)


def insert_finite_sorted_list(l: list, v: Any, max_length: int):
    """Insert into a sorted finite list, dropping the smallest lowest values."""
    insort(l, v)
    if len(l) > max_length:
        l.pop(0)


def get_top_n(it: Iterable, n: int) -> List:
    top_n = []
    for e in it:
        insert_finite_sorted_list(top_n, e, n)
    return top_n
