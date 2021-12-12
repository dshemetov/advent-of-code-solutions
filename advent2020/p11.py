from advent_tools import Puzzle, get_valid_neighbor_ixs
import numpy as np
from typing import Tuple, Iterable

def solve_a(s: str) -> int:
    state = string_to_array(s)
    return count_occupied_seats(update_state_until_fixed(state, "nearby"))

def string_to_array(s: str) -> np.ndarray:
    return np.array([list(x) for x in s.strip("\n").split("\n")])

def count_occupied_seats(state: np.ndarray) -> int:
    return len(np.where(state == "#")[0])

def update_state_until_fixed(state: np.ndarray, method: str) -> np.ndarray:
    current_state = state.copy()
    next_state = state.copy()
    no_changes = False
    while no_changes is False:
        no_changes = True
        newly_occupied_seats, newly_vacant_seats = find_seats_to_update(current_state, method)
        for ix in newly_occupied_seats:
            next_state[ix] = "#"
            no_changes = False
        for ix in newly_vacant_seats:
            next_state[ix] = "L"
            no_changes = False
        current_state = next_state.copy()
    return next_state

def find_seats_to_update(state: np.ndarray, method: str) -> np.ndarray:
    if method == "nearby":
        newly_occupied_seats = ((i, j) for i, j in get_empty_seats(state) if check_nearby_seats_empty(i, j, state))
        newly_vacant_seats = ((i, j) for i, j in get_occupied_seats(state) if check_nearby_seats_crowded(i, j, state))
    if method == "visible":
        newly_occupied_seats = ((i, j) for i, j in get_empty_seats(state) if check_visible_seats_empty(i, j, state))
        newly_vacant_seats = ((i, j) for i, j in get_occupied_seats(state) if check_visible_seats_crowded(i, j, state))
    return newly_occupied_seats, newly_vacant_seats

def get_empty_seats(state: np.ndarray) -> Iterable[Tuple[int, int]]:
    return zip(*np.where(state == "L"))

def get_occupied_seats(state: np.ndarray) -> Iterable[Tuple[int, int]]:
    return zip(*np.where(state == "#"))

def check_nearby_seats_empty(i: int, j: int, state: np.ndarray) -> bool:
    for i_, j_ in get_valid_neighbor_ixs(i, j, state, diagonals=True):
        if state[(i_, j_)] == "#":
            return False
    return True

def check_nearby_seats_crowded(i: int, j: int, state: np.ndarray) -> bool:
    visible_seats = 0
    for i_, j_ in get_valid_neighbor_ixs(i, j, state, diagonals=True):
        if state[(i_, j_)] == "#":
            visible_seats += 1
        if visible_seats >= 4:
            return True
    return False

def check_visible_seats_empty(i: int, j: int, state: np.ndarray) -> bool:
    up, left = np.array([-1, 0]), np.array([0, -1])
    directions = [up, -up, left, -left, up + left, up - left, -up + left, -up - left]
    for direction in directions:
        if "#" == get_first_visible_object(i, j, direction, state):
            return False
    return True

def check_visible_seats_crowded(i: int, j: int, state: np.ndarray) -> bool:
    up, left = np.array([-1, 0]), np.array([0, -1])
    directions = [up, -up, left, -left, up + left, up - left, -up + left, -up - left]
    visible_seats = 0
    for direction in directions:
        if "#" == get_first_visible_object(i, j, direction, state):
            visible_seats += 1
        if visible_seats >= 5:
            return True
    return False

def get_first_visible_object(i: int, j: int, direction: np.ndarray, state: np.ndarray) -> str:
    x_max, y_max = state.shape
    di, dj = direction
    i_, j_ = i + di, j + dj
    while (0 <= i_ < x_max) and (0 <= j_ < y_max):
        v = state[(i_, j_)]
        if v != ".":
            return v
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
