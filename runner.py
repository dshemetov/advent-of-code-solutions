import argparse
from importlib import import_module
import time

from joblib import Memory
memory = Memory("~/.advent_tools/joblib_cache", verbose=0)


@memory.cache
def get_answer(year: int, day: int, part: str) -> int:
    try:
        solution_module = import_module(f"advent{year}.p{day}")
        solution_class_ = getattr(solution_module, "Solution")
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Problem not implemented yet.")
    return getattr(solution_class_(), f"answer_{part}")

# Non-public API: https://github.com/joblib/joblib/blob/754433f617793bc950be40cfaa265a32aed11d7d/joblib/memory.py#L758
# and an answer that led me there https://stackoverflow.com/a/69361221
def is_cached(year: int, day: int, part: str) -> int:
    """Return the list of inputs and outputs from `mem` (joblib.Memory cache)."""
    args = [year, day, part]
    func_id, args_id = get_answer._get_output_identifiers(*args)
    try:
        _ = get_answer.store_backend.load_item([func_id, args_id])
        return True
    except KeyError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get solutions to Advent of Code puzzles.")
    parser.add_argument("-s", "--string", dest="string", type=str, action="store", required=True,
                        help="specify the problem as a contiguous string: {year}.{day}.{part}")
    parser.add_argument("-c", "--clear-cache", dest="clear_cache", action="store_true",
                        help="clear the answer cache for problem")
    args = parser.parse_args()

    year, day, part = args.string.split(".")
    year, day = int(year), int(day)

    if args.clear_cache and is_cached(year, day, part):
        result = get_answer.call_and_shelve(year, day, part).clear()
        t = time.perf_counter()
        print(f"Recalculating answer to year {year}, day {day}, part {part}...")
        ans = get_answer(year, day, part)
        print(ans)
        print(f"(elapsed time: {(time.perf_counter() - t):.5f} seconds)")
    elif is_cached(year, day, part):
        print(f"Looking up cached answer to year {year}, day {day}, part {part}...")
        ans = get_answer(year, day, part)
        print(ans)
    else:
        t = time.perf_counter()
        print(f"Calculating uncached answer to year {year}, day {day}, part {part}...")
        ans = get_answer(year, day, part)
        print(ans)
        print(f"(elapsed time: {(time.perf_counter() - t):.5f} seconds)")
