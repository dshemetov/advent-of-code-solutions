# Part a
def parse():
    with open("input8a.txt") as f:
        for line in f:
            op, num = line.split(" ")
            num = int(num)
            yield op, num

def part1():
    instructions = [x for x in parse()]
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

print(part1())


# Part b
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

def part2():
    instructions = [x for x in parse()]
    for i, (x, y) in enumerate(instructions):
        modified_instructions = instructions.copy()
        if x in {"nop", "jmp"}:
            modified_instructions[i] = ("jmp", y) if x == "nop" else ("nop", y)
            val, flag = execute_instructions(modified_instructions)
            if flag:
                break
    return val

print(part2())