import pytest
from .p12b import State, execute_commands, parse_commands, execute_command, north, east, south, origin

test_string = """F10
N3
F7
R90
F11"""

class Test12a:
    def test_parse_command(self):
        assert parse_commands(test_string)[0] == ("F", "10")
        assert parse_commands(test_string)[1] == ("N", "3")
        assert parse_commands(test_string)[2] == ("F", "7")
        assert parse_commands(test_string)[3] == ("R", "90")
        assert parse_commands(test_string)[4] == ("F", "11")

    def test_update_ship(self):
        state = State(origin, 10 * east + north)
        new_state = execute_command(state, ("F", "10"))
        expected_state = State(100 * east + 10 * north, 10 * east + north)
        assert new_state == expected_state

        new_state = execute_command(new_state, ("N", "3"))
        expected_state = State(100 * east + 10 * north, 10 * east + 4 * north)
        assert new_state == expected_state

        new_state = execute_command(new_state, ("F", "7"))
        expected_state = State(170 * east + 38 * north, 10 * east + 4 * north)
        assert new_state == expected_state

        new_state = execute_command(new_state, ("R", "90"))
        expected_state = State(170 * east + 38 * north, 4 * east + 10 * south)
        assert new_state == expected_state

        new_state = execute_command(new_state, ("F", "11"))
        expected_state = State(214 * east + 72 * south, 4 * east + 10 * south)
        assert new_state == expected_state

    def test_execute_commands(self):
        new_state = execute_commands(State(origin, 10 * east + north), parse_commands(test_string))
        expected_state = State(214 * east + 72 * south, 4 * east + 10 * south)
        assert new_state == expected_state
