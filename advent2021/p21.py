import argparse
import importlib
import time
from abc import ABC, abstractmethod
from typing import List, Tuple, Set
from scipy.spatial import distance_matrix
from itertools import permutations, product, cycle, product
import numpy as np
import copy
import random as rng
import re
from collections import namedtuple, Counter

class AdventProblem(ABC):
    """
    An abstraction of an advent code problem.
    """
    def __init__(self, name: str):
        """
        :param name: a name useful for logging and debugging
        """

        self.name = name

    @abstractmethod
    def solve_part1(self) -> str:
        """
        Solve the advent problem part 1.
        """

    @abstractmethod
    def solve_part2(self) -> str:
        """
        Solve the advent problem part 2.
        """


class Die(ABC):
    def __init__(self):
        self.roll_count = 0

    def do_roll(self) -> int:
        self.roll_count += 1
        return self.get_roll()

    @abstractmethod
    def get_roll(self) -> int:

        """
        Get the value of the roll
        """


class Die6(Die):
    def __init__(self):
        super().__init__()

    def get_roll(self) -> int:
        return rng.randint(1, 6)


class DeterministicDie(Die):
    def __init__(self):
        super().__init__()
        self.num = 0

    def get_roll(self) -> int:
        self.num += 1
        if self.num > 100:
            self.num = 1
        return self.num


class Player:
    def __init__(self, num:int, location: int):
        self.num = num
        self.location = location
        self.score = 0

    def move_roll(self, die):
        rolls: List[int] = []
        for _ in range(3):
            rolls.append(die.do_roll())

        result = sum(rolls)
        new_location = ((self.location + result - 1) % 10) + 1
        self.score += new_location
        self.location = new_location

    def check_for_win(self):
        return self.score >= 1000

WorldState = namedtuple('WorldState', ['p1_loc', 'p1_score', 'p2_loc', 'p2_score'])

class Day21(AdventProblem):
    def __init__(self, test: bool):
        super().__init__('Dirac Dice')
        sensor_file = 'test.txt' if test else 'data3.txt'
        sensor_lines = open(sensor_file, 'r').read()
        (_, p1_start), (_, p2_start) = re.findall("Player (\d+) starting position: (\d+)", sensor_lines)
        self.players = [Player(1, location=int(p1_start)), Player(2, location=int(p2_start))]

    def solve_part1(self) -> str:
        die = DeterministicDie()
        players = copy.deepcopy(self.players)

        for player in cycle(players):
            player.move_roll(die)
            #print(f"player {player.num} score: {player.score}")
            if player.check_for_win():
                winner = player
                break

        loser = players[winner.num % 2]

        return f'{loser.score * die.roll_count}'

    def prune_winners(self, state_dict: Counter, winning_count: Tuple[int, int]) -> Counter:
        state_dict_copy = state_dict.copy()
        for state in state_dict:
            if state.p1_score >= 21:
                winning_count[0] += state_dict[state]
                del state_dict_copy[state]
            elif state.p2_score >= 21:
                winning_count[1] += state_dict[state]
                del state_dict_copy[state]
        return state_dict_copy

    def transition_state(self, state: WorldState, state_dict: Counter, pnum: int):
        state_dict_new = Counter()
        for state in state_dict:
            sent = state_dict[state]
            if sent == 0:
                continue

            for r1, r2, r3 in product(range(1,3+1), repeat=3):
                rsum = r1+r2+r3
                location1, score1, location2, score2 = state
                if pnum == 0:
                    location1 = (-1 + rsum + location1) % 10 + 1
                    score1 += location1
                else:
                    location2 = (-1 + rsum + location2) % 10 + 1
                    score2 += location2

                new_state = WorldState(location1, score1, location2, score2)
                state_dict_new[new_state] += sent
        return state_dict_new

    def solve_part2(self) -> str:
        p1, p2 = self.players[0], self.players[1]
        state = WorldState(p1.location, p1.score, p2.location, p2.score)
        print(f'Initial state is: {state}')
        state_dict: Counter[WorldState, int] = Counter()
        state_dict[state] = 1
        winning_count: List[int] = [0, 0]

        for turn in range(14):
            for player_turn in range(2):
                state_dict = self.transition_state(state, state_dict, player_turn)
                state_dict = self.prune_winners(state_dict, winning_count)

        return f'{max(winning_count)}'

def run_day(day: int, test: bool) -> None:
    module = importlib.import_module('main')
    class_ = getattr(module, f'Day{day}')
    time1 = time.time()
    instance: AdventProblem = class_(test)
    time2 = time.time()
    print(f'Creating the class took {time2 - time1:.4f} seconds')
    print(f'Now solving Day {day} "{instance.name}":')
    part1, time3 = instance.solve_part1(), time.time()
    print(f'Part 1 ({time3 - time2:.4f} s) - {part1}')
    part2, time4 = instance.solve_part2(), time.time()
    print(f'Part 2 ({time4 - time3:.4f} s) - {part2}')


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser("main.py")

#     parser.add_argument(dest='day', help='which day to run')
#     parser.add_argument('-t',
#                         '--test',
#                         dest='test',
#                         help='run the output on the test data',
#                         action="store_true")
#     parser.set_defaults(test=False)

#     args = parser.parse_args()

#     run_day(args.day, args.test)

run_day(21, True)