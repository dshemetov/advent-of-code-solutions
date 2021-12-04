from advent_tools import Puzzle

from typing import Iterable, Tuple, List

def parse_input_a(s: str) -> Tuple[int, List]:
    depart_time, bus_schedule = s.split("\n")
    depart_time = int(depart_time)
    bus_schedule = filter(lambda x: x != "x", bus_schedule.split(","))
    return depart_time, bus_schedule

def parse_input_b(s: str) -> List[Tuple[int, int]]:
    _, bus_schedule = s.split("\n")
    bus_schedule = enumerate(bus_schedule.split(","))
    bus_schedule = filter(lambda x: x[1] != "x", bus_schedule)
    bus_schedule = list((int(e[1]), e[0]) for e in bus_schedule)
    return bus_schedule

def get_minutes_until_next_bus(i: int, n: int) -> int:
    if i % n == 0:
        return 0
    else:
        return n - i % n

def get_next_bus_time(i: int, n: int) -> int:
    return i + get_minutes_until_next_bus(i, n)

def solve_a(s: str) -> int:
    depart_time, bus_schedule = parse_input_a(s)
    bus_id, next_bus_time = min([(int(bus_id), get_next_bus_time(depart_time, int(bus_id))) for bus_id in bus_schedule], key=lambda x: x[1])
    return bus_id * (next_bus_time - depart_time)

def find_timestamp(bus_schedule: Iterable[Tuple[int, int]]) -> int:
    largest_id, largest_id_wait_time = max(bus_schedule, key=lambda x: x[0])
    t = largest_id - largest_id_wait_time
    while True:
        if all(get_minutes_until_next_bus(t, bus_id) == wait_time for bus_id, wait_time in bus_schedule):
            break
        t += largest_id
    return t

def solve_b(s: str) -> int:
    bus_schedule = parse_input_b(s)
    return find_timestamp(bus_schedule)

class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(13, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(13, 2020).input_data)