# Part a
def parse():
    with open("input9a.txt") as f:
        for line in f:
            yield int(line)

def make_pairs(nums):
    from itertools import product
    return set([x + y for x, y in product(nums, repeat=2) if x != y])

def part1():
    nums = list(parse())
    for i, x in enumerate(nums):
        if i < 25:
            continue
        valid_nums = make_pairs(nums[i-25:i])
        if not x in valid_nums:
            break
    return x

print(part1())

# Part b
def part2():
    nums = list(parse())
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j]) == 138879426:
                return i, j, max(nums[i:j]) + min(nums[i:j])

print(part2())