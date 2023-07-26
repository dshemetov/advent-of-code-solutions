"""Packet Decoder
https://adventofcode.com/2021/day/16

I got stuck on this one, so here is a clean solution from Reddit.
"""
import collections
import math
import operator

Operator = collections.namedtuple("Operator", ["data", "lenType", "len", "op"])


def solve_a(s: str):
    packet = bin(int(data := s.strip("\n"), 16))[2:].zfill(len(data) * 4)
    ops = [sum, math.prod, min, max, None, operator.gt, operator.lt, operator.eq, print]
    stack = collections.deque([Operator([], 1, 1, 8)])
    pos = 0

    while len(stack) > 0:
        t = int(packet[pos + 3 : pos + 6], 2)

        if t == 4:
            newPos = pos + 6 + (packet[pos + 6 :: 5].index("0") + 1) * 5
            t = "".join(
                [i[1] for i in enumerate(packet[pos + 6 : newPos]) if i[0] % 5 > 0]
            )

            stack[-1].data.append(int(t, 2))
            pos = newPos
        else:
            lenType = int(packet[pos + 6])
            pos += 22 - lenType * 4
            size = (not lenType) * pos + int(packet[pos - 15 + lenType * 4 : pos], 2)
            stack.append(Operator([], lenType, size, t))

        while (
            len(stack) > 0
            and stack[-1].len == (pos, len(stack[-1].data))[stack[-1].lenType]
        ):
            val = stack.pop()
            val = ops[val.op](val.data) if val.op < 5 else ops[val.op](*val.data)
            if len(stack) > 0:
                stack[-1].data.append(val)
