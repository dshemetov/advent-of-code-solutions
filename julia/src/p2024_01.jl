module p2024_01
include("Advent.jl")
using .Advent


function string_to_matrix(s::String)
    s |>
    strip |>
    (x -> split(x, "\n")) |>
    (x -> [split(e) for e in x]) |>
    (x -> [parse.(Int, e) for e in x]) |>
    stack |>
    transpose
end

"""
```jldoctest
solve_a(test_string)

# output

11
```
"""
function solve_a(s::Union{String,Nothing})
    if isnothing(s)
        s = get_input_string(2024, 1)
    end
    m = string_to_matrix(s)
    m[:, 1] = sort(m[:, 1])
    m[:, 2] = sort(m[:, 2])
    sum(abs.(m[:, 1] - m[:, 2]))
end

function Counter(a::AbstractArray)
    Dict(x => count(e -> e == x, a) for x in unique(a))
end

"""
```jldoctest
solve_b(test_string)

# output

31
```
"""
function solve_b(s::Union{String,Nothing})
    if isnothing(s)
        s = get_input_string(2024, 1)
    end
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