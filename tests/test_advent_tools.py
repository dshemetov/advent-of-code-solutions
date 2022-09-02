from advent_tools import get_top_n


def test_FiniteSortedList():
    assert get_top_n([5, 4, 3, 10, 2, 5], 5) == [3, 4, 5, 5, 10]
