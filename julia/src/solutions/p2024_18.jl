function solve(input::Question{2024,18,'a'})
    if input.s == ""
        n, m = 7, 7
        num_bytes = 12
        s = test_string_2024_18
    else
        n, m = 71, 71
        num_bytes = 1024
        s = input.s
    end
    s = strip(s, '\n')
    s = split(s, '\n')
    return solve_maze(s, num_bytes, n, m)
end

function solve_maze(s, num_bytes, n, m)
    grid = fill('.', n, m)
    for line in s[1:num_bytes]
        y, x = parse.(Int, split(line, ","))
        grid[x+1, y+1] = '#'
    end

    # print_grid(grid)

    # Now we have to do a maze solve
    queue = PriorityQueue()
    enqueue!(queue, (1, 1) => 0)

    costs = Dict{Tuple{Int,Int},Int}()
    costs[(1, 1)] = 0

    while !isempty(queue)
        pos = dequeue!(queue)
        cost = costs[pos]
        if pos == (n, m)
            return cost
        end

        for dir in [(0, 1), (1, 0), (-1, 0), (0, -1)]
            x, y = pos .+ dir
            if !(1 <= x <= n && 1 <= y <= m) || grid[x, y] == '#'
                continue
            end
            new_cost = cost + 1
            if !haskey(costs, (x, y)) || new_cost < costs[(x, y)]
                costs[(x, y)] = new_cost
                enqueue!(queue, (x, y) => new_cost)
            end
        end

    end

    return -1
end

function solve(input::Question{2024,18,'b'})
    if input.s == ""
        n, m = 7, 7
        num_bytes = 12
        s = test_string_2024_18
    else
        n, m = 71, 71
        num_bytes = 1024
        s = input.s
    end
    s = strip(s, '\n')
    s = split(s, '\n')
    for i in num_bytes:length(s)
        if solve_maze(s, i, n, m) == -1
            return s[i]
        end
    end
    return -1
end

test_string_2024_18 = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""
