module utils
using DotEnv
using DuckDB
using HTTP

# create a new in-memory database
con = DBInterface.connect(DuckDB.DB, "puzzles.db")

# create a table
DBInterface.execute(con, "CREATE TABLE IF NOT EXISTS inputs (year INTEGER, day INTEGER, input VARCHAR)")

function db_cache_write(year::Int, day::Int, input::AbstractString)
    new_con = DBInterface.connect(DuckDB.DB, "puzzles.db")
    stmt = DBInterface.prepare(new_con, "INSERT INTO inputs VALUES(?, ?, ?)")
    DBInterface.execute(stmt, (year, day, input))
    DBInterface.close(new_con)
end

function db_cache_read(year::Int, day::Int)
    new_con = DBInterface.connect(DuckDB.DB, "puzzles.db")
    results = DBInterface.execute(new_con, "SELECT input FROM inputs WHERE year = $year AND day = $day") |> collect
    if length(results) > 0
        return results[1][1]
    end
    DBInterface.close(new_con)
    return nothing
end

function get_input_string(year, day)
    if (input = db_cache_read(year, day)) !== nothing
        return input
    end
    DotEnv.load!(".env")
    url = "https://adventofcode.com/$year/day/$day/input"
    headers = ["cookie" => """session=$(ENV["AOC_TOKEN"])"""]
    s = HTTP.request("GET", url, headers).body |> String |> chomp
    db_cache_write(year, day, s)
    s
end

function string_to_matrix(s::AbstractString)
    s |>
    strip |>
    (x -> split(x, "\n")) |>
    (x -> [split(e) for e in x]) |>
    (x -> [parse.(Int, e) for e in x]) |>
    stack |>
    transpose
end
end