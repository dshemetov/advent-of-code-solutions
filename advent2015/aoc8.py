import numpy as np
f = open("/home/dmitron/code/adventofcode/aoc8.txt",'r')
s = f.read()
lines = s.split("\n")
lines.pop()

print(lines[0])
print(len(lines[0]))
#print("\x")

print(lines[2])
print(len(lines[2]))

eq = {}
eq["a"] = lambda x,y: x & y
print(eq["a"](1,2))
