import pytest
from .p13 import parse_input_a, parse_input_b, get_next_bus_time, find_timestamp

test_strings = [
    """939\n7,13,x,x,59,x,31,19""",
    """1\n17,x,13,19""",
    """1\n67,7,59,61""",
    """1\n67,x,7,59,61""",
    """1\n67,7,x,59,61""",
    """1\n1789,37,47,1889"""
]

class Test13a:
    def test_get_next_bus_time(self):
        assert get_next_bus_time(14, 7) == 14
        assert get_next_bus_time(15, 7) == 21
        assert get_next_bus_time(36, 11) == 44

    def test_problem(self):
        depart_time, bus_schedule = parse_input_a(test_strings[0])
        bus_id, next_bus_time = min([(int(bus_id), get_next_bus_time(depart_time, int(bus_id))) for bus_id in bus_schedule], key=lambda x: x[1])
        assert bus_id * (next_bus_time - depart_time) == 295

class Test13b:
    def test_parse_input_b(self):
        assert list(parse_input_b(test_strings[0])) == [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]

    def test_find_timestamp(self):
        assert find_timestamp(parse_input_b(test_strings[0])) == 1068781
        assert find_timestamp(parse_input_b(test_strings[1])) == 3417
        assert find_timestamp(parse_input_b(test_strings[2])) == 754018
        assert find_timestamp(parse_input_b(test_strings[3])) == 779210
        assert find_timestamp(parse_input_b(test_strings[4])) == 1261476
        assert find_timestamp(parse_input_b(test_strings[5])) == 1202161486
