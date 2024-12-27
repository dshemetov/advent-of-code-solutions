module p2024_03
include("utils.jl")


function solve(part::Char, s::AbstractString=test_string2)
    if part == 'a'
        return solve_a(s)
    elseif part == 'b'
        return solve_b(s)
    end
end

function solve_a(s::AbstractString=test_string)::Int
    s = strip(s, '\n')
    m = stack([parse.(Int, [x[1], x[2]]) for x in eachmatch(r"mul\((\d+),(\d+)\)", s)], dims=1)
    return sum(m[:, 1] .* m[:, 2])
end

function solve_b(s::AbstractString=test_string)::Int
    s = strip(s, '\n')
    doflags = vcat([1], [x.offset for x in eachmatch(r"do\(\)", s)])
    dontflags = [x.offset for x in eachmatch(r"don't\(\)", s)]
    active_ranges = []
    hi = 1
    for start in doflags
        if !isempty(active_ranges) && (last(active_ranges)[1] <= start <= last(active_ranges)[2])
            continue
        end
        while hi <= length(dontflags) && dontflags[hi] < start
            hi += 1
        end
        if hi <= length(dontflags)
            push!(active_ranges, (start, dontflags[hi]))
        else
            push!(active_ranges, (start, length(s)))
            break
        end
    end

    valid_substrings = [s[i:j] for (i, j) in active_ranges]
    values = [[x[1], x[2]] for vs in valid_substrings for x in eachmatch(r"mul\((\d+),(\d+)\)", vs)]
    m = stack([parse.(Int, pair) for pair in values], dims=1)
    return sum(m[:, 1] .* m[:, 2])
end

test_string = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
test_string2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

end
