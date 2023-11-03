"""23. Amphipod https://adventofcode.com/2021/day/23

Lessons learned:

- This is one of those puzzles where the first part can be solved by hand and,
  indeed, it leads to a solution for the second part.
- The rules are setup so that the search space is actually much smaller than it
  appears. The main constraint is that each amphipod's will have at most 2
  steps: one to the hallways and one to its destination room.
- This is my problem for part A:

cost = 0
#############
#...........#
###C#C#A#B###
  #D#D#B#A#
  #########

cost += 7A + 2B + 9A + 5B + 6C + 5C
#############
#AA.B.....B.#
###.#.#C#.###
  #D#D#C#.#
  #########

cost += 8D + 3B + 6B + 9D + 3A + 3A
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

- For part B, we need to use our knowledge above to write an algorithm. We can
  think of the hallway as 7 registers and then 2 x 4 registers for the rooms:

#############
#12.3.4.5.67#
###A#B#C#D###
  #A#B#C#D#
  #########
"""

from collections import defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from heapq import heappop, heappush

from advent.tools import get_puzzle_input

EXAMPLE = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(EXAMPLE)
    """
    end_goal = """
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
"""
    board = from_string(s)
    pqueue = [(get_board_value(board), board)]
    memo = {str(board): get_board_value(board)}
    j = 0
    while pqueue:
        j += 1
        # sleep(0.01)  # Prevent computer from overheating.
        _, board = heappop(pqueue)
        if j % 2000 == 0:
            print(j)
            print(board)
        if to_string(board) == end_goal:
            print(board)
            print(board.cost)
            break
        for i, loc_to in board.get_valid_moves():
            board_ = make_move(board, i, loc_to)
            cost_ = get_board_value(board_)
            if str(board_) in memo and memo[str(board_)] <= cost_:
                continue
            heappush(pqueue, (cost_, board_))
            memo[str(board_)] = cost_

    if s == get_puzzle_input(2021, 23):
        # Solved manually.
        a, b, c, d = 1, 10, 100, 1000
        ans = (
            7 * a
            + 2 * b
            + 9 * a
            + 5 * b
            + 6 * c
            + 5 * c
            + 8 * d
            + 3 * b
            + 6 * b
            + 9 * d
            + 3 * a
            + 3 * a
        )
        assert ans == board.cost

    return board.cost


def solve_b(s: str) -> int:
    return 0


@dataclass
class BoardState:
    """State of the board.

    We store a list of amphipods, where each amphipod is represented by a tuple
    of (amphipod_type, location_type, index, has_moved), where amphipod_type is
    either "A", "B", "C", or "D", location_type is either "Room" or "Hallway",
    the index is the numbered position (hallways are numbered from 0 to 10, left
    to right, and the rooms are numbered from 0 to 7, typewriter order), and
    has_moved is a boolean indicating whether the amphipod has moved.

    The cost is the number of steps taken so far.

    Hallway indexes corresponding to each room:

        Room        1 2 3 4 5 6 7 8 H index     2 4 6 8 2 4 6 8
    """

    amphipods: list[list[str, str, int, bool]]
    cost: int = 0
    moves: list[tuple[int, tuple[str, int]]] = field(default_factory=list)

    def __repr__(self):
        return to_string(self)

    def get_valid_moves(self) -> list[tuple[int, tuple[str, int]]]:
        moves = []
        for i, amphipod in enumerate(self.amphipods):
            for move in get_valid_moves(self, amphipod):
                moves += [(i, move)]
        return moves

    def __lt__(self, other: "BoardState"):
        return self.cost < other.cost or self.amphipods < other.amphipods


def make_move(b: BoardState, i: int, loc_to: tuple[str, int]) -> BoardState:
    loc_from = b.amphipods[i][1:3]
    amphipod_type = b.amphipods[i][0]
    new_b = BoardState(b.amphipods.copy(), b.cost)
    new_b.amphipods[i] = (amphipod_type, loc_to[0], loc_to[1], True)
    new_b.cost += get_move_cost(loc_from, loc_to) * 10 ** (
        ord(amphipod_type) - ord("A")
    )
    new_b.moves.append((loc_from, loc_to))
    return new_b


@lru_cache(maxsize=None)
def get_move_cost(loc_from: tuple[str, int], loc_to: tuple[str, int]) -> int:
    """
    Examples:
    >>> [get_move_cost(("Room", 0), ("Hallway", i)) for i in range(11)] == [3,2,1,2,3,4,5,6,7,8,9]
    True
    >>> [get_move_cost(("Room", 4), ("Hallway", i)) for i in range(11)] == [4,3,2,3,4,5,6,7,8,9,10]
    True
    >>> [get_move_cost(("Room", 0), ("Room", i)) for i in range(8)] == [0, 4, 6, 8, 1, 5, 7, 9]
    True
    >>> [get_move_cost(("Room", 4), ("Room", i)) for i in range(8)] == [1, 5, 7, 9, 0, 6, 8, 10]
    True
    """
    if loc_from[0] == "Hallway" and loc_to[0] == "Hallway":
        raise ValueError("Cannot move from hallway to hallway.")
    if {loc_from[0], loc_to[0]} == {"Room", "Hallway"}:
        loc_room, loc_hallway = (
            (loc_from, loc_to) if loc_from[0] == "Room" else (loc_to, loc_from)
        )

        return abs(loc_hallway[1] - 2 * (loc_room[1] % 4 + 1)) + 1 + (loc_room[1] > 3)
    if (loc_from[0], loc_to[0]) == ("Room", "Room"):
        return (loc_from[1] + 4 == loc_to[1] or loc_from[1] == loc_to[1] + 4) + (
            (loc_from[1] % 4) != (loc_to[1] % 4)
        ) * (
            2 * abs((loc_from[1] % 4) - (loc_to[1] % 4))
            + 2
            + (loc_from[1] > 3)
            + (loc_to[1] > 3)
        )


def from_string(s: str) -> BoardState:
    lines = s.strip().splitlines()
    amphipods_data = lines[2][3:11:2] + lines[3][3:11:2]
    return BoardState(
        amphipods=[(a, "Room", i, False) for i, a in enumerate(amphipods_data)]
    )


def to_string(b: BoardState) -> str:
    hallway_str = list("...........")
    room_str1 = list(".#.#.#.")
    room_str2 = list(".#.#.#.")

    for a, l, i, _ in b.amphipods:
        if l == "Room":
            if i < 4:
                room_str1[i * 2] = a
            else:
                room_str2[(i - 4) * 2] = a
        else:
            hallway_str[i] = a

    room_str1 = "".join(room_str1)
    room_str2 = "".join(room_str2)
    hallway_str = "".join(hallway_str)

    return f"""
#############
#{hallway_str}#
###{room_str1}###
  #{room_str2}#
  #########
"""


def get_path(
    loc_from: tuple[str, int], loc_to: tuple[str, int], include_from: bool = False
) -> list[tuple[str, int]]:
    path = []
    if loc_from[0] == "Hallway" and loc_to[0] == "Hallway":
        raise ValueError("Cannot move from hallway to hallway.")
    elif {loc_from[0], loc_to[0]} == {"Hallway", "Room"}:
        loc_room, loc_hallway = (
            (loc_from, loc_to) if loc_from[0] == "Room" else (loc_to, loc_from)
        )
        room_hallway_index = 2 * (loc_room[1] % 4 + 1)
        if include_from:
            path.append(loc_from)
        if loc_hallway[1] > room_hallway_index:
            for i in range(room_hallway_index, loc_hallway[1]):
                path.append(("Hallway", i))
        elif loc_hallway[1] < room_hallway_index:
            for i in range(room_hallway_index, loc_hallway[1], -1):
                path.append(("Hallway", i))
        if loc_room[1] > 3:
            path.append(("Room", loc_room[1] - 4))
        path.append(loc_to)
    elif (loc_from[0], loc_to[0]) == ("Room", "Room"):
        if include_from:
            path.append(loc_from)
        if loc_from[1] > 3:
            path.append(("Room", loc_from[1] - 4))
        room_to_hallway_index = 2 * (loc_to[1] % 4 + 1)
        room_from_hallway_index = 2 * (loc_from[1] % 4 + 1)
        if room_to_hallway_index > room_from_hallway_index:
            for i in range(room_from_hallway_index, room_to_hallway_index + 1):
                path.append(("Hallway", i))
        elif room_to_hallway_index < room_from_hallway_index:
            for i in range(room_from_hallway_index, room_to_hallway_index - 1, -1):
                path.append(("Hallway", i))
        if loc_to[1] > 3:
            path.append(("Room", loc_to[1] - 4))
        path.append(loc_to)

    return path


def draw_path(b: BoardState, path: list[tuple[str, int]]) -> str:
    hallway_str = list("...........")
    room_str1 = list(".#.#.#.")
    room_str2 = list(".#.#.#.")

    for loc in path[:-1]:
        if loc[0] == "Room":
            if loc[1] < 4:
                room_str1[loc[1] * 2] = "*"
            else:
                room_str2[(loc[1] - 4) * 2] = "*"
        else:
            hallway_str[loc[1]] = "*"

    loc = path[-1]
    if loc[0] == "Room":
        if loc[1] < 4:
            room_str1[loc[1] * 2] = "!"
        else:
            room_str2[(loc[1] - 4) * 2] = "!"
    else:
        hallway_str[loc[1]] = "!"

    room_str1 = "".join(room_str1)
    room_str2 = "".join(room_str2)
    hallway_str = "".join(hallway_str)

    path_str = f"""
#############
#{hallway_str}#
###{room_str1}###
  #{room_str2}#
  #########
"""

    return merge_drawings(str(b), path_str)


def merge_drawings(s1: str, s2: str) -> str:
    lines1 = s1.strip().splitlines()
    lines2 = s2.strip().splitlines()
    lines = []
    for l1, l2 in zip(lines1, lines2):
        line = []
        for c1, c2 in zip(l1, l2):
            if c1 in {"A", "B", "C", "D"}:
                line.append(c1)
            else:
                line.append(c2)
        lines.append("".join(line))
    return "\n".join(lines)


def check_valid_move(
    b: BoardState, loc_from: tuple[str, int], loc_to: tuple[str, int]
) -> bool:
    if loc_to == loc_from:
        return False
    if loc_from[0] == "Hallway" and loc_to[0] == "Hallway":
        return False
    for amphipod in b.amphipods:
        if amphipod[1:3] == loc_to:
            return False

        path = get_path(loc_from, loc_to)
        if path is not None:
            for loc in path:
                for amphipod in b.amphipods:
                    if amphipod[1:3] == loc:
                        return False
    return True


def get_valid_moves(
    b: BoardState, amphipod: tuple[str, str, int, bool]
) -> list[tuple[str, int]]:
    if amphipod[3] and amphipod[1] == "Room":
        return []
    if amphipod[1] == "Hallway":
        all_moves = [
            ("Room", ord(amphipod[0]) - ord("A")),
            ("Room", ord(amphipod[0]) - ord("A") + 4),
        ]
    else:
        all_moves = [
            ("Room", ord(amphipod[0]) - ord("A")),
            ("Room", ord(amphipod[0]) - ord("A") + 4),
        ]
        for i in [0, 1, 3, 5, 7, 9, 10]:
            all_moves.append(("Hallway", i))
    return list(
        filter(lambda move: check_valid_move(b, amphipod[1:3], move), all_moves)
    )


def get_heuristic_cost_2(b: BoardState) -> int:
    heuristic_costs = defaultdict(list)
    for amphipod in b.amphipods:
        top_room = ("Room", ord(amphipod[0]) - ord("A"))
        bottom_room = ("Room", ord(amphipod[0]) - ord("A") + 4)
        heuristic_costs[amphipod[0]].append(
            (
                get_move_cost(amphipod[1:3], top_room),
                get_move_cost(amphipod[1:3], bottom_room),
            )
        )
    heuristic_cost = 0
    for k in heuristic_costs:
        heuristic_cost += min(
            heuristic_costs[k][0][0] + heuristic_costs[k][1][1],
            heuristic_costs[k][0][1] + heuristic_costs[k][1][0],
        ) * 10 ** (ord(k) - ord("A"))
    return heuristic_cost


def get_board_value(b: BoardState) -> int:
    return b.cost + get_heuristic_cost_2(b)
