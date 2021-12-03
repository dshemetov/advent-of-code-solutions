from dataclasses import dataclass, field
from typing import List, Set

from advent_tools import Puzzle

@dataclass
class ListSet:
    values: List[int]
    unique_values: Set[int] = field(default_factory=set)

    def __post_init__(self):
        self.values = self.values.copy()
        self.unique_values = set(self.values)

    def append(self, value: int):
        self.unique_values |= {value}
        self.values.append(value)
        return self

class GameState:
    def __init__(self, values: List[int]):
        values = values.copy()
        self.current_value = values.pop()
        self.listset = ListSet(values)

    def advance_game(self, n: int = 1):
        if n < 1:
            raise ValueError("n must be 1 or larger.")
        for i in range(n):
            next_number = GameState.get_next_number(self.current_value, self.listset)
            self.listset.append(self.current_value)
            self.current_value = next_number

    def get_nth_spoken_number(self, n: int) -> int:
        if n <= len(self.listset.values):
            return self.listset.values[n-1]
        elif n == len(self.listset.values) + 1:
            return self.current_value
        else:
            self.advance_game(n - (len(self.listset.values) + 1))
            return self.current_value

    @classmethod
    def get_next_number(self, current_value: int, listset: ListSet) -> int:
        return GameState.find_number_age(current_value, listset.values) if current_value in listset.unique_values else 0

    @classmethod
    def find_number_age(self, value: int, l: list) -> int:
        for i, v in enumerate(reversed(l), start=1):
            if v == value:
                return i
        raise ValueError("Number not in list.")

class Solution:
    @property
    def answer(self) -> int:
        puzzle_input = [int(x) for x in Puzzle(15, 2020).input_data.strip("\n").split(",")]
        return GameState(puzzle_input).get_nth_spoken_number(2020)
