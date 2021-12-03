from advent_tools import Puzzle

from typing import Iterable, Tuple, List

def parse_input(s: str) -> List[Tuple[int, int]]:
    _, bus_schedule = s.split("\n")
    bus_schedule = enumerate(bus_schedule.split(","))
    bus_schedule = filter(lambda x: x[1] != "x", bus_schedule)
    bus_schedule = list((int(e[1]), e[0]) for e in bus_schedule)
    return bus_schedule

def get_minutes_until_next(i: int, n: int) -> int:
    if i % n == 0:
        return 0
    else:
        return n - i % n

def find_timestamp(bus_schedule: Iterable[Tuple[int, int]]) -> int:
    largest_id, largest_id_wait_time = max(bus_schedule, key=lambda x: x[0])
    t = largest_id - largest_id_wait_time
    while True:
        if all(get_minutes_until_next(t, bus_id) == wait_time for bus_id, wait_time in bus_schedule):
            break
        t += largest_id
    return t

class Solution:
    @property
    def answer(self) -> int:
        return 1

    @property
    def answer_slow(self) -> int:
        bus_schedule = parse_input(Puzzle(13, 2020).input_data)
        return find_timestamp(bus_schedule)
