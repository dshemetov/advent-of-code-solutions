import numpy as np
f = open("/home/dmitron/code/adventofcode/aoc7.txt",'r')
s = f.read()
G = np.zeros((1000,1000))
lines = s.split("\n")
lines.pop()

def srch(var):
    for line in lines:
        words = line.split(" ")
        if "AND" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            if var3 == var:
                return var1, var2, "(" + var1 + " & " + var2 + ")"
        elif "OR" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            if var3 == var:
                return var1, var2, "(" + var1 + " | " + var2 + ")"
        elif "NOT" in line:
            var1, var2 = words[1], words[3]
            if var2 == var:
                return var1, "", "(~" + var1 + ")"
        elif "LSHIFT" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            if var3 == var:
                return var1, "", "(" + var1 + " << " + var2 + ")"
        elif "RSHIFT" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            if var3 == var:
                return var1, "", "(" + var1 + " >> " + var2 + ")"
        else:
            var1, var2 = words[0], words[2]
            if var2 == var:
                return var1, "", var1

cmd = "a"
vararr = ["a"]
eq = {}

for i in range(500):
    cvar = vararr.pop()
    fl = 0

    try:
        ind = cmd.index(cvar)
        fl = 1
    except:
        fl = 0

    if not fl:
        continue

    if cvar in eq.keys():
        var1,var2,cmdnew = eq[cvar][0],eq[cvar][1],eq[cvar][2]
    else:
        var1,var2,cmdnew = srch(cvar)
        eq[cvar] = (var1,var2,cmdnew)
    if len(var1) > 0 and not 57 >= ord(var1[0]) >= 48:
        vararr.insert(0,var1)
    if len(var2) > 0 and not 57 >= ord(var2[0]) >= 48:
        vararr.insert(0,var2)

    while 1:
        try:
            ind = cmd.index(cvar)
            cmd = cmd[:ind] + cmdnew + cmd[ind+len(cvar):]
        except:
            break

    while cvar in vararr:
        vararr.remove(cvar)

    if len(vararr) == 0:
        break


print(len(eq.keys()))
print(cmd)
#print(vararr)
#print(len(vararr))
