from advent_tools import Puzzle

from typing import Tuple, List

def parse_input(s: str) -> Tuple[int, List]:
    depart_time, bus_schedule = s.split("\n")
    depart_time = int(depart_time)
    bus_schedule = filter(lambda x: x != "x", bus_schedule.split(","))
    return depart_time, bus_schedule

def get_next_multiple(i: int, n: int) -> int:
    return i + n - i % n

class Solution:
    @property
    def answer(self) -> int:
        depart_time, bus_schedule = parse_input(Puzzle(13, 2020).input_data)
        bus_id, next_bus_time = min([(int(bus_id), get_next_multiple(depart_time, int(bus_id))) for bus_id in bus_schedule], key=lambda x: x[1])
        return bus_id * (next_bus_time - depart_time)
