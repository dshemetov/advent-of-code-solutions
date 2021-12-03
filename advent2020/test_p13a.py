import pytest
from .p13a import parse_input, get_next_multiple

test_string = """939
7,13,x,x,59,x,31,19"""

class Test13a:
    def test_get_next_multiple(self):
        assert get_next_multiple(15, 7) == 21
        assert get_next_multiple(36, 11) == 44

    def test_problem(self):
        depart_time, bus_schedule = parse_input(test_string)
        bus_id, next_bus_time = min([(int(bus_id), get_next_multiple(depart_time, int(bus_id))) for bus_id in bus_schedule], key=lambda x: x[1])
        assert bus_id * (next_bus_time - depart_time) == 295
