import pytest
from .p12a import execute_commands, parse_commands, execute_command, north, np, west

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
        state = (np.array([0, 0]), north)
        new_state = execute_command(state, ("F", "10"))
        expected_state = (np.array([0, 10]), north)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

        state = (np.array([0, 0]), north)
        new_state = execute_command(state, ("N", "3"))
        expected_state = (np.array([0, 3]), north)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

        state = (np.array([0, 0]), north)
        new_state = execute_command(state, ("R", "90"))
        expected_state = (np.array([0, 0]), -west)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

        state = (np.array([0, 0]), north)
        new_state = execute_command(state, ("L", "450"))
        expected_state = (np.array([0, 0]), west)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

    def test_execute_commands(self):
        new_state = execute_commands((np.array([0, 0]), -west), parse_commands(test_string))
        expected_state = (np.array([17, -8]), -north)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])
