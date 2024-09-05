"""10. Pipe Maze https://adventofcode.com/2023/day/10"""


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    0
    """
    grid = [list(x) for x in s.strip("\n").splitlines()]
    m, n = len(grid), len(grid[0])

    # TODO: I might need to verify that these are all inbounds here?
    # Unfortunately annoying. It would be nice to not have to worry about it.
    # Otherwise, I might need to worry about it downstream every time I access d
    # with an index.
    # TODO: Unfortunately, we have to loop over all these and try them, since
    # they're likely to have multiple valid S choices (a valid S choice is one
    # that actually connects to both of its neighbors).
    ds = []
    starts = []
    for s in ["-", "|", "F", "J", "L", "7"]:
        d = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "S":
                    starts.append((i, j))
                    grid[i][j] = s
                if grid[i][j] == "-":
                    d[(i, j)] = [(i, j - 1), (i, j + 1)]
                if grid[i][j] == "|":
                    d[(i, j)] = [(i - 1, j), (i + 1, j)]
                if grid[i][j] == "F":
                    d[(i, j)] = [(i + 1, j), (i, j + 1)]
                if grid[i][j] == "J":
                    d[(i, j)] = [(i - 1, j), (i, j - 1)]
                if grid[i][j] == "L":
                    d[(i, j)] = [(i - 1, j), (i, j + 1)]
                if grid[i][j] == "7":
                    d[(i, j)] = [(i + 1, j), (i, j - 1)]
        ds.append(d)

    # TODO: check that all connections are reciprocated. The goal is to detect
    # when a path abruptly stops and not include that distance in the max check
    # below.
    for d in ds:
        for i in range(m):
            for j in range(n):
                if x := d.get((i, j)):
                    first = second = False
                    y, z = d.get(x[0]), d.get(x[1])
                    if y and (i, j) not in y:
                        first = True
                    if z and (i, j) not in z:
                        second = True

                    if first and second:
                        del x[0:2]
                    elif first:
                        del x[0]
                    elif second:
                        del x[1]

                    d[(i, j)] = x

    js = []
    for s, d in zip(starts, ds):
        j = 0
        seen = set()
        cur_queue = [s]
        next_queue = []
        while cur_queue or next_queue:
            while cur_queue:
                x = cur_queue.pop()
                next_queue.extend(e for e in d[x] if e not in seen)
                seen |= {x}
            if not cur_queue and next_queue:
                cur_queue = next_queue.copy()
                next_queue = []
                j += 1
        js.append(j)
        js.append(j)

    return 0


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    0
    """
    s = s.strip("\n")
    return 0


test_string = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
