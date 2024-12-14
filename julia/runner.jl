using DataFrames

function solve_problem(problem_year::Int, problem_number::Int, part::Char)
    padded_number = lpad(problem_number, 2, '0')
    module_name = Symbol("p$(problem_year)_$(padded_number)")
    include("julia/p$(problem_year).$(padded_number).jl")

    if part == 'a' && isdefined(eval(module_name), Symbol("solve_a"))
        return @eval @timed $(module_name).solve_a()
    elseif part == 'b' && isdefined(eval(module_name), Symbol("solve_b"))
        return @eval @timed $(module_name).solve_b()
    else
        return nothing
    end
end

function main()
    # Inspect the files in the "julia" directory to get the year and problem
    # number and pass them to solve_problem. Let's make a DataFrame out of the
    # answers and print it. Let's time each run as well.
    files = readdir("julia")
    pattern = r"^p(\d{4})\.(\d{2})\.jl$"
    df = DataFrame(year=Int[], problem=Int[], part=Char[], value=Int[], time=Float64[])
    for file in files
        m = match(pattern, file)
        if m !== nothing
            year = parse(Int, m.captures[1])
            problem = parse(Int, m.captures[2])
            part1 = solve_problem(year, problem, 'a')
            push!(df, (year, problem, 'a', part1.value, part1.time))
            part2 = solve_problem(year, problem, 'b')
            push!(df, (year, problem, 'b', part2.value, part2.time))
        end
    end
    println(df)
end

# Example usage

solve_problem(2024, 1, 'a')
solve_problem(2024, 1, 'b')
main()

