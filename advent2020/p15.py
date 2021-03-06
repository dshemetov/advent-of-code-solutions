from advent_tools import Puzzle
from typing import List, Dict

class GameState:
    def __init__(self, values: List[int]):
        values = values.copy()
        self.turn_number = len(values)
        self.current_value = values.pop()
        self.last_turn = convert_list_to_last_turn_dict(values)

    def advance_game(self, n: int = 1):
        if n < 1:
            raise ValueError("n must be 1 or larger.")
        for _ in range(n):
            new_value = GameState.get_next_number(self.current_value, self.turn_number, self.last_turn)
            self.last_turn[self.current_value] = self.turn_number
            self.current_value = new_value
            self.turn_number += 1

    def get_nth_spoken_number(self, n: int) -> int:
        if n < self.turn_number:
            raise ValueError("n must be larger than the current turn number.")
        elif n == self.turn_number:
            return self.current_value
        else:
            self.advance_game(n - self.turn_number)
            return self.current_value

    @staticmethod
    def get_next_number(current_value: int, turn_number: int, last_turn: Dict[int, int]):
        return turn_number - last_turn.get(current_value, turn_number)

def convert_list_to_last_turn_dict(l: List[int]) -> Dict[int, int]:
    return dict({v: i + 1 for i, v in enumerate(l)})

def solve_a(s: str) -> int:
    puzzle_input = [int(x) for x in s.strip("\n").split(",")]
    return GameState(puzzle_input).get_nth_spoken_number(2020)

def solve_b(s: str) -> int:
    puzzle_input = [int(x) for x in s.strip("\n").split(",")]
    return GameState(puzzle_input).get_nth_spoken_number(30000000)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(15, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(15, 2020).input_data)
