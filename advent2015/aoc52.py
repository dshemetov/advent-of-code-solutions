f = open("/home/dmitron/code/adventofcode/aoc5.txt",'r')
s = f.read()
a = s.split("\n")

nice = 0
for lin in a:
    if not any( [lin[i:i+2] in lin[i+2:] for i in range(len(lin)-2)] ):
        continue

    if not any( [lin[i] == lin[i+2] for i in range(len(lin)-2)] ):
        continue

    nice += 1

print(nice)
