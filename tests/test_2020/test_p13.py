from advent2020.p13 import solve_a, solve_b, get_next_bus_time, solve_modular_congruence_equation_pair

test_strings = [
    """939\n7,13,x,x,59,x,31,19""",
    """1\n17,x,13,19""",
    """1\n67,7,59,61""",
    """1\n67,x,7,59,61""",
    """1\n67,7,x,59,61""",
    """1\n1789,37,47,1889""",
]


def test_get_next_bus_time():
    assert get_next_bus_time(14, 7) == 14
    assert get_next_bus_time(15, 7) == 21
    assert get_next_bus_time(36, 11) == 44


def test_solve_a():
    assert solve_a(test_strings[0]) == 295


def test_solve_modular_congruence_equation_pair():
    assert solve_modular_congruence_equation_pair((2, 5), (3, 7)) == (17, 35)
    assert solve_modular_congruence_equation_pair((2, 5), (3, 7)) == (17, 35)


def test_solve_b():
    assert solve_b(test_strings[0]) == 1068781
    assert solve_b(test_strings[1]) == 3417
    assert solve_b(test_strings[2]) == 754018
    assert solve_b(test_strings[3]) == 779210
    assert solve_b(test_strings[4]) == 1261476
    assert solve_b(test_strings[5]) == 1202161486
