import pytest
from .p11b import string_to_array, get_visible_seat_count, np, update_state_until_fixed, update_state, count_occupied_seats

class Test11b:
    test_string = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL\n"
    next_states = [
        "#.##.##.##\n#######.##\n#.#.#..#..\n####.##.##\n#.##.##.##\n#.#####.##\n..#.#.....\n##########\n#.######.#\n#.#####.##\n",
        "#.LL.LL.L#\n#LLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLL#\n#.LLLLLL.L\n#.LLLLL.L#",
        "#.L#.##.L#\n#L#####.LL\nL.#.#..#..\n##L#.##.##\n#.##.#L.##\n#.#####.#L\n..#.#.....\nLLL####LL#\n#.L#####.L\n#.L####.L#",
        "#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##LL.LL.L#\nL.LL.LL.L#\n#.LLLLL.LL\n..L.L.....\nLLLLLLLLL#\n#.LLLLL#.L\n#.L#LL#.L#",
        "#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##L#.#L.L#\nL.L#.#L.L#\n#.L####.LL\n..#.#.....\nLLL###LLL#\n#.LLLLL#.L\n#.L#LL#.L#",
        "#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##L#.#L.L#\nL.L#.LL.L#\n#.LLLL#.LL\n..#.L.....\nLLL###LLL#\n#.LLLLL#.L\n#.L#LL#.L#"
    ]
    def test_get_visible_seat_count(self):
        test = """.......#.\n...#.....\n.#.......\n.........\n..#L....#\n....#....\n.........\n#........\n...#....."""
        test = string_to_array(test)
        assert get_visible_seat_count(test, np.array([4, 3])) == 8
        test = """.............\n.L.L.#.#.#.#.\n............."""
        test = string_to_array(test)
        assert get_visible_seat_count(test, np.array([1, 2])) == 0
        test = """.##.##.\n#.#.#.#\n##...##\n...L...\n##...##\n#.#.#.#\n.##.##."""
        test = string_to_array(test)
        assert get_visible_seat_count(test, np.array([3, 3])) == 0
        test = """.#.#.\n..#..\n.#.#."""
        test = string_to_array(test)
        assert get_visible_seat_count(test, np.array([1, 2])) == 4

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
        np.testing.assert_equal(current_state, string_to_array(self.next_states[5]))

    def test_count_occupied_seats(self):
        current_state = string_to_array(self.test_string)
        current_state = update_state_until_fixed(current_state)
        assert count_occupied_seats(current_state) == 26
