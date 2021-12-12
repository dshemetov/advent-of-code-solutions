from advent_tools import Puzzle
import re
from typing import List, Tuple

def solve_a(s: str) -> int:
    d = dict([parse_line(line) for line in s.split("\n")])
    traversed = set()
    to_traverse = set(["shiny gold"])
    while len(to_traverse) > 0:
        entry = to_traverse.pop()
        traversed.add(entry)
        parents = get_parents(entry, d)
        to_traverse |= set(parents) - traversed
    return len(traversed) - 1

def parse_line(line: str) -> Tuple[str, str]:
    container_bag, contained_bags = re.match(r'(\w+ \w+) bags contain (.*)', line).groups()
    contained_bags = [[int(e.groups()[0]), e.groups()[1]] for e in re.finditer(r'(\d+) (\w+ \w+) bags?', contained_bags)]
    return (container_bag, contained_bags)

def get_parents(child, d):
    return [e for e in d if child in flatten(d[e])]

def flatten(lst: List[List]) -> List:
    return [e for row in lst for e in row]

def solve_b(s: str) -> int:
    d = dict([parse_line(line) for line in s.split("\n")])
    return get_bags(d, "shiny gold") - 1

def get_bags(d, e):
    n = sum(bag[0] * get_bags(d, bag[1]) for bag in d[e]) if len(d[e]) > 0 else 0
    return n + 1


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(7, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(7, 2020).input_data)
