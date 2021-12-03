import re

# Part a
def parse():
    with open("input7a.txt") as f:
        for line in f:
            parent, entries = re.match(r'(\w+ \w+) bags contain (.*)', line).groups()
            children = [e.groups() for e in re.finditer(r'(\d+) (\w+ \w+) bags?', entries)]
            yield (parent, children)

# Example: regex capture groups!
line = "light salmon bags contain 5 wavy plum bags, 4 drab white bags, 5 muted bronze bags, 5 mirrored beige bags."
# The +'s are important
parent, entries = re.match(r'(\w+ \w+) bags contain (.*)', line).groups()
print(parent)
# The bags? is optional
print([[int(e.groups()[0]), e.groups()[1]] for e in re.finditer(r'(\d+) (\w+ \w+) bags?', entries)])

def flatten(list):
    return [y for x in list for y in x]

def get_parents(f, d):
    return [e for e in d if f in flatten(d[e])]

def part1():
    d = dict(parse())
    traversed = set()
    to_traverse = set(["shiny gold"])
    while len(to_traverse) > 0:
        entry = to_traverse.pop()
        traversed.add(entry)
        parents = get_parents(entry, d)
        to_traverse |= set(parents) - traversed
    return len(traversed) - 1

print(part1())


# Part b
def get_bags(d, e):
    n = sum(bag[0] * get_bags(d, bag[1]) for bag in d[e]) if len(d[e]) > 0 else 0
    return n + 1

def part2():
    d = dict(parse())
    return get_bags(d, "shiny gold") - 1

print(part2())