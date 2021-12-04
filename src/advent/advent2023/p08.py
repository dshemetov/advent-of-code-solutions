"""8. Haunted Wasteland https://adventofcode.com/2023/day/8"""

import re
from itertools import chain, cycle, islice


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    2
    >>> solve_a(test_string2)
    6
    """
    s = s.strip("\n")
    commands, *network = s.splitlines()

    d = {}
    for node in network[1:]:
        node, *children = re.findall(r"\w+", node)
        d[node] = children

    cur_node = "AAA"
    steps = 0
    for command in cycle(commands):
        if cur_node == "ZZZ":
            return steps
        cur_node = d[cur_node][1 if command == "R" else 0]
        steps += 1

    return -1


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string3)
    6
    """
    commands, *network = s.strip("\n").splitlines()

    d = {}
    for node in network[1:]:
        node, *children = re.findall(r"\w+", node)
        d[node] = children

    state_paths = [[(x, (0, commands[0]))] for x in d if x.endswith("A")]
    visited_states = [{state_path[0]} for state_path in state_paths]
    loop_points = [False] * len(state_paths)
    for next_command in islice(cycle(enumerate(commands)), 1, None):
        for j, state_path in enumerate(state_paths):
            new_node, cur_command = state_path[-1][0], state_path[-1][1][1]
            new_state = (d[new_node][1 if cur_command == "R" else 0], next_command)
            if new_state in visited_states[j]:
                loop_points[j] = new_state
            else:
                state_path.append(new_state)
                visited_states[j] |= {new_state}
        if all(loop_points):
            break

    state_paths2 = [
        chain(state_path[: (x := state_path.index(loop_point))], cycle(state_path[x:]))
        for state_path, loop_point in zip(state_paths, loop_points)
    ]

    for i, x in enumerate(zip(*state_paths)):
        if all(y[0].endswith("Z") for y in x):
            return i

    return -1


test_string = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

test_string2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

test_string3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
