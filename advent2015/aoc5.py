f = open("/home/dmitron/code/adventofcode/aoc5.txt",'r')
s = f.read()
a = s.split("\n")

alphabet = [chr(i) for i in range(97,123)]
alphabet2 = [str(i)+str(i) for i in alphabet]
print(alphabet2)

nice = 0
for lin in a:
    if "ab" in lin or "cd" in lin or "pq" in lin or "xy" in lin:
        continue

    if not any([ii in lin for ii in alphabet2]):
        print(lin)
        continue

    vow = 0
    vow += sum([i == "a" for i in lin])
    vow += sum([i == "e" for i in lin])
    vow += sum([i == "i" for i in lin])
    vow += sum([i == "o" for i in lin])
    vow += sum([i == "u" for i in lin])

    if vow < 3:
        continue

    nice += 1

print(nice)
