module Advent
export solve

using DataFrames
include("utils.jl")

# Dispatch to the right function by using parametric types
# https://discourse.julialang.org/t/how-to-dispatch-by-value/43266
struct Question{Y,D,P}
    s::AbstractString
end

# Include all the solution files
solution_files = readdir(joinpath(@__DIR__, "solutions"), join=true)
foreach(include, solution_files)

function solve(year::Int, day::Int, part::Char, test::Bool=true)
    if test
        arg = Question{year,day,part}("")
    else
        input = get_input_string(year, day)
        arg = Question{year,day,part}(input)
    end
    return @timed solve(arg)
end

function solve(year::Int, day::Int, test::Bool=true)
    part1 = solve(year, day, 'a', test)
    part2 = solve(year, day, 'b', test)
    println("Part 1: $(part1.value) in $(part1.time) seconds")
    println("Part 2: $(part2.value) in $(part2.time) seconds")
end

function solve(year::Int, test::Bool=true)
    df = DataFrame(year=Int[], day=Int[], part=Char[], value=Int[], time=Float64[])
    pattern = r"p(\d{4})_(\d{2}).jl"
    for file in solution_files
        m = match(pattern, file)
        y = parse(Int, m.captures[1])
        if year != y
            continue
        end
        day = parse(Int, m.captures[2])
        part1 = solve(year, day, 'a', test)
        push!(df, (year, day, 'a', part1.value, part1.time))
        part2 = solve(year, day, 'b', test)
        push!(df, (year, day, 'b', part2.value, part2.time))
    end
    # # Sort the DataFrame by year, day, and part
    # sort!(df, [:year, :day, :part])
    println(df)
    println()
    println("Total time: $(sum(df.time)) seconds")
end

# solve(Question{2024,9,'a'}(""))

end
