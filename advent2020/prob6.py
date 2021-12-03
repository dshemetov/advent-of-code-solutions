# Part a
def parse():
    with open("input6a.txt") as f:
        s = ""
        for line in f:
            if line != "\n":
                s += line.strip()
            else:
                yield s
                s = ""
        yield s

sum((len(set(qs)) for qs in parse()))


# Part b
from string import ascii_letters
def parse():
    with open("input6a.txt") as f:
        s = set(ascii_letters)
        for line in f:
            if line != "\n":
                s = s.intersection(line)
            else:
                yield s
                s = set(ascii_letters)
        yield s

sum((len(set(qs)) for qs in parse()))