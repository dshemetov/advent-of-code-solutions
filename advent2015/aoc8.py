from advent_tools import Puzzle

s = Puzzle(2015, 8).input_data
lines = s.split("\n")
lines.pop()

print(lines[0])
print(len(lines[0]))
# print("\x")

print(lines[2])
print(len(lines[2]))

eq = {}
eq["a"] = lambda x, y: x & y
print(eq["a"](1, 2))
