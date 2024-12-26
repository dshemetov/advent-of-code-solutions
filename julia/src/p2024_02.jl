module p2024_02
include("utils.jl")


function solve(part::Char, s::String=test_string)
    if part == 'a'
        return solve_a(s)
    elseif part == 'b'
        return solve_b(s)
    end
end

function solve_a(s::String=test_string)::Int
    s = strip(s, '\n')
    lines = [parse.(Int, split(line)) for line in split(s, '\n')]
    diffs = [diff(line) for line in lines]
    all_increasing = [all(diff .>= 0) for diff in diffs]
    all_decreasing = [all(diff .<= 0) for diff in diffs]
    changes_bounded = [all(1 .<= abs.(diff) .<= 3) for diff in diffs]
    return sum(all_increasing .| all_decreasing .& changes_bounded)
end

function solve_b(s::String=test_string)::Int
    s = strip(s, '\n')
    lines = [parse.(Int, split(line)) for line in split(s, '\n')]
    diffs = [diff(line) for line in lines]
    most_increasing = [sum(diff .> 0) >= length(diff) - 1 for diff in diffs]
    most_decreasing = [sum(diff .< 0) >= length(diff) - 1 for diff in diffs]
    changes_bounded = [all(1 .<= abs.(diff) .<= 3) for diff in diffs]
    return sum(most_increasing .| most_decreasing .& changes_bounded)
end

# Example usage
test_string = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

end