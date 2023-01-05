# %%
"""Monkey in the Middle
https://adventofcode.com/2022/day/11

# TODO: speed up solve_b, this is currently my slowest solution, clocking it a glacial 300ms!

Lessons learned:
- default values in lambda functions help avoid late binding errors
- lambda functions are a performance hit
"""
from heapq import nlargest
from math import prod
import re

r = re.compile(r"""Monkey (\d+):
  Starting items: ([\s\d\,]+)
  Operation: new = old ([\+\*]) (old|\d+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)""")

def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    10605
    """
    monkey_datas = {}
    for monkey in s.split("\n\n"):
        num, items, op, val, test, true_monkey, false_monkey = r.match(monkey).groups()

        monkey_data = {}
        monkey_data["items"] = [int(x) for x in items.split(",")]
        monkey_data["operation"] = (op, val)
        monkey_data["test"] = int(test)
        monkey_data["test_true"] = int(true_monkey)
        monkey_data["test_false"] = int(false_monkey)
        monkey_data["inspects"] = 0

        num = int(num)
        monkey_datas[num] = monkey_data

    for _ in range(20):
        for m in range(num + 1):
            md = monkey_datas[m]
            (op, val), test, true_monkey, false_monkey = md["operation"], md["test"], md["test_true"], md["test_false"]
            for i in range(len(md["items"])):
                v = md["items"][i] if val == "old" else int(val)
                if op == "+":
                    md["items"][i] += v
                elif op == "*":
                    md["items"][i] *= v
                md["items"][i] //= 3

                if md["items"][i] % test == 0:
                    monkey_datas[true_monkey]["items"].append(md["items"][i])
                else:
                    monkey_datas[false_monkey]["items"].append(md["items"][i])

            md["inspects"] += len(md["items"])
            md["items"] = []

    lo, hi = nlargest(2, [md["inspects"] for md in monkey_datas.values()])
    return lo * hi

# @profile
def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    10605
    """
    monkey_datas = {}
    for monkey in s.split("\n\n"):
        num, items, op, val, test, true_monkey, false_monkey = r.match(monkey).groups()

        monkey_data = {}
        monkey_data["items"] = [int(x) for x in items.split(",")]
        monkey_data["operation"] = (op, int(val) if val != "old" else val)
        monkey_data["test"] = int(test)
        monkey_data["test_true"] = int(true_monkey)
        monkey_data["test_false"] = int(false_monkey)
        monkey_data["inspects"] = 0

        num = int(num)
        monkey_datas[num] = monkey_data

    mod = prod([md["test"] for md in monkey_datas.values()])

    for _ in range(10000):
        for m in range(num + 1):
            md = monkey_datas[m]
            (op, val), test, true_monkey, false_monkey = md["operation"], md["test"], md["test_true"], md["test_false"]
            for i in range(len(md["items"])):
                v = md["items"][i] if val == "old" else val
                if op == "+":
                    md["items"][i] += v
                elif op == "*":
                    md["items"][i] *= v

                if md["items"][i] > mod:
                    md["items"][i] %= mod

                if md["items"][i] % test == 0:
                    monkey_datas[true_monkey]["items"].append(md["items"][i])
                else:
                    monkey_datas[false_monkey]["items"].append(md["items"][i])

            md["inspects"] += len(md["items"])
            md["items"] = []

    lo, hi = nlargest(2, [md["inspects"] for md in monkey_datas.values()])
    return lo * hi

test_string = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip("\n")

# %%
# from advent_tools import get_puzzle_input
# solve_a(test_string)
# solve_a(get_puzzle_input().strip("\n"))
# solve_b(test_string)
# %load_ext line_profiler
# %lprun -s -f solve_b solve_b(get_puzzle_input(2022, 11).strip("\n"))
