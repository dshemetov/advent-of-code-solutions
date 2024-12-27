module p2024_01
include("utils.jl")
using .utils: string_to_matrix


function solve(part::Char, s::AbstractString=test_string)
    if part == 'a'
        return solve_a(s)
    elseif part == 'b'
        return solve_b(s)
    end
end

function solve_a(s::AbstractString=test_string)
    m = string_to_matrix(s)
    m[:, 1] = sort(m[:, 1])
    m[:, 2] = sort(m[:, 2])
    sum(abs.(m[:, 1] - m[:, 2]))
end

function Counter(a::AbstractArray)
    Dict(x => count(e -> e == x, a) for x in unique(a))
end

function solve_b(s::AbstractString=test_string)
    m = string_to_matrix(s)
    c = Counter(m[:, 2])
    sum(abs.(x * get!(c, x, 0) for x in m[:, 1]))
end

test_string = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

end