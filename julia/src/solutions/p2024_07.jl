function solve(input::Question{2024,7,'a'})
    if input.s == ""
        s = test_string_2024_07
    else
        s = input.s
    end
    s = strip(s, '\n')
    lines = [[parse(Int, y.match) for y in eachmatch(r"\d+", x)] for x in split(s, "\n")]

    total = 0
    for line in lines
        if is_valid_iterative((line[1], line[2:end]), false)
            total += line[1]
        end
    end

    return total
end

function solve(input::Question{2024,7,'b'})
    if input.s == ""
        s = test_string_2024_07
    else
        s = input.s
    end
    s = strip(s, '\n')
    lines = [[parse(Int, y.match) for y in eachmatch(r"\d+", x)] for x in split(s, "\n")]

    total = 0
    for line in lines
        if is_valid_iterative((line[1], line[2:end]), true)
            total += line[1]
        end
    end

    return total
end

function is_valid_iterative(equation::Tuple{Int,Vector{Int}}, with_combination::Bool)::Bool
    stack::Vector{Tuple{Int,Vector{Int}}} = [equation]
    while !isempty(stack)
        current_total, current_numbers = pop!(stack)
        if length(current_numbers) == 1
            if current_total == current_numbers[1]
                return true
            end
            continue
        end

        a, b, rest... = current_numbers
        if current_total < a
            continue
        end

        push!(stack, (current_total, vcat(a + b, rest)))
        push!(stack, (current_total, vcat(a * b, rest)))

        if with_combination
            push!(stack, (current_total, vcat(a * 10^length("$(b)") + b, rest)))
        end
    end
    return false
end

test_string_2024_07 = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
