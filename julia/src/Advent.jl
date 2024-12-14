module Advent
export get_input_string

using DotEnv
using DuckDB
using HTTP

# create a new in-memory database
con = DBInterface.connect(DuckDB.DB, "puzzles.db")

# create a table
DBInterface.execute(con, "CREATE TABLE IF NOT EXISTS inputs (year INTEGER, day INTEGER, input VARCHAR)")

# insert data by executing a prepared statement
stmt = DBInterface.prepare(con, "INSERT INTO inputs VALUES(?, ?, ?)")

function db_cache_write(year::Int, day::Int, input::String)
    DBInterface.execute(stmt, (year, day, input))
end

function db_cache_read(year::Int, day::Int)
    results = DBInterface.execute(con, "SELECT input FROM inputs WHERE year = $year AND day = $day") |> collect
    if length(results) > 0
        return results[1][1]
    end
    return nothing
end

function get_input_string(year, day)
    if (input = db_cache_read(year, day)) !== nothing
        return input
    end
    DotEnv.load!(".env")
    url = "https://adventofcode.com/$year/day/$day/input"
    headers = ["cookie" => """session=$(ENV["AOC_TOKEN"])"""]
    s = HTTP.request("GET", url, headers).body |> String
    db_cache_write(year, day, s)
    s
end
end