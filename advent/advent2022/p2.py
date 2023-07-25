"""Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    15
    """
    s = s.strip("\n")
    total = 0
    for line in s.splitlines():
        a, b = line.split()
        if a == "A":
            if b == "X":
                total += 3 + 1
            elif b == "Y":
                total += 6 + 2
            elif b == "Z":
                total += 0 + 3
        elif a == "B":
            if b == "X":
                total += 0 + 1
            elif b == "Y":
                total += 3 + 2
            elif b == "Z":
                total += 6 + 3
        elif a == "C":
            if b == "X":
                total += 6 + 1
            elif b == "Y":
                total += 0 + 2
            elif b == "Z":
                total += 3 + 3
    return total


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    12
    """
    s = s.strip("\n")
    total = 0
    for line in s.splitlines():
        a, b = line.split()

        if b == "X":
            if a == "A":
                total += 0 + 3
            elif a == "B":
                total += 0 + 1
            elif a == "C":
                total += 0 + 2
        elif b == "Y":
            if a == "A":
                total += 3 + 1
            elif a == "B":
                total += 3 + 2
            elif a == "C":
                total += 3 + 3
        elif b == "Z":
            if a == "A":
                total += 6 + 2
            elif a == "B":
                total += 6 + 3
            elif a == "C":
                total += 6 + 1

    return total


test_string = """
A Y
B X
C Z
"""
