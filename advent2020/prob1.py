# Part a
with open("input1a.txt") as f:
    ints = f.readlines()
ints = [int(e) for e in ints]

pair_sums = ((ints[i] + ints[j], ints[i], ints[j]) for i in range(len(ints)) for j in range(i, len(ints)))
out = filter(lambda x: x[0] == 2020, pair_sums)
_, b, c = list(out)[0]
print("Part a: ", b*c)

# Part b
with open("input1a.txt") as f:
    ints = f.readlines()
ints = [int(e) for e in ints]

triplet_sums = ((ints[i] + ints[j] + ints[k], ints[i], ints[j], ints[k]) for i in range(len(ints)) for j in range(i, len(ints)) for k in range(j, len(ints)))
out = filter(lambda x: x[0] == 2020, triplet_sums)
_, b, c, d = list(out)[0]
print("Part b: ", b*c*d)