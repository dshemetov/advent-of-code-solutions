function solve(input::Question{2024,14,'a'})
    if input.s == ""
        s = test_string_2024_14
        width = 11
        height = 7
    else
        s = input.s
        width = 101
        height = 103
    end
    s = strip(s, '\n')
    nums = [parse.(Int, eachmatch_vector(line, r"-?\d+")) for line in split(s, '\n')]
    pos = hcat([[n[1], n[2]] for n in nums]...)'  # m x 2 matrix of positions
    vel = hcat([[n[3], n[4]] for n in nums]...)'  # m x 2 matrix of velocities

    for _ in 1:100
        pos .= mod.(pos .+ vel, [width height])
    end

    return get_score(pos, width, height)
end

function solve(input::Question{2024,14,'b'})
    if input.s == ""
        s = test_string_2024_14
        width = 11
        height = 7
    else
        s = input.s
        width = 101
        height = 103
    end
    s = strip(s, '\n')
    nums = [parse.(Int, eachmatch_vector(line, r"-?\d+")) for line in split(s, '\n')]
    pos = hcat([[n[1], n[2]] for n in nums]...)'  # m x 2 matrix of positions
    vel = hcat([[n[3], n[4]] for n in nums]...)'  # m x 2 matrix of velocities

    smallest_score = Inf
    step_of_smallest_score = 0
    for i in 1:10000
        pos .= mod.(pos .+ vel, [width height])
        score = check_line(pos)
        if score < smallest_score
            smallest_score = score
            step_of_smallest_score = i
            # println("New smallest score: $smallest_score at step $step_of_smallest_score")
        end
    end

    return step_of_smallest_score
end

function check_line(pos)
    # Let's make a score function that counts how many robots are on a diagonal
    # line with a slope of 1
    pairs = Set(Tuple(row) for row in eachrow(pos))
    return -sum([1 for pair in pairs if (pair .+ (1, 1) in pairs) || (pair .- (1, 1) in pairs)], init = 0)
end

function get_score(pos, width, height)
    quadrants = [0, 0, 0, 0]
    for i in 1:size(pos, 1)
        if pos[i, 1] < div(width, 2) && pos[i, 2] < div(height, 2)
            quadrants[1] += 1
        elseif pos[i, 1] < div(width, 2) && pos[i, 2] > div(height, 2)
            quadrants[2] += 1
        elseif pos[i, 1] > div(width, 2) && pos[i, 2] < div(height, 2)
            quadrants[3] += 1
        elseif pos[i, 1] > div(width, 2) && pos[i, 2] > div(height, 2)
            quadrants[4] += 1
        end
    end
    return prod(quadrants)
end

function view_robots(robots, width, height)
    grid = fill('.', height, width)

    for robot in robots
        grid[robot.y+1, robot.x+1] = 'R'
    end

    print_grid(grid)
end

test_string_2024_14 = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

