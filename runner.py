import time
from datetime import date
from importlib import import_module
from typing import Any, Callable, Optional, Tuple

import typer
from dotenv import set_key
from joblib import Memory
from rich import print
from rich.table import Table

from advent_tools import Puzzle

memory = Memory("~/.advent_tools/joblib_cache", verbose=0)
app = typer.Typer(name="Advent of Code Solution Runner", chain=True)


def timed(func: Callable) -> Callable:
    """Times the function and returns the elapsed time."""

    def new_func(*args, **kwargs) -> Tuple[Any, float]:
        t = time.perf_counter()
        out = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - t
        return out, time_elapsed

    return new_func


@memory.cache
def get_answer(year: int, day: int, part: str) -> Tuple[int, float]:
    try:
        solution_module = import_module(f"advent{year}.p{day}")
        solution_method = getattr(solution_module, f"solve_{part}")
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Problem not implemented yet.")
    answer, time_taken = timed(solution_method)(Puzzle(year, day).input_data)
    return answer, time_taken


def get_answer_cache(year: int, day: int, part: str, clear_cache: bool) -> Tuple[int, float]:
    if clear_cache:
        if get_answer.check_call_in_cache(year, day, part) is True:
            result = get_answer.call_and_shelve(year, day, part)
            prev_answer, prev_time_taken = result.get()
            result.clear()
            answer, time_taken = get_answer(year, day, part)
            if answer != prev_answer:
                print(f"Warning, new result differs from cached for {year}.{day}.{part}. New is {answer}, old was {prev_answer}.")
        else:
            answer, time_taken = get_answer(year, day, part)
            prev_time_taken = None
    else:
        answer, prev_time_taken = get_answer(year, day, part)
        time_taken = 0
    return answer, time_taken, prev_time_taken


@app.command("solve")
def get_solutions(
    year: Optional[int] = typer.Option(date.today().year, "--year", "-y", help="The year of the problem."),
    day: Optional[int] = typer.Option(None, "--day", "-d", help="The day of the problem."),
    part: Optional[str] = typer.Option(None, "--part", "-p", help="The part of the problem."),
    clear_cache: bool = typer.Option(False, "--clear-cache", "-c", help="Clear the cache for this problem."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show warnings."),
):
    """Prints the solution for a problem or problems."""
    days = range(1, 26) if day is None else [day]
    parts = ["a", "b"] if part is None else [part]
    total_time_taken = 0
    run_stats = {}
    for day in days:
        for part in parts:
            try:
                ans, time_taken, prev_time_taken = get_answer_cache(year, day, part, clear_cache)
            except ModuleNotFoundError:
                if verbose:
                    print(f"Problem {year}.{day}.{part} not implemented yet.")
                continue
            except Exception as e:
                print(f"Unexpected error occurred for {year}.{day}.{part}: {e}")
                continue
            run_stats[(day, part)] = [ans, time_taken, prev_time_taken]
            total_time_taken += time_taken

    table = Table(title=f"{year} Solutions", caption=f"Total time taken: {total_time_taken:>5.3f}.")
    table.add_column("Day", style="dim", no_wrap=True)
    table.add_column("Part", style="dim", no_wrap=True)
    table.add_column("Answer", justify="right")
    table.add_column("Time Taken", justify="right")
    table.add_column("Prev Time Taken", justify="right")

    for (day, part), (ans, time_taken, prev_time_taken) in run_stats.items():
        table.add_row(str(day), part, str(ans), f"{time_taken:>5.5f}", f"{prev_time_taken:>5.5f}")

    print(table)


@app.command("set-cookie")
def set_cookie(cookie: Optional[str] = typer.Option(None, "--cookie", "-c", help="The cookie to set.", prompt="Enter your cookie (input hidden)", hide_input=True)):
    """Prints the cookie for the current user.
    
    Go to https://adventofcode.com/, inspect the browser session, and find your cookie.
    """
    if cookie is not None:
        set_key(".env", "AOC_TOKEN", cookie)
    else:
        raise ValueError("Got empty cookie.")


if __name__ == "__main__":
    app()
