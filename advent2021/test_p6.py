import pytest
from .p6 import get_number_fish_after_days, Counter

test_string = """3,4,3,1,2
"""

def test_get_number_fish_after_days():
    fish_ages = Counter([int(x) for x in test_string.split(",")])
    assert get_number_fish_after_days(fish_ages, 18) == 26
    assert get_number_fish_after_days(fish_ages, 80) == 5934
