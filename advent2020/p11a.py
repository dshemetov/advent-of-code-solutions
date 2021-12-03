from advent_tools import Puzzle

import numpy as np
from typing import Tuple, Iterable, List

def string_to_array(s: str) -> np.ndarray:
    return np.array([list(x) for x in s.strip("\n").split("\n")])

def get_ix_neighborhood(mat: np.ndarray, ix: np.ndarray, diags: bool=True) -> List[np.ndarray]:
    x_max, y_max = mat.shape
    up, left = np.array([-1, 0]), np.array([0, -1])

    if diags:
        directions = [up, -up, left, -left, up + left, up - left, -up + left, -up - left]
    else:
        directions = [up, -up, left, -left]

    return [ix + x for x in directions if 0 <= (ix + x)[0] < x_max and 0 <= (ix + x)[1] < y_max]

def check_nearby_seats_empty(state: np.ndarray, ix: np.ndarray) -> bool:
    return all(state[tuple(e)] != "#" for e in get_ix_neighborhood(state, ix))

def check_nearby_seats_crowded(state: np.ndarray, ix: np.ndarray) -> bool:
    return sum(1 if state[tuple(e)] == "#" else 0 for e in get_ix_neighborhood(state, ix)) >= 4

def get_empty_seats(state: np.ndarray) -> Iterable[Tuple[int, int]]:
    return zip(*np.where(state == "L"))

def get_occupied_seats(state: np.ndarray) -> Iterable[Tuple[int, int]]:
    return zip(*np.where(state == "#"))

def find_seats_to_update(state: np.ndarray) -> np.ndarray:
    newly_occupied_seats = [ix for ix in get_empty_seats(state) if check_nearby_seats_empty(state, np.array(ix))]
    newly_vacant_seats = [ix for ix in get_occupied_seats(state) if check_nearby_seats_crowded(state, np.array(ix))]
    return newly_occupied_seats, newly_vacant_seats

def update_state(state: np.ndarray) -> np.ndarray:
    next_state = state.copy()
    newly_occupied_seats, newly_vacant_seats = find_seats_to_update(state)
    if len(newly_occupied_seats) > 0:
        for ix in newly_occupied_seats:
            next_state[ix] = "#"
    if len(newly_vacant_seats) > 0:
        for ix in newly_vacant_seats:
            next_state[ix] = "L"
    return next_state

def update_state_until_fixed(state: np.ndarray) -> np.ndarray:
    current_state = state.copy()
    next_state = state.copy()
    newly_occupied_seats, newly_vacant_seats = find_seats_to_update(current_state)
    while len(newly_vacant_seats) > 0 or len(newly_occupied_seats) > 0:
        if len(newly_occupied_seats) > 0:
            for ix in newly_occupied_seats:
                next_state[ix] = "#"
        if len(newly_vacant_seats) > 0:
            for ix in newly_vacant_seats:
                next_state[ix] = "L"
        current_state = next_state.copy()
        newly_occupied_seats, newly_vacant_seats = find_seats_to_update(current_state)
    return next_state

def count_occupied_seats(state: np.ndarray) -> int:
    return len(np.where(state == "#")[0])

class Solution:
    @property
    def answer(self) -> int:
        state = string_to_array(Puzzle(11, 2020).input_data)
        return count_occupied_seats(update_state_until_fixed(state))
