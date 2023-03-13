from advent2020.p12 import (
    State,
    east,
    execute_command_a,
    execute_command_b,
    north,
    np,
    origin,
    parse_commands,
    solve_a,
    solve_b,
    south,
    west,
)

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
        new_state = execute_command_a(state, ("F", "10"))
        expected_state = (np.array([0, 10]), north)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

        state = (np.array([0, 0]), north)
        new_state = execute_command_a(state, ("N", "3"))
        expected_state = (np.array([0, 3]), north)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

        state = (np.array([0, 0]), north)
        new_state = execute_command_a(state, ("R", "90"))
        expected_state = (np.array([0, 0]), -west)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

        state = (np.array([0, 0]), north)
        new_state = execute_command_a(state, ("L", "450"))
        expected_state = (np.array([0, 0]), west)
        np.testing.assert_equal(new_state[0], expected_state[0])
        np.testing.assert_equal(new_state[1], expected_state[1])

    def test_solve_a(self):
        assert solve_a(test_string) == 25


class Test12b:
    def test_parse_command(self):
        assert parse_commands(test_string)[0] == ("F", "10")
        assert parse_commands(test_string)[1] == ("N", "3")
        assert parse_commands(test_string)[2] == ("F", "7")
        assert parse_commands(test_string)[3] == ("R", "90")
        assert parse_commands(test_string)[4] == ("F", "11")

    def test_update_ship(self):
        state = State(origin, 10 * east + north)
        new_state = execute_command_b(state, ("F", "10"))
        expected_state = State(100 * east + 10 * north, 10 * east + north)
        assert new_state == expected_state

        new_state = execute_command_b(new_state, ("N", "3"))
        expected_state = State(100 * east + 10 * north, 10 * east + 4 * north)
        assert new_state == expected_state

        new_state = execute_command_b(new_state, ("F", "7"))
        expected_state = State(170 * east + 38 * north, 10 * east + 4 * north)
        assert new_state == expected_state

        new_state = execute_command_b(new_state, ("R", "90"))
        expected_state = State(170 * east + 38 * north, 4 * east + 10 * south)
        assert new_state == expected_state

        new_state = execute_command_b(new_state, ("F", "11"))
        expected_state = State(214 * east + 72 * south, 4 * east + 10 * south)
        assert new_state == expected_state

    def test_execute_commands(self):
        assert solve_b(test_string) == 214 + 72
