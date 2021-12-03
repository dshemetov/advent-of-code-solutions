from functools import reduce
from operator import mul
from typing import List
import re

from advent_tools import Puzzle

def find_simple_expressions(expr: str) -> List[str]:
    """A simple expression contains no parenthetical sub-statements."""
    return re.compile("\([^\(\)]*[^\(\)]\)").findall(expr)

def find_simple_addition(expr: str) -> re.Match:
    """A simple addition involves the addition of 2 or more numbers and no parenthetical sub-statements."""
    # return re.compile("(\d+ \+ \d+)").findall(expr)    # only matches additions of 2 numbers
    return re.search("(\d+\s+[\s\+\d]+\d+)", expr)       # matches all sequences of additions; \d+ matches one or more digits, \s+ matches at least one space to exclude plain numbers

def evaluate_simple_additions(expr: str) -> str:
    match = find_simple_addition(expr)
    while match:
        s = match.group(0)
        total = str(sum(int(x) for x in s.split(" + ")))
        expr = expr.replace(s, total)
        match = find_simple_addition(expr)
    return expr

def evaluate_simple_expression(expr: str) -> str:
    expr = evaluate_simple_additions(expr.strip("()"))
    return str(reduce(mul, (int(x) for x in expr.split(" * "))))

def evaluate_expression(expr: str) -> int:
    matches = find_simple_expressions(expr)
    while matches:
        for match in find_simple_expressions(expr):
            expr = expr.replace(match, evaluate_simple_expression(match))
        matches = find_simple_expressions(expr)
    return int(evaluate_simple_expression(expr))

class Solution:
    @property
    def answer(self) -> int:
        # 9966990988262 is correct
        return sum(evaluate_expression(expr) for expr in Puzzle(18, 2020).input_lines)
