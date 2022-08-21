from advent_tools import Puzzle, get_valid_neighbor_ixs
from copy import deepcopy
from itertools import product
from typing import List, Tuple, Iterable


def solve_a(s: str) -> int:
    state = string_to_array(s)
    return count_occupied_seats(update_state_until_fixed(state, "nearby"))


def string_to_array(s: str) -> List[List[str]]:
    return [list(x) for x in s.strip("\n").split("\n")]


def count_occupied_seats(state: List[List[str]]) -> int:
    return sum(1 for row in state for x in row if x == "#")


def update_state_until_fixed(state: List[List[str]], method: str) -> List[List[str]]:
    current_state = deepcopy(state)
    next_state = deepcopy(state)
    no_changes = False
    while no_changes is False:
        no_changes = True
        newly_occupied_seats, newly_vacant_seats = find_seats_to_update(current_state, method)
        for i, j in newly_occupied_seats:
            next_state[i][j] = "#"
            no_changes = False
        for i, j in newly_vacant_seats:
            next_state[i][j] = "L"
            no_changes = False
        current_state = deepcopy(next_state)
    return next_state


def find_seats_to_update(state: List[List[str]], method: str) -> List[List[str]]:
    if method == "nearby":
        newly_occupied_seats = ((i, j) for i, j in get_empty_seats(state) if check_nearby_seats_empty(i, j, state))
        newly_vacant_seats = ((i, j) for i, j in get_occupied_seats(state) if check_nearby_seats_crowded(i, j, state))
    if method == "visible":
        newly_occupied_seats = ((i, j) for i, j in get_empty_seats(state) if check_visible_seats_empty(i, j, state))
        newly_vacant_seats = ((i, j) for i, j in get_occupied_seats(state) if check_visible_seats_crowded(i, j, state))
    return newly_occupied_seats, newly_vacant_seats


def get_empty_seats(state: List[List[str]]) -> Iterable[Tuple[int, int]]:
    n, m = len(state), len(state[0])
    for i, j in product(range(n), range(m)):
        if state[i][j] == "L":
            yield i, j


def get_occupied_seats(state: List[List[str]]) -> Iterable[Tuple[int, int]]:
    n, m = len(state), len(state[0])
    for i, j in product(range(n), range(m)):
        if state[i][j] == "#":
            yield i, j


def check_nearby_seats_empty(i: int, j: int, state: List[List[str]]) -> bool:
    n, m = len(state), len(state[0])
    for i_, j_ in get_valid_neighbor_ixs((i, j), (n, m), diagonals=True):
        if state[i_][j_] == "#":
            return False
    return True


def check_nearby_seats_crowded(i: int, j: int, state: List[List[str]]) -> bool:
    n, m = len(state), len(state[0])
    visible_seats = 0
    for i_, j_ in get_valid_neighbor_ixs((i, j), (n, m), diagonals=True):
        if state[i_][j_] == "#":
            visible_seats += 1
            if visible_seats >= 4:
                return True
    return False


def check_visible_seats_empty(i: int, j: int, state: List[List[str]]) -> bool:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for di, dj in directions:
        if "#" == get_first_visible_object(i, j, di, dj, state):
            return False
    return True


def check_visible_seats_crowded(i: int, j: int, state: List[List[str]]) -> bool:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visible_seats = 0
    for di, dj in directions:
        if "#" == get_first_visible_object(i, j, di, dj, state):
            visible_seats += 1
            if visible_seats >= 5:
                return True
    return False


def get_first_visible_object(i: int, j: int, di: int, dj: int, state: List[List[str]]) -> str:
    n, m = len(state), len(state[0])
    i_, j_ = i + di, j + dj
    while (0 <= i_ < n) and (0 <= j_ < m):
        v = state[i_][j_]
        if v == "#":
            return "#"
        if v == "L":
            return "L"
        i_, j_ = i_ + di, j_ + dj
    return "."


def solve_b(s: str) -> int:
    state = string_to_array(s)
    return count_occupied_seats(update_state_until_fixed(state, "visible"))


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(11, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(11, 2020).input_data)
