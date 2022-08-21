from advent_tools import Puzzle, get_bezout_coefficients, get_gcd
from itertools import product
from typing import Tuple, List


def solve_a(s: str) -> int:
    depart_time, bus_schedule = s.split("\n")
    depart_time, bus_schedule = int(depart_time), filter(lambda x: x != "x", bus_schedule.split(","))
    bus_id, next_bus_time = min([(int(bus_id), get_next_bus_time(depart_time, int(bus_id))) for bus_id in bus_schedule], key=lambda x: x[1])
    return bus_id * (next_bus_time - depart_time)


def get_next_bus_time(time: int, period: int) -> int:
    return time + get_minutes_until_next_bus(time, period)


def get_minutes_until_next_bus(time: int, period: int) -> int:
    if time % period == 0:
        return 0
    else:
        return period - time % period


def solve_b(s: str) -> int:
    _, bus_schedule = s.split("\n")
    bus_schedule: List[Tuple[int, int]] = list((-offset, int(bus_id)) for offset, bus_id in enumerate(bus_schedule.split(",")) if bus_id != "x")
    return solve_modular_congruence_equations(bus_schedule)


def solve_modular_congruence_equations(residue_classes: List[Tuple[int, int]]) -> int:
    """Solve an arbitrary system of modular equations.

    Elements in residue_classes are assumed to be pairs (a_i, b_i) and the system of equations to solve is:
        x = a_i mod b_i,          i = 1, 2, ...
    """
    if not all(get_gcd(a, b) == 1 for a, b in product((m for _, m in residue_classes), repeat=2) if a != b):
        raise ValueError("The moduli in the system are not all pair-wise relatively prime.")

    residue_classes_ = residue_classes.copy()
    while len(residue_classes_) > 1:
        bus1, bus2 = residue_classes_.pop(), residue_classes_.pop()
        a, b = solve_modular_congruence_equation_pair(bus1, bus2)
        residue_classes_ += [(a, b)]
    return a


def solve_modular_congruence_equation_pair(b1: Tuple[int, int], b2: Tuple[int, int]) -> Tuple[int, int]:
    """Solve a system of two modular equations.

    Solves the system
        x = a1 mod n1
        x = a2 mod n2
    where a1, n1 = b1 and a2, n2 = b2.
    """
    (a1, n1), (a2, n2) = b1, b2
    s, t = get_bezout_coefficients(n1, n2)
    x = a2 * s * n1 + a1 * t * n2
    return (x % (n1 * n2), n1 * n2)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(13, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(13, 2020).input_data)
