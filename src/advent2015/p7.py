import numpy as np


def solve_a(s: str) -> int:

    G = np.zeros((1000, 1000))
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
            var1, var2, cmdnew = eq[cvar][0], eq[cvar][1], eq[cvar][2]
        else:
            var1, var2, cmdnew = srch(cvar)
            eq[cvar] = (var1, var2, cmdnew)
        if len(var1) > 0 and not 57 >= ord(var1[0]) >= 48:
            vararr.insert(0, var1)
        if len(var2) > 0 and not 57 >= ord(var2[0]) >= 48:
            vararr.insert(0, var2)

        while 1:
            try:
                ind = cmd.index(cvar)
                cmd = cmd[:ind] + cmdnew + cmd[ind + len(cvar) :]
            except:
                break

        while cvar in vararr:
            vararr.remove(cvar)

        if len(vararr) == 0:
            break


    print(len(eq.keys()))
    print(cmd)
    # print(vararr)
    # print(len(vararr))
    return 0

def solve_b(s: str) -> int:
    return 0

    G = np.zeros((1000, 1000))
    lines = s.split("\n")
    lines.pop()

    eq = {}
    for line in lines:
        words = line.split(" ")
        if "AND" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            eq[var3] = (var1, var2, "(" + var1 + " & " + var2 + ")")
        elif "OR" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            eq[var3] = (var1, var2, "(" + var1 + " | " + var2 + ")")
        elif "NOT" in line:
            var1, var2 = words[1], words[3]
            eq[var2] = (var1, "", "((~65536 + " + var1 + ") % 65536)")
        elif "LSHIFT" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            eq[var3] = (var1, "", "(" + var1 + " << " + var2 + ")")
        elif "RSHIFT" in line:
            var1, var2, var3 = words[0], words[2], words[4]
            eq[var3] = (var1, "", "(" + var1 + " >> " + var2 + ")")
        else:
            var1, var2 = words[0], words[2]
            eq[var2] = ("", "", var1)


    for i in range(0):
        print("Iter:" + str(i))
        for j in eq.keys():
            if eq[j][1] == "" and eq[j][0] != "":
                k = eq[j][0]
                if eq[k][0] == "" and eq[k][1] == "" and 48 <= ord(eq[k][2][0]) <= 57:
                    print("j:", j, eq[j], k, eq[k])
                    cmd = eq[j][2]
                    ind = cmd.index(k)
                    cmd = cmd[:ind] + eq[k][2] + cmd[ind + len(k) :]
                    eq[j] = ("", "", str(eval(cmd)))
                    print("newj:", eq[j])
            elif eq[j][0] == "" and eq[j][1] == "" and 48 <= ord(eq[j][2][0]) <= 57:
                continue
            elif eq[j][0] == "" and eq[j][1] == "" and not 48 <= ord(eq[j][2][0]) <= 57:
                k = eq[j][2]
                if eq[k][0] == "" and eq[k][1] == "" and 48 <= ord(eq[k][2][0]) <= 57:
                    print("j:", j, eq[j], k, eq[k])
                    cmd = eq[j][2]
                    ind = cmd.index(k)
                    cmd = cmd[:ind] + eq[k][2] + cmd[ind + len(k) :]
                    eq[j] = ("", "", str(eval(cmd)))
                    print("newj:", eq[j])
            elif eq[j][0] != "" and eq[j][1] != "":
                if 48 <= ord(eq[j][0][0]) <= 57 and 48 <= ord(eq[j][1][0]) <= 57:
                    print("j:", j, eq[j], k, eq[k])
                    cmd = eq[j][2]
                    eq[j] = ("", "", str(eval(cmd)))
                    print("newj:", eq[j])
                elif 48 <= ord(eq[j][0][0]) <= 57 and not 48 <= ord(eq[j][1][0]) <= 57:
                    k = eq[j][1]
                    if eq[k][0] == "" and eq[k][1] == "":
                        print("j:", j, eq[j], k, eq[k])
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind + len(k) :]
                        eq[j] = ("", "", str(eval(cmd)))
                        print("newj:", eq[j])
                elif not 48 <= ord(eq[j][0][0]) <= 57 and 48 <= ord(eq[j][1][0]) <= 57:
                    k = eq[j][0]
                    if eq[k][0] == "" and eq[k][1] == "":
                        print("j:", j, eq[j], k, eq[k])
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind + len(k) :]
                        eq[j] = ("", "", str(eval(cmd)))
                        print("newj:", eq[j])
                elif not 48 <= ord(eq[j][0][0]) <= 57 and not 48 <= ord(eq[j][1][0]) <= 57:
                    k1 = eq[j][0]
                    k2 = eq[j][1]
                    if eq[k1][0] == "" and eq[k1][1] == "" and eq[k2][0] == "" and eq[k2][1] == "":
                        print("j:", j, eq[j], k1, eq[k1], k2, eq[k2])
                        cmd = eq[j][2]
                        ind = cmd.index(k1)
                        cmd = cmd[:ind] + eq[k1][2] + cmd[ind + len(k1) :]
                        ind = cmd.index(k2)
                        cmd = cmd[:ind] + eq[k2][2] + cmd[ind + len(k2) :]
                        eq[j] = ("", "", str(eval(cmd)))
                        print("newj:", eq[j])

    print(eq["a"])

    """
        for k in eq.keys():
            if eq[k][0] == "" and eq[k][1] == "" and 48 <= ord(eq[k][2][0]) <= 57:
                #print(k)
                #print(eq[k])
                for j in eq.keys():
                    if eq[j][0] == k and eq[j][1] == "":
                        print(j)
                        print(eq[j])
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind+len(k):]
                        eq[j] = ("", "", str(eval(cmd)))
                        print(eq[j])
                    elif eq[j][1] == k and eq[j][0] == "":
                        print(j)
                        print(eq[j])
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind+len(k):]
                        eq[j] = ("", "", str(eval(cmd)))
                        print(eq[j])
                    elif eq[j][0] == k and 48 <= ord(eq[j][1][0]) <= 57:
                        print(j)
                        print(eq[j])
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind+len(k):]
                        eq[j] = ("", "", str(eval(cmd)))
                        print(eq[j])
                    elif eq[j][1] == k and 48 <= ord(eq[j][0][0]) <= 57:
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind+len(k):]
                        eq[j] = ("", "", str(eval(cmd)))
                        print(eq[j])
                    elif eq[j][0] == "" and eq[j][1] == "" and eq[j][2] == k:
                        cmd = eq[j][2]
                        ind = cmd.index(k)
                        cmd = cmd[:ind] + eq[k][2] + cmd[ind+len(k):]
                        eq[j] = ("", "", str(eval(cmd)))
                        print(eq[j])
                #del eq[k]
    """

