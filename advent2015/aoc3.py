from advent_tools import Puzzle

s = Puzzle(3, 2015).input_data
G = set()
og = [0, 0]
G.add(tuple(og))

for m in s:
    if m == "^":
        og[1] += 1
        G.add(tuple(og))
    elif m == "v":
        og[1] -= 1
        G.add(tuple(og))
    elif m == "<":
        og[0] -= 1
        G.add(tuple(og))
    else:
        og[0] += 1
        G.add(tuple(og))

print(len(G))
