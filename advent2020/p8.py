from advent_tools import Puzzle

def solve_a(s: str) -> int:
    lines = (line.split(" ") for line in s.split("\n"))
    instructions = [(op, int(num)) for op, num in lines]
    acc = 0
    executed_lines = set()
    i = 0
    while i < len(instructions):
        op, num = instructions[i]
        if i in executed_lines:
            break
        executed_lines.add(i)
        if op == "acc":
            acc += num
            i += 1
        elif op == "jmp":
            i += num
        elif op == "nop":
            i += 1
    return acc

def execute_instructions(instructions):
    acc = 0
    executed_lines = set()
    i = 0
    last_line_executed = False
    while i not in executed_lines:
        if i > len(instructions)+1:
            raise LookupError
        elif i == len(instructions):
            last_line_executed = True
            break
        op, num = instructions[i]
        executed_lines.add(i)
        if op == "acc":
            acc += num
            i += 1
        elif op == "jmp":
            i += num
        elif op == "nop":
            i += 1
    return acc, last_line_executed

def solve_b(s: str) -> int:
    lines = (line.split(" ") for line in s.split("\n"))
    instructions = [(op, int(num)) for op, num in lines]
    for i, (x, y) in enumerate(instructions):
        modified_instructions = instructions.copy()
        if x in {"nop", "jmp"}:
            modified_instructions[i] = ("jmp", y) if x == "nop" else ("nop", y)
            val, flag = execute_instructions(modified_instructions)
            if flag:
                break
    return val


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(8, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(8, 2020).input_data)
