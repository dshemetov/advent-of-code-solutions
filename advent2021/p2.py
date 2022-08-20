def solve_a(s: str) -> int:
    x, y = 0, 0
    for dir, n in (line.split(" ") for line in s.split("\n")):
        if dir == "forward":
            x += int(n)
        if dir == "up":
            y += int(n)
        if dir == "down":
            y -= int(n)
    return abs(x * y)

def solve_b(s: str) -> int:
    x, y, aim = 0, 0, 0
    for dir, n in (line.split(" ") for line in s.split("\n")):
        if dir == "forward":
            x += int(n)
            y += aim * int(n)
        if dir == "up":
            aim -= int(n)
        if dir == "down":
            aim += int(n)
    return abs(x * y)
