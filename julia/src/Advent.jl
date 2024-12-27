module Advent
export solve

using DataFrames
include("utils.jl")
using .utils: get_input_string

# Include all the problem modules
files = readdir(@__DIR__)
pattern = r"^p(\d{4})_(\d{2})\.jl"
problem_files = filter(x -> match(pattern, x) !== nothing, files)
foreach(include, problem_files)
problem_modules = [Symbol("p$(year)_$(lpad(problem, 2, '0'))") for year in 2020:2024, problem in 1:25 if isdefined(Advent, Symbol("p$(year)_$(lpad(problem, 2, '0'))"))]

function solve(problem_year::Int, problem_number::Int, part::Char, test::Bool=true)
    padded_number = lpad(problem_number, 2, '0')
    module_name = Symbol("p$(problem_year)_$(padded_number)")

    if test
        return @eval @timed $(module_name).solve($(part))
    else
        input = get_input_string(problem_year, problem_number)
        return @eval @timed $(module_name).solve($(part), $(input))
    end
end

function solve(problem_year::Int, problem_number::Int, test::Bool=true)
    part1 = solve(problem_year, problem_number, 'a', test)
    part2 = solve(problem_year, problem_number, 'b', test)
    println("Part 1: $(part1.value) in $(part1.time) seconds")
    println("Part 2: $(part2.value) in $(part2.time) seconds")
end

function solve(problem_year::Int, test::Bool=true)
    df = DataFrame(year=Int[], problem=Int[], part=Char[], value=Int[], time=Float64[])
    for file in problem_files
        m = match(pattern, file)
        year = parse(Int, m.captures[1])
        if year != problem_year
            continue
        end
        problem = parse(Int, m.captures[2])
        part1 = solve(year, problem, 'a', test)
        push!(df, (year, problem, 'a', part1.value, part1.time))
        part2 = solve(year, problem, 'b', test)
        push!(df, (year, problem, 'b', part2.value, part2.time))
    end
    println(df)
end
end
