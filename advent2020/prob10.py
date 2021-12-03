# Part a
def parse(fname="input10a.txt"):
    with open(fname) as f:
        for line in f:
            yield int(line)

def part1():
    nums = list(parse())
    nums = [0] + sorted(nums) + [max(nums) + 3]
    diffs = [y-x for x,y in zip(nums[:-1], nums[1:])]
    return diffs.count(1) * diffs.count(3)

print(part1())


# Part b
from itertools import chain, islice, tee
from functools import reduce
from sympy import symbols, Poly

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    return zip(a, islice(b, 1, None))

def diff(iterable):
    """s -> s1-s0, s2-s1, s3-s2, ..."""
    return (y-x for x, y in pairwise(iterable))

def integer_composition(n):
    x = symbols('x')
    f = 0
    for k in range(n+1):
        f += (x + x**2 + x**3)**k
    return Poly(f, x).coeff_monomial(x**n)

def part2():
    # Get the sorted adapter sequence
    nums = list(parse())
    nums = chain([0], sorted(nums), [max(nums) + 3])
    # Find the diffs, add a 3 at the beginning and end to cap off edge 1-sequences
    diffs = chain([3], diff(nums), [3])
    # Find the end points of the 1-sequences
    ixs = (i for i, x in enumerate(diffs) if x == 3)
    # The length of the 1-sequence [a, b] is (b - a - 1)
    diffs = (integer_composition(x-1) for x in diff(ixs))
    return reduce(lambda x, y: x * y, diffs)

print(part2())


# Appendix
# Part b
def get_sequences(nums):
    """Brute force; times out for long sequences."""
    current_choice = nums[0]
    if len(nums) == 1:
        return [[current_choice]]
    choices = [i for i, x in enumerate(nums) if current_choice < x <= current_choice + 3]
    if len(choices) == 0:
        return [[current_choice]]
    sequences = ([current_choice] + seq for i in choices for seq in get_sequences(nums[i:]))
    return sequences

all([len(list(get_sequences(range(k+1)))) == integer_composition(k) for k in range(1, 12)])
