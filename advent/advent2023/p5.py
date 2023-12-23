"""5. If You Give A Seed A Fertilizer https://adventofcode.com/2023/day/5"""


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    35
    """
    blocks = s.strip("\n").split("\n\n")
    seeds = [int(x) for x in blocks[0].split(": ")[1].split(" ")]
    maps = []
    for block in blocks[1:]:
        maps.append(
            [
                (int(d), int(s), int(r))
                for x in block.split("\n")[1:]
                for d, s, r in [x.split(" ")]
            ]
        )
    nums = []
    for seed in seeds:
        for m in maps:
            for d, s, r in m:
                if seed in range(s, s + r):
                    seed = d + seed - s
                    break
        nums += [seed]
    return min(nums)


def range_intersect(r1, r2):
    """
    Examples:
    >>> range_intersect((3, 7), (2, 5))
    (3, 5)
    >>> range_intersect((3, 7), (4, 8))
    (4, 7)
    >>> range_intersect((3, 7), (8, 10)) is None
    True
    >>> range_intersect((3, 7), (7, 10))
    (7, 7)
    """
    x, y = max(r1[0], r2[0]), min(r1[1], r2[1])
    if x <= y:
        return x, y
    else:
        return None


def range_diff(r1, r2):
    """
    Examples:
    >>> range_diff((3, 7), (2, 5))
    [(2, 2)]
    >>> range_diff((3, 7), (4, 8))
    [(8, 8)]
    >>> range_diff((3, 7), (2, 10))
    [(2, 2), (8, 10)]
    >>> range_diff((3, 7), (8, 10))
    [(8, 10)]
    >>> range_diff((3, 7), (4, 6))
    []
    """
    if not range_intersect(r1, r2):
        return [r2]
    out = []
    if r2[0] < r1[0]:
        out.append((r2[0], r1[0] - 1))
    if r1[1] < r2[1]:
        out.append((r1[1] + 1, r2[1]))
    return out


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    46
    """
    s = test_string
    blocks = s.strip("\n").split("\n\n")
    seeds = [int(x) for x in blocks[0].split(": ")[1].split(" ")]
    maps = []
    for block in blocks[1:]:
        maps.append(
            [
                ((int(s), int(s) + int(r) - 1), int(d) - int(s))
                for x in block.split("\n")[1:]
                for d, s, r in [x.split(" ")]
            ]
        )
    seed_ranges = [
        (seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1] - 1)
        for i in range(len(seeds) // 2)
    ]

    queue = seed_ranges
    for map in maps:
        next_stage = []
        for r, d in map:
            # TODO: I think this filtered queue isn't really doing its job
            # correctly.
            filtered_queue = []
            for seed_range in queue:
                if x := range_intersect(r, seed_range):
                    next_stage.append((x[0] - d, x[1] - d))
                filtered_queue.extend(range_diff(r, seed_range))
            queue = filtered_queue
        queue += next_stage

    return min(x for x, _ in queue)


test_string = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
