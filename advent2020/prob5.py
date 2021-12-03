# Part a
def get_row(string):
    binarized = string.replace("B", "1").replace("F", "0")
    return int(binarized, 2)

def get_col(string):
    binarized = string.replace("R", "1").replace("L", "0")
    return int(binarized, 2)

def get_seatid(string):
    r = get_row(string[:7])
    c = get_col(string[7:])
    return 8 * r + c

test = "FBFBBFFRLR"
assert get_seatid(test) == 357
test = "BFFFBBFRRR"
assert get_seatid(test) == 567
test = "FFFBBBFRRR"
assert get_seatid(test) == 119
test = "BBFFBBFRLL"
assert get_seatid(test) == 820

with open("input5a.txt") as f:
    ans = max(get_seatid(line) for line in f)
    print(ans)

# Part b
with open("input5a.txt") as f:
    ids = set([get_seatid(line) for line in f])

for x in ids:
    if x+1 not in ids and x+2 in ids:
        ans = x
        print(x+1)
        break
