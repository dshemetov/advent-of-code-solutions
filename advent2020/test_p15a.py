import pytest
from .p15a import ListSet, GameState

class TestListSet:
    def test_constructor(self):
        l = [1, 2, 3, 2, 4]
        ls = ListSet(l)
        assert ls.values == l
        assert ls.unique_values == set(l)

    def test_append(self):
        l = [1, 2, 3, 2, 4]
        ls = ListSet(l)
        ls.append(0)
        assert ls.values == l + [0]
        assert ls.unique_values == set(l + [0])

class TestGameState:
    def test_find_number_age(self):
        assert GameState.find_number_age(1, [1, 2, 3, 4]) == 4
        assert GameState.find_number_age(2, [1, 2, 3, 4]) == 3
        assert GameState.find_number_age(3, [1, 2, 3, 4]) == 2
        assert GameState.find_number_age(2, [2, 4, 0, 5]) == 4
        assert GameState.find_number_age(4, [2, 4, 0, 5]) == 3
        assert GameState.find_number_age(0, [2, 4, 0, 5]) == 2

    def test_get_next_number(self):
        ls = ListSet([0, 3])
        assert GameState.get_next_number(6, ls) == 0
        ls = ListSet([0, 3, 6])
        assert GameState.get_next_number(0, ls) == 3
        ls = ListSet([0, 3, 6, 0])
        assert GameState.get_next_number(3, ls) == 3
        ls = ListSet([0, 3, 6, 0, 3])
        assert GameState.get_next_number(3, ls) == 1
        ls = ListSet([0, 3, 6, 0, 3, 3])
        assert GameState.get_next_number(1, ls) == 0

    def test_advance_game(self):
        gs = GameState([0, 3, 6])
        gs.advance_game(1)
        assert gs.listset.values == GameState([0, 3, 6, 0]).listset.values
        gs.advance_game(3)
        assert gs.listset.values == GameState([0, 3, 6, 0, 3, 3, 1]).listset.values

    def test_get_nth_spoken_number(self):
        ls = GameState([0, 3, 6])
        assert ls.get_nth_spoken_number(2) == 3
        assert ls.get_nth_spoken_number(6) == 3
        assert ls.get_nth_spoken_number(7) == 1
        assert ls.get_nth_spoken_number(2020) == 436
        assert GameState([1, 3, 2]).get_nth_spoken_number(2020) == 1
        assert GameState([2, 1, 3]).get_nth_spoken_number(2020) == 10
        assert GameState([1, 2, 3]).get_nth_spoken_number(2020) == 27
        assert GameState([2, 3, 1]).get_nth_spoken_number(2020) == 78
        assert GameState([3, 2, 1]).get_nth_spoken_number(2020) == 438
        assert GameState([3, 1, 2]).get_nth_spoken_number(2020) == 1836
