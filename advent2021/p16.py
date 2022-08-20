from typing import List, Tuple
from advent_tools import Puzzle

def solve_a(s: str) -> int:
    bs = hex_to_bin(s)
    versions, _ = read_binary(bs)
    return sum(versions)

def hex_to_bin(s: str) -> List[int]:
    bs = bin(int(s, 16))[2:]
    bs = [0] * (-len(bs) % 4) + [int(x) for x in bs] # zero-pad on the left
    return bs

def bin_to_num(ls: List[int]) -> int:
    return sum(2**i * j for i, j in enumerate(reversed(ls)))

def read_binary(bs: List[int]):
    bs = bs.copy()
    versions, numbers = [], []
    while not all(x == 0 for x in bs):
        bs, numbers, versions = unpack_packet(bs, numbers, versions)
    return versions, numbers

def read_packet_header(bs: List[int]) -> Tuple[int, int]:
    version = bin_to_num(bs[:3])
    type_id = bin_to_num(bs[3:6])
    return version, type_id

def unpack_packet(bs: List[int], numbers: List[int], versions: List[int]) -> Tuple[List[int], List[int], List[int]]:
    bs = bs.copy()
    numbers = numbers.copy()
    versions = versions.copy()
    header, bs = bs[:6], bs[6:]
    version, type_id = read_packet_header(header)
    if type_id == 4:
        number, bs = unpack_literal_packet(bs)
        numbers += [number]
        versions += [version]
    else:
        numbers, bs = unpack_operator_packet(bs, numbers, versions)
    return bs, numbers, versions

def unpack_literal_packet(bs: List[int]) -> Tuple[int, List[int]]:
    bs = bs.copy()
    numbers = []
    read_bit = 1
    while read_bit == 1:
        group, bs = bs[:5], bs[5:]
        read_bit = group[0]
        numbers += group[1:]
    return bin_to_num(numbers), bs

def unpack_operator_packet(bs: List[int], numbers: List[int], versions: List[int]) -> Tuple[List[int], List[int], List[int]]:
    bs = bs.copy()
    length_type_id, bs = bs[0], bs[1:]
    if length_type_id == 0:
        sub_packet_length, bs = bs[:15], bs[15:]
        sub_packet_length = bin_to_num(sub_packet_length)
        numbers_, versions_ = read_binary(bs[:sub_packet_length])
        bs = bs[sub_packet_length:]
        numbers += numbers_
        versions += versions_

    number = []
    read_bit = 1
    while read_bit == 1:
        group, bs = bs[:5], bs[5:]
        read_bit = group[0]
        number += group[1:]
    return bin_to_num(number), bs

def solve_b(s: str) -> int:
    return 0


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle().input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle().input_data)
