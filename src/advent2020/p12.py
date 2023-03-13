import re
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
from numpy.linalg import matrix_power, norm

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


def solve_a(s: str) -> Tuple[np.ndarray, np.ndarray]:
    commands = parse_commands(s)
    state = (origin, -west)

    for command in commands:
        state = execute_command_a(state, command)

    return int(norm(state[0], ord=1))


def parse_commands(s: str) -> List[Tuple[str, str]]:
    return re.findall(r"(.)(\d+)", s)


def execute_command_a(state: Tuple[np.ndarray, np.ndarray], command: Tuple[str, str]) -> np.ndarray:
    pos, directory = state
    instruction, num = command
    if instruction == "F":
        return (pos + int(num) * directory, directory)
    if instruction == "N":
        return (pos + int(num) * north, directory)
    if instruction == "S":
        return (pos - int(num) * north, directory)
    if instruction == "W":
        return (pos + int(num) * west, directory)
    if instruction == "E":
        return (pos - int(num) * west, directory)
    if instruction == "R":
        return (pos, np.linalg.matrix_power(turn_right, int(num) // 90) @ directory)
    if instruction == "L":
        return (pos, np.linalg.matrix_power(-turn_right, int(num) // 90) @ directory)


def solve_b(s: str) -> int:
    commands = parse_commands(s)
    state = State(origin, 10 * east + north)

    for command in commands:
        state = execute_command_b(state, command)

    return int(norm(state.ship_pos, ord=1))


def execute_command_b(state: State, command: Tuple[str, str]) -> np.ndarray:
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
