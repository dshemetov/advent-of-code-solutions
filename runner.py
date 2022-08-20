"""Run Advent of Code solutions.

Usage:
    runner.py problem <year.day.part> [-c | --clear-cache]
    runner.py day <year.day> [-c | --clear-cache]
    runner.py year <year> [-c | --clear-cache]
    runner.py -h | --help
    runner.py --version

Options:
    -h --help            Show this screen.
    --version            Show version.
    -c --clear-cache     Clear cached solutions, if already computed.
"""
from typing import Tuple
from docopt import docopt
from importlib import import_module
import time

from joblib import Memory
memory = Memory("~/.advent_tools/joblib_cache", verbose=0)

from advent_tools import Puzzle


@memory.cache
def get_answer(year: int, day: int, part: str) -> int:
    try:
        solution_module = import_module(f"advent{year}.p{day}")
        solution_method = getattr(solution_module, f"solve_{part}")
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Problem not implemented yet.")
    return solution_method(Puzzle(day, year).input_data)

def is_cached(year: int, day: int, part: str) -> int:
    """Return the list of inputs and outputs from `mem` (joblib.Memory cache).
    
    Uses non-public API: https://github.com/joblib/joblib/blob/754433f617793bc950be40cfaa265a32aed11d7d/joblib/memory.py#L758
    and the answer that led me there https://stackoverflow.com/a/69361221.
    """
    args = [year, day, part]
    func_id, args_id = get_answer._get_output_identifiers(*args)
    try:
        _ = get_answer.store_backend.load_item([func_id, args_id])
        return True
    except KeyError:
        return False

def timed(func):
    def new_func(*args, **kwargs):
        t = time.perf_counter()
        out = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - t
        return out, time_elapsed
    return new_func

@timed
def get_answer_cache(year: int, day: int, part: str, clear_cache: bool, verbose: bool = False) -> int:
    if clear_cache and is_cached(year, day, part):
        result = get_answer.call_and_shelve(year, day, part).clear()
        ans = get_answer(year, day, part)
        if result != ans and verbose:
            print(f"Warning, new result differs from cached for {year}.{day}.{part}...")
    else:
        ans = get_answer(year, day, part)
    return ans

def get_part_solution(year: int, day: int, part: str, clear_cache: bool, verbose: bool = False) -> Tuple[int, float]:
    try:
        ans, time_taken = get_answer_cache(year, day, part, clear_cache, verbose)
        print(f"Day {day:>2}. Solution {part}: {ans:>20} (elapsed time {time_taken:>5.3f}).")
    except ModuleNotFoundError:
        ans, time_taken = 0, 0
    return ans, time_taken

def get_day_solutions(year: int, day: int, clear_cache: bool, verbose: bool = False) -> Tuple[Tuple[int, float], Tuple[int, float]]:
    ans1, time_taken1 = get_part_solution(year, day, "a", clear_cache, verbose)
    ans2, time_taken2 = get_part_solution(year, day, "b", clear_cache, verbose)
    return (ans1, time_taken1), (ans2, time_taken2)

def get_year_solutions(year: int, clear_cache: bool):
    print(f"{year} Solutions:")

    total_time_taken = 0
    for day in range(1, 26):
        (_, time_taken1), (_, time_taken2) = get_day_solutions(year, day, clear_cache)
        total_time_taken += time_taken1 + time_taken2
    print(f"Total time taken: {total_time_taken}.")

if __name__ == "__main__":
    args = docopt(__doc__, version='Advent of Code Solution Runner v0.1.0')

    if args.get("problem"):
        year, day, part = args["<year.day.part>"].split(".")
        year, day = int(year), int(day)
        get_part_solution(year, day, part, args["--clear-cache"])

    if args.get("day"):
        year, day = args["<year.day>"].split(".")
        year, day = int(year), int(day)
        get_day_solutions(year, day, args["--clear-cache"])

    if args.get("year"):
        year = int(args["<year>"])
        get_year_solutions(year, args["--clear-cache"])
