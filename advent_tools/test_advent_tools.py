import pytest
from .advent_tools import get_gcd, get_bezout_coefficients


def test_get_gcd():
    assert get_gcd(6, 4) == 2
    assert get_gcd(4, 6) == 2
    assert get_gcd(5, 17) == 1
    assert get_gcd(60, 40) == 20

def test_get_gcd():
    a, b = 6, 4
    s, t = get_bezout_coefficients(a, b)
    assert s * a + t * b == get_gcd(a, b)
    a, b = 4, 6
    s, t = get_bezout_coefficients(a, b)
    assert s * a + t * b == get_gcd(a, b)
    s, t = 5, 17
    s, t = get_bezout_coefficients(a, b)
    assert s * a + t * b == get_gcd(a, b)
    a, b = 60, 40
    s, t = get_bezout_coefficients(a, b)
    assert s * a + t * b == get_gcd(a, b)
