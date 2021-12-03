import re
from typing import List

from advent_tools import Puzzle

def find_simple_expressions(expr: str) -> List[str]:
    """A simple expression contains no parenthetical sub-statements."""
    return re.compile("\([^\(\)]*[^\(\)]\)").findall(expr)

def evaluate_simple_expression(expr: str) -> str:
    expr = expr.strip("()").split(" ")
    register, tail = int(expr[0]), expr[1:]
    for x in tail:
        if x in ["+", "*"]:
            op = x
        else:
            register = (register * int(x)) if op == "*" else (register + int(x))
    return str(register)

def evaluate_expression(expr: str) -> int:
    matches = find_simple_expressions(expr)
    while matches:
        for match in matches:
            expr = expr.replace(match, evaluate_simple_expression(match))
        matches = find_simple_expressions(expr)
    return int(evaluate_simple_expression(expr))

class Solution:
    @property
    def answer(self) -> int:
        return sum(evaluate_expression(expr) for expr in Puzzle(18, 2020).input_lines)
