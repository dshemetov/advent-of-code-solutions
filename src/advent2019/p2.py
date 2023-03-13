from advent_tools import get_puzzle_input


# Next we set the inputs, without overwriting.
def setInputs(t, i1, i2):
    s = t.copy()
    s[1] = i1
    s[2] = i2
    return s


# Next we build a library of operations the
# intcode computer can choose to execute.
def plus(temp_intcode, i1, i2, o):
    a1, a2 = temp_intcode[i1], temp_intcode[i2]
    temp_intcode[o] = a1 + a2
    return


def times(temp_intcode, i1, i2, o):
    a1, a2 = temp_intcode[i1], temp_intcode[i2]
    temp_intcode[o] = a1 * a2
    return


instructions = {1: [plus, 3], 2: [times, 3]}


# Here we define a function that operates on intcode. This function runs the main loop.
def run_intcode(temp_intcode):
    i = 0
    while i < len(temp_intcode):
        # First, we recognize the instruction.
        opcode = temp_intcode[i]
        # We make a halt check.
        if opcode == 99:
            break
        instruction = instructions[opcode]
        # the instruction contains the number of
        # arguments
        op = instruction[0]
        num_args = instruction[1]
        args = temp_intcode[i + 1 : i + num_args + 1]
        op(temp_intcode, *args)
        i += num_args + 1

    return temp_intcode[0]


INPUT = [int(x) for x in get_puzzle_input(2019, 2).strip("\n").split(",")]
temp_intcode = setInputs(INPUT, 12, 2)
print("Part a solution: ", run_intcode(temp_intcode))

from itertools import product

for i, j in product(range(99), repeat=2):
    temp_intcode = setInputs(INPUT, i, j)
    if run_intcode(temp_intcode) == 19690720:
        break
print("Part b solution: ", 53 * 100 + j)
