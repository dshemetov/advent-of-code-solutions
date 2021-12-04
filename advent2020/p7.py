import re
from typing import List, Tuple
from advent_tools import Puzzle

def parse_line(line: str) -> Tuple[str, str]:
    container_bag, contained_bags = re.match(r'(\w+ \w+) bags contain (.*)', line).groups()
    contained_bags = [[int(e.groups()[0]), e.groups()[1]] for e in re.finditer(r'(\d+) (\w+ \w+) bags?', contained_bags)]
    return (container_bag, contained_bags)

def flatten(lst: List[List]) -> List:
    return [e for row in lst for e in row]

def get_parents(child, d):
    return [e for e in d if child in flatten(d[e])]

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


# Example: regex capture groups!
line = "light salmon bags contain 5 wavy plum bags, 4 drab white bags, 5 muted bronze bags, 5 mirrored beige bags."
# \w+ matches one or more words
# the first capture group matches (light salmon)
# the second capture group grabs the rest of the string
parent, entries = re.match(r'(\w+ \w+) bags contain (.*)', line).groups()
# \d+ matches one or more integers (could be two digit integers, for example)
# The bags? is optional
print([[int(e.groups()[0]), e.groups()[1]] for e in re.finditer(r'(\d+) (\w+ \w+) bags?', entries)])



# Part b
def get_bags(d, e):
    n = sum(bag[0] * get_bags(d, bag[1]) for bag in d[e]) if len(d[e]) > 0 else 0
    return n + 1

def solve_b(s: str) -> int:
    d = dict([parse_line(line) for line in s.split("\n")])
    return get_bags(d, "shiny gold") - 1


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(7, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(7, 2020).input_data)

Solution().answer_b