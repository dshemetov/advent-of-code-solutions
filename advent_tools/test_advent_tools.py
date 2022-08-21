from advent_tools import FiniteSortedList


def test_FiniteSortedList():
    t = FiniteSortedList([5, 4, 3], 5)
    t.insert(10)
    t.insert(2)
    t.insert(5)
    assert t.lst == [3, 4, 5, 5, 10]
