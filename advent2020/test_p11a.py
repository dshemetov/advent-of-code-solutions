import pytest
from .p11a import string_to_array, update_state, np, update_state_until_fixed, count_occupied_seats

class Test11a:
    test_string = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL\n"
    next_states = [
        "#.##.##.##\n#######.##\n#.#.#..#..\n####.##.##\n#.##.##.##\n#.#####.##\n..#.#.....\n##########\n#.######.#\n#.#####.##\n",
        "#.LL.L#.##\n#LLLLLL.L#\nL.L.L..L..\n#LLL.LL.L#\n#.LL.LL.LL\n#.LLLL#.##\n..L.L.....\n#LLLLLLLL#\n#.LLLLLL.L\n#.#LLLL.##\n",
        "#.##.L#.##\n#L###LL.L#\nL.#.#..#..\n#L##.##.L#\n#.##.LL.LL\n#.###L#.##\n..#.#.....\n#L######L#\n#.LL###L.L\n#.#L###.##\n",
        "#.#L.L#.##\n#LLL#LL.L#\nL.L.L..#..\n#LLL.##.L#\n#.LL.LL.LL\n#.LL#L#.##\n..L.L.....\n#L#LLLL#L#\n#.LLLLLL.L\n#.#L#L#.##\n",
        "#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##",
    ]
    def test_update_state(self):
        current_state = string_to_array(self.test_string)
        current_state = update_state(current_state)
        np.testing.assert_equal(current_state, string_to_array(self.next_states[0]))
        current_state = update_state(current_state)
        np.testing.assert_equal(current_state, string_to_array(self.next_states[1]))
        current_state = update_state(current_state)
        np.testing.assert_equal(current_state, string_to_array(self.next_states[2]))
        current_state = update_state(current_state)
        np.testing.assert_equal(current_state, string_to_array(self.next_states[3]))
        current_state = update_state(current_state)
        np.testing.assert_equal(current_state, string_to_array(self.next_states[4]))

    def test_update_state_until_fixed(self):
        current_state = string_to_array(self.test_string)
        current_state = update_state_until_fixed(current_state)
        np.testing.assert_equal(current_state, string_to_array(self.next_states[4]))

    def test_count_occupied_seats(self):
        current_state = string_to_array(self.test_string)
        current_state = update_state(current_state)
        assert count_occupied_seats(current_state) == 71
