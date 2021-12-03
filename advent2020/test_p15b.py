import pytest
from .p15b import convert_list_to_last_turn, GameState

class TestCounter:
    def test_convert_list_to_last_turn(self):
        assert convert_list_to_last_turn([0, 3, 6]) == dict({0: 1, 3: 2, 6: 3})
        assert convert_list_to_last_turn([0, 3, 6, 0, 3]) == dict({0: 4, 3: 5, 6: 3})

class TestGameState:
    def test_get_next_number(self):
        gs = GameState([0, 3, 6])
        next_number = GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn)
        assert next_number == 0
        gs = GameState([0, 3, 6, 0])
        next_number = GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn)
        assert next_number == 3
        gs = GameState([0, 3, 6, 0, 3])
        next_number = GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn)
        assert next_number == 3
        gs = GameState([0, 3, 6, 0, 3, 3])
        next_number = GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn)
        assert next_number == 1
        gs = GameState([0, 3, 6, 0, 3, 3, 1])
        next_number = GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn)
        assert next_number == 0

    def test_advance_game(self):
        gs = GameState([0, 3, 6])
        gs.advance_game(1)
        assert gs.current_value == 0
        gs = GameState([0, 3, 6, 0])
        gs.advance_game(1)
        assert gs.current_value == 3
        gs.advance_game(1)
        assert gs.current_value == 3
        gs.advance_game(1)
        assert gs.current_value == 1
        gs.advance_game(1)
        assert gs.current_value == 0
        gs.advance_game(1)
        assert gs.current_value == 4
        gs.advance_game(1)
        assert gs.current_value == 0

    def test_get_nth_spoken_number(self):
        gs = GameState([0, 3, 6])
        assert gs.get_nth_spoken_number(3) == 6
        assert gs.get_nth_spoken_number(6) == 3
        assert gs.get_nth_spoken_number(7) == 1
        assert gs.get_nth_spoken_number(2020) == 436
        assert GameState([1, 3, 2]).get_nth_spoken_number(2020) == 1
        assert GameState([2, 1, 3]).get_nth_spoken_number(2020) == 10
        assert GameState([1, 2, 3]).get_nth_spoken_number(2020) == 27
        assert GameState([2, 3, 1]).get_nth_spoken_number(2020) == 78
        assert GameState([3, 2, 1]).get_nth_spoken_number(2020) == 438
        assert GameState([3, 1, 2]).get_nth_spoken_number(2020) == 1836
