"""Run Advent of Code solutions.

Usage:
    runner.py problem <year.day.part> [-c | --clear-cache]
    runner.py year <year> [-c | --clear-cache]
    runner.py -h | --help
    runner.py --version

Options:
    -h --help            Show this screen.
    --version            Show version.
    -c --clear-cache     Clear cached solutions, if already computed.
"""
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

def get_day_answer(year: int, day: int, part: str, clear_cache: bool, verbose: bool = True) -> int:
    if clear_cache and is_cached(year, day, part):
        if verbose:
            print(f"Recalculating answer to {year}.{day}.{part}...")
        result = get_answer.call_and_shelve(year, day, part).clear()
        t = time.perf_counter()
        ans = get_answer(year, day, part)
        time_taken = time.perf_counter() - t
        if result != ans and verbose:
            print(f"Warning, new result differs from cached for {year}.{day}.{part}...")
    elif is_cached(year, day, part):
        if verbose:
            print(f"Looking up cached answer to {year}.{day}.{part}...")
        ans = get_answer(year, day, part)
        time_taken = 0
    else:
        if verbose:
            print(f"Calculating uncached answer to {year}.{day}.{part}...")
        t = time.perf_counter()
        ans = get_answer(year, day, part)
        time_taken = time.perf_counter() - t

    return ans, time_taken


if __name__ == "__main__":
    args = docopt(__doc__, version='Advent of Code Solution Runner v0.1.0')

    if args.get("problem"):
        year, day, part = args["<year.day.part>"].split(".")
        year, day = int(year), int(day)
        ans, time_taken = get_day_answer(year, day, part, args["--clear-cache"])
        print(ans)
        print(f"(elapsed time: {time_taken:.3f} seconds)")

    if args.get("year"):
        year = int(args["<year>"])
        print(f"{year} Solutions:")
        total_time_taken = 0
        for day in range(1, 26):
            try:
                ans1, time_taken1 = get_day_answer(year, day, "a", args["--clear-cache"], verbose=False)
                ans2, time_taken2 = get_day_answer(year, day, "b", args["--clear-cache"], verbose=False)
            except ModuleNotFoundError:
                ans1, time_taken1 = 0, 0
                ans2, time_taken2 = 0, 0
            
            total_time_taken = total_time_taken + time_taken1 + time_taken2
            print(f"Day {day : >2}. Solution A: {ans1 : >16}, elapsed time {time_taken1 : .3f}. Solution B: {ans2 : >16}, elapsed time {time_taken2 : .3f}.")
        print(f"Total time taken: {total_time_taken}.")
