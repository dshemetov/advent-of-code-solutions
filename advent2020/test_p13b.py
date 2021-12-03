import pytest
from .p13b import parse_input, find_timestamp

test_strings = [
    """939\n7,13,x,x,59,x,31,19""",
    """1\n17,x,13,19""",
    """1\n67,7,59,61""",
    """1\n67,x,7,59,61""",
    """1\n67,7,x,59,61""",
    """1\n1789,37,47,1889"""
]

class Test13a:
    def test_parse_input(self):
        assert list(parse_input(test_strings[0])) == [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]

    def test_find_timestamp(self):
        assert find_timestamp(parse_input(test_strings[0])) == 1068781
        assert find_timestamp(parse_input(test_strings[1])) == 3417
        assert find_timestamp(parse_input(test_strings[2])) == 754018
        assert find_timestamp(parse_input(test_strings[3])) == 779210
        assert find_timestamp(parse_input(test_strings[4])) == 1261476
        assert find_timestamp(parse_input(test_strings[5])) == 1202161486
