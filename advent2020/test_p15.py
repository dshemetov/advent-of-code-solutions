import pytest
from .p15 import GameState


def test_get_next_number():
    gs = GameState([0, 3, 6])
    assert GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn) == 0
    gs = GameState([0, 3, 6, 0])
    assert GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn) == 3
    gs = GameState([0, 3, 6, 0, 3])
    assert GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn) == 3
    gs = GameState([0, 3, 6, 0, 3, 3])
    assert GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn) == 1
    gs = GameState([0, 3, 6, 0, 3, 3, 1])
    assert GameState.get_next_number(gs.current_value, gs.turn_number, gs.last_turn) == 0

def test_advance_game():
    gs = GameState([0, 3, 6])
    gs.advance_game(1)
    assert gs.current_value == 0
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

def test_get_nth_spoken_number():
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
