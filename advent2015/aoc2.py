import os

f = open("/home/dmitron/code/adventofcode/aoc2.txt",'r')
a = f.read()
b = a.split("\n")
c = [i.split("x") for i in b]
c.pop()
d = [[int(i[0]),int(i[1]),int(i[2])] for i in c]
ansp1 = sum([2*(int(i[0])*int(i[1])+int(i[1])*int(i[2])+int(i[2])*int(i[0])) + min(int(i[0])*int(i[1]),int(i[1])*int(i[2]),int(i[0])*int(i[2])) for i in c])
ansp2 = sum([ i[0]*i[1]*i[2] + 2*min(int(i[0])+int(i[1]),int(i[1])+int(i[2]),int(i[2])+int(i[0])) for i in d])

print(ansp1)
print(ansp2)
