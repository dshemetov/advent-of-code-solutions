from typing import List
import re
from advent_tools import Puzzle

def solve_a(s: str) -> int:
    memory = dict()
    for line in s.split("\n"):
        if "mask" in line:
            mask = list(line.strip("mask = "))
        else:
            key, value = [int(x) for x in re.match("mem\[(\d+)\] = (\d+)", line).groups()]
            memory[key] = apply_mask(value, mask)
    return sum(memory.values())

def apply_mask(v: int, mask: List[str]) -> int:
    bit_list = int_to_bits(v)
    for i in range(36):
        if mask[i] in {"0", "1"}:
            bit_list[i] = int(mask[i])
    return bits_to_int(bit_list)

def bits_to_int(ls: List[int]) -> int:
    return sum(2**i * j for i, j in enumerate(reversed(ls)))

def int_to_bits(n: int) -> List[int]:
    bits = []
    r = n
    for i in reversed(range(36)):
        q = r // (2 ** i)
        bits += [q]
        r = r - 2 ** i * q
    return bits

def solve_b(s: str) -> int:
    memory = dict()
    for line in s.split("\n"):
        if "mask" in line:
            mask = list(line.strip("mask = "))
        else:
            key, value = [int(x) for x in re.match("mem\[(\d+)\] = (\d+)", line).groups()]
            for address in get_memory_addresses(key, mask):
                memory[bits_to_int(address)] = value
    return sum(memory.values())

def get_memory_addresses(v: int, mask: List[str]) -> int:
    bit_list = int_to_bits(v)
    for i in range(36):
        if mask[i] == "1":
            bit_list[i] = int(mask[i])

    addresses = [bit_list]
    for i in range(36):
        if mask[i] == "X":
            addresses_ = []
            for address in addresses:
                address_ = address.copy()
                address_[i] = 0
                addresses_.append(address_)
                address_ = address.copy()
                address_[i] = 1
                addresses_.append(address_)
            addresses = addresses_.copy()
    return addresses


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(14, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(14, 2020).input_data)