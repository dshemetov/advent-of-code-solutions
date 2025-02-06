function solve(input::Question{2024,16,'a'})
    if input.s == ""
        s = test_string_2024_16
    else
        s = input.s
    end
    s = strip(s, '\n')
    grid = stack([collect(row) for row in split(s, '\n')], dims=1)
    m, n = size(grid)

    start_pos = Tuple(findfirst(==('S'), grid))
    end_pos = Tuple(findfirst(==('E'), grid))
    println(start_pos)
    println(end_pos)

    return 0
end

function solve(input::Question{2024,16,'b'})
    if input.s == ""
        s = test_string_2024_16
    else
        s = input.s
    end
    return 0
end

test_string_2024_16 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
