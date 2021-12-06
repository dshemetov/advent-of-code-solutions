from advent_tools import Puzzle
from collections import Counter

def solve_a(s: str) -> int:
    fish_ages = Counter(int(x) for x in s.split(","))
    return get_number_fish_after_days(fish_ages, 80)

def get_number_fish_after_days(fish_ages: Counter, n: int) -> int:
    return sum(pass_days(fish_ages, n).values())

def pass_days(fish_ages: Counter, n: int = 1) -> Counter:
    for _ in range(n):
        fish_ages_ = fish_ages.copy()
        for key, value in fish_ages.items():
            if key == 0:
                fish_ages_[0] -= value
                fish_ages_[6] += value
                fish_ages_[8] += value
            else:
                fish_ages_[key] -= value
                fish_ages_[key-1] += value
        fish_ages = fish_ages_.copy()
    return fish_ages

def solve_b(s: str) -> int:
    fish_ages = Counter(int(x) for x in s.split(","))
    return get_number_fish_after_days(fish_ages, 256)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(6, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(6, 2021).input_data)