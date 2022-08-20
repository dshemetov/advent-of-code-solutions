from advent_tools import reverse_dict
from itertools import permutations, product
import re
from typing import Dict, List

def solve_a(s: str) -> int:
    matches = (x.groups() for x in re.finditer("(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)", s))
    lines = ([match[:10], match[10:]] for match in matches)
    return sum(1 for _, y in lines for e in y if len(e) in {7, 4, 2, 3})

def solve_b(s: str) -> int:
    matches = (x.groups() for x in re.finditer("(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)", s))
    lines = ([match[:10], match[10:]] for match in matches)
    return sum(decode_entry(ins, outs) for ins, outs in lines)

# TODO: Permutations enumeration
def decode_entry2(inputs: List[str], outputs: List[str]) -> int:
    reductions = make_reductions(inputs)

    for permutation in product(*(permutations(s) for s in ls)):
        permutation = "".join(permutation)
        letter_mapping = dict(zip(permutation, "abcdefg"))
        remapped_inputs = [apply_letter_mapping(s, letter_mapping) for s in inputs]

        if verify_segments(remapped_inputs):
            break

    remapped_outputs = [apply_letter_mapping(s, letter_mapping) for s in outputs]
    return sum(10**i * x for i, x in enumerate(reversed(get_digits_from_segments(remapped_outputs))))

def make_reductions(inputs: List[str]) -> List[str]:
    return "".join()

def decode_entry(inputs: List[str], outputs: List[str]) -> int:
    for permutation in permutations("abcdefg"):
        letter_mapping = dict(zip(permutation, "abcdefg"))
        remapped_inputs = [apply_letter_mapping(s, letter_mapping) for s in inputs]

        if verify_segments(remapped_inputs):
            break

    remapped_outputs = [apply_letter_mapping(s, letter_mapping) for s in outputs]
    return sum(10**i * x for i, x in enumerate(reversed(get_digits_from_segments(remapped_outputs))))

def apply_letter_mapping(s: str, d: Dict[str, str]) -> str:
    return "".join(d[c] for c in s)

def verify_segments(ls: List[str]) -> bool:
    try:
        return set(get_digits_from_segments(ls)) == set(range(10))
    except KeyError:
        return False

def get_digits_from_segments(ls: List[str]) -> List[int]:
    return [segments_to_digit["".join(sorted(s))] for s in ls]

digit_to_segments = dict({
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
})

segments_to_digit = reverse_dict(digit_to_segments)
