from advent_tools import Puzzle

import numpy as np
from numpy.linalg import norm
from typing import Tuple, List
import re

origin = np.array([0, 0])
north, west = np.array([0, 1]), np.array([-1, 0])
turn_right = np.array([[0, 1], [-1, 0]])

def parse_commands(s: str) -> List[Tuple[str, str]]:
    m = re.findall("(.)(\d+)", s)
    return m

def execute_command(state: Tuple[np.ndarray, np.ndarray], command: Tuple[str, str]) -> np.ndarray:
    pos, dir = state
    instruction, num = command
    if instruction == "F":
        return (pos + int(num) * dir, dir)
    if instruction == "N":
        return (pos + int(num) * north, dir)
    if instruction == "S":
        return (pos - int(num) * north, dir)
    if instruction == "W":
        return (pos + int(num) * west, dir)
    if instruction == "E":
        return (pos - int(num) * west, dir)
    if instruction == "R":
        return (pos, np.linalg.matrix_power(turn_right, int(num) // 90) @ dir)
    if instruction == "L":
        return (pos, np.linalg.matrix_power(-turn_right, int(num) // 90) @ dir)

def execute_commands(state: Tuple[np.ndarray, np.ndarray], commands: List[Tuple[str, str]]) -> Tuple[np.ndarray, np.ndarray]:
    for command in commands:
        state = execute_command(state, command)
    return state

class Solution:
    @property
    def answer(self) -> int:
        input_string = parse_commands(Puzzle(12, 2020).input_data)
        final_state = execute_commands((origin, -west), input_string)
        return int(norm(final_state[0], ord=1))
