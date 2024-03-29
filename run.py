import cProfile
import os
import pstats
import time
import traceback
from datetime import date
from importlib import import_module
from typing import Any, Callable
from warnings import warn

import pandas as pd
import typer
from dotenv import load_dotenv, set_key
from joblib import Memory
from rich import print
from rich.table import Table

from advent.tools import get_puzzle_input

memory = Memory(".joblib_cache", verbose=0)
app = typer.Typer(name="Advent of Code Solution Runner", chain=True)

AnswerType = int | str | None
YearOption = typer.Option(
    date.today().year, "--year", "-y", help="The year of the problem."
)
DayOption = typer.Option(None, "--day", "-d", help="The day of the problem.")
PartOption = typer.Option(None, "--part", "-p", help="The part of the problem.")


def timed(func: Callable) -> Callable:
    """Times the function and returns the elapsed time."""

    def new_func(*args, **kwargs) -> tuple[Any, float]:
        t = time.perf_counter()
        out = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - t
        return out, time_elapsed

    return new_func


@memory.cache
def get_answer(year: int, day: int, part: str) -> tuple[AnswerType, float]:
    try:
        solution_module = import_module(f"advent.advent{year}.p{day}")
        solution_method = getattr(solution_module, f"solve_{part}")
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Problem not implemented yet.") from e
    timed_solution_method = timed(solution_method)
    answer, time_taken = timed_solution_method(get_puzzle_input(year, day))
    return answer, time_taken


def get_answer_cache(
    year: int, day: int, part: str, clear_cache: bool
) -> tuple[AnswerType, float, float]:
    if clear_cache:
        if get_answer.check_call_in_cache(year, day, part) is True:
            result = get_answer.call_and_shelve(year, day, part)
            prev_answer, prev_time_taken = result.get()
            result.clear()
            answer, time_taken = get_answer(year, day, part)
            if answer != prev_answer:
                warn(
                    f"Warning, new result differs from cached for {year}.{day}.{part}. New is {answer}, old was {prev_answer}."
                )
        else:
            answer, time_taken = get_answer(year, day, part)
            prev_time_taken = float("nan")
    else:
        answer, prev_time_taken = get_answer(year, day, part)
        time_taken = 0.0
    return answer, time_taken, prev_time_taken


@app.command("solve")
def get_solutions(
    year: int = YearOption,
    day: int = DayOption,
    part: str = PartOption,
    clear_cache: bool = typer.Option(
        False, "--clear-cache", "-c", help="Clear the solution cache for this problem."
    ),
    silent: bool = typer.Option(True, "--silent", "-s", help="Silence warnings."),
    profile: bool = typer.Option(
        False, "--profile", "-P", help="Profile the solution."
    ),
):
    """Prints the solution for a problem or problems."""
    days = range(1, 26) if day is None else [day]
    parts = ["a", "b"] if part is None else [part]
    total_time_taken = 0
    table = Table(title=f"{year} Solutions")
    table.add_column("Day", style="dim", no_wrap=True)
    table.add_column("Part", style="dim", no_wrap=True)
    table.add_column("Answer", style="gold1", justify="right")
    table.add_column("Time Taken", style="steel_blue1", justify="right")
    table.add_column("Prev Time Taken", style="slate_blue3", justify="right")
    row_values = []
    for day in days:
        for part in parts:
            try:
                if profile:
                    with cProfile.Profile() as pr:
                        pr.enable()
                        ans, time_taken, prev_time_taken = get_answer_cache(
                            year, day, part, clear_cache
                        )
                        pr.create_stats()
                        pstats.Stats(pr).sort_stats("cumtime").print_stats(f"p{day}.py")
                else:
                    ans, time_taken, prev_time_taken = get_answer_cache(
                        year, day, part, clear_cache
                    )
            except ModuleNotFoundError:
                if not silent:
                    warn(f"Problem {year}.{day}.{part} not implemented yet.")
                continue
            except Exception as e:
                warn(f"Unexpected error occurred for {year}.{day}.{part}: {e}")
                traceback.print_exception(type(e), e, e.__traceback__)
                continue
            table.add_row(
                str(day),
                part,
                str(ans),
                f"{time_taken:>5.5f}",
                f"{prev_time_taken:>5.5f}",
            )
            row_values.append((day, part, ans, time_taken, prev_time_taken))
            total_time_taken += time_taken

    table.caption = f"Total time taken: {total_time_taken:>5.5f}"
    print(table)
    return table


def make_table_with_pandas(row_values):
    """A test of making a markdown table with Pandas.

    Doesn't look as good as the rich table, but it's simple.
    """
    out2 = pd.DataFrame(
        row_values,
        columns=["Day", "Part", "Answer", "Time Taken", "Prev Time Taken"],
    ).to_markdown(tablefmt="rounded_grid", floatfmt=".5f", index=False)
    print(out2)

    out3 = pd.DataFrame(
        row_values,
        columns=["Day", "Part", "Answer", "Time Taken", "Prev Time Taken"],
    ).to_string(index=False, float_format=lambda x: f"{x:.5f}")
    table = Table(title="2022 Solutions")
    table.add_row(out3)
    print(out3)


@app.command("set-cookie")
def set_cookie(
    cookie: str = typer.Option(
        None,
        "--cookie",
        "-c",
        help="The cookie to set.",
        prompt="Enter your cookie (input hidden)",
        hide_input=True,
    )
):
    """Prints the cookie for the current user.

    Go to https://adventofcode.com/, inspect the browser session, and find your cookie.
    """
    if cookie is not None:
        set_key(".env", "AOC_TOKEN", cookie)
    else:
        raise ValueError("Got empty cookie.")


@app.command("clear-download-cache")
def clear_download_cache(
    year: int = YearOption,
    day: int = DayOption,
):
    """Clears the input download cache."""
    load_dotenv()
    AOC_TOKEN = os.environ.get("AOC_TOKEN")

    days = range(1, 26) if day is None else [day]
    for day in days:
        if get_puzzle_input.check_call_in_cache(year, day, AOC_TOKEN) is True:
            result = get_puzzle_input.call_and_shelve(year, day, AOC_TOKEN)
            result.clear()
            print(f"Download cache cleared for {year}.{day}.")
        else:
            print(f"No solution cache for {year}.{day}.")


@app.command("clear-solution-cache")
def clear_solution_cache(
    year: int = YearOption,
    day: int = DayOption,
    part: str = PartOption,
):
    """Clears the solution cache."""
    days = range(1, 26) if day is None else [day]
    parts = ["a", "b"] if part is None else [part]
    for day in days:
        for part in parts:
            if get_answer.check_call_in_cache(year, day, part) is True:
                result = get_answer.call_and_shelve(year, day, part)
                result.clear()
                print(f"Solution cache cleared for {year}.{day}.{part}.")
            else:
                print(f"No solution cache for {year}.{day}.{part}.")


if __name__ == "__main__":
    app()
