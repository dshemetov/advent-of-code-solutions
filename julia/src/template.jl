module p202Y_XX
include("utils.jl")


function solve(part::Char, s::AbstractString=test_string)
    if part == 'a'
        return solve_a(s)
    elseif part == 'b'
        return solve_b(s)
    end
end

function solve_a(s::AbstractString=test_string)::Int
    return 0
end

function solve_b(s::AbstractString=test_string)::Int
    return 0
end

test_string = """
"""

end
