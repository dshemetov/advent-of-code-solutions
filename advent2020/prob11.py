from copy import deepcopy

# Part a
def parse(fname="input11a.txt"):
    with open(fname) as f:
        for line in f:
            yield [c for c in line.strip()]


def find_chars(grid, symbol):
    ixs = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i][j] == symbol
    ]
    return ixs


def count_neighborhood(ix, grid, symbol):
    n, m = ix
    imax, jmax = (len(grid), len(grid[0]))
    num_symbols = sum(
        [
            1
            for i in range(max(n - 1, 0), min(n + 2, imax))
            for j in range(max(m - 1, 0), min(m + 2, jmax))
            if grid[i][j] == symbol
        ]
    )
    return num_symbols


def update_grid(grid):
    ngrid = deepcopy(grid)
    ixs = find_chars(grid, "L")
    lone_seats = [ix for ix in ixs if count_neighborhood(ix, grid, "#") == 0]
    ixs = find_chars(grid, "#")
    crowded_seats = [ix for ix in ixs if count_neighborhood(ix, grid, "#")-1 >= 4]
    for i, j in lone_seats:
        ngrid[i][j] = "#"
    for i, j in crowded_seats:
        ngrid[i][j] = "L"
    return ngrid

def grid_eq(grid1, grid2):
    if len(grid1) != len(grid2):
        return False
    if len(grid1[0]) != len(grid2[0]):
        return False

    return all(grid1[i][j] == grid2[i][j] for i in range(len(grid1)) for j in range(len(grid1[0])))

grid_eq(grid, grid)
grid_eq(grid, update_grid(grid))
grid_eq(grid, [])

def part1():
    grid = [row for row in parse()]
    # grid = [["L", "L", "L"], [".", ".", "."], ["L", ".", "."]]
    ogrid = []
    while not grid_eq(grid, ogrid):
        ogrid, grid = deepcopy(grid), update_grid(grid)

    return len(find_chars(grid, "#"))

print(part1())


# Part b
grid = [["L", "L", "L"], [".", ".", "."], ["L", ".", "."]]
v = (1, 0)
ix = (0, 0)
vi, vj = v
ixi, ixj = ix
imax, jmax = (len(grid), len(grid[0]))
xmax = min(imax-ixi if vi == 1 else ixi, jmax-ixj if vj == 1 else ixj)
[grid[ixi + i*vi][ixj + i*vj] for i in range(xmax)]

def get_line_array(grid, ix, v):
    pass

def count_neighborhood(ix, grid, symbol):
    n, m = ix
    imax, jmax = (len(grid), len(grid[0]))
    num_symbols = sum(
        [
            1
            for i in range(max(n - 1, 0), min(n + 2, imax))
            for j in range(max(m - 1, 0), min(m + 2, jmax))
            if grid[i][j] == symbol
        ]
    )
    return num_symbols
