module p2024_01
include("utils.jl")
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

function solve_a()
    m = string_to_matrix(get_input_string(2024, 1))
    m[:, 1] = sort(m[:, 1])
    m[:, 2] = sort(m[:, 2])
    sum(abs.(m[:, 1] - m[:, 2]))
end

function Counter(a::AbstractArray)
    Dict(e => count(x -> x == e, a) for e in unique(a))
end

function solve_b()
    m = string_to_matrix(get_input_string(2024, 1))
    c = Counter(m[:, 2])
    sum(abs.(x * get!(c, x, 0) for x in m[:, 1]))
end

end