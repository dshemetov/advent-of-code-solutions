from advent_tools import Puzzle

import numpy as np
from numpy.linalg import norm, matrix_power
from typing import Tuple, List
import re
from dataclasses import dataclass

origin = np.array([0, 0])
north, west = np.array([0, 1]), np.array([-1, 0])
south, east = -north, -west
turn_right = np.array([[0, 1], [-1, 0]])

@dataclass
class State:
    ship_pos: np.ndarray
    waypoint_pos: np.ndarray

    def __eq__(self, other):
        if isinstance(other, State):
            return np.allclose(self.ship_pos, other.ship_pos) and np.allclose(self.waypoint_pos, other.waypoint_pos)
        else:
            return False

def parse_commands(s: str) -> List[Tuple[str, str]]:
    return re.findall("(.)(\d+)", s)

def execute_command(state: State, command: Tuple[str, str]) -> np.ndarray:
    s_pos, w_pos = state.ship_pos, state.waypoint_pos
    instruction, num = command
    if instruction == "F":
        return State(s_pos + int(num) * w_pos, w_pos)
    if instruction == "N":
        return State(s_pos, w_pos + int(num) * north)
    if instruction == "S":
        return State(s_pos, w_pos + int(num) * south)
    if instruction == "W":
        return State(s_pos, w_pos + int(num) * west)
    if instruction == "E":
        return State(s_pos, w_pos + int(num) * east)
    if instruction == "R":
        return State(s_pos, matrix_power(turn_right, int(num) // 90) @ w_pos)
    if instruction == "L":
        return State(s_pos, matrix_power(-turn_right, int(num) // 90) @ w_pos)

def execute_commands(state: State, commands: List[Tuple[str, str]]) -> State:
    for command in commands:
        state = execute_command(state, command)
    return state

class Solution:
    @property
    def answer(self) -> int:
        input_string = parse_commands(Puzzle(12, 2020).input_data)
        final_state = execute_commands(State(origin, 10 * east + north), input_string)
        return int(norm(final_state.ship_pos, ord=1))
