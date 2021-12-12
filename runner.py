import argparse
import time
from importlib import import_module

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get solutions to Advent of Code puzzles.")
    parser.add_argument("-s", "--string", dest="string", type=str, action="store", required=True,
                        help="specify the problem as a contiguous string: {year}.{day}.{part}")
    parser.add_argument("-c", "--clear-cache", dest="clear_cache", action="store_true",
                        help="clear the answer cache for problem")
    args = parser.parse_args()

    year, day, part = args.string.split(".")
    year, day = int(year), int(day)

    if args.clear_cache:
        result = get_answer.call_and_shelve(year, day, part)
        result.clear()
        t = time.perf_counter()
        print(f"Answer: {get_answer(year, day, part)} (elapsed time: {(time.perf_counter() - t):.5f} seconds)")
    else:
        print(f"Answer: {get_answer(year, day, part)}")
