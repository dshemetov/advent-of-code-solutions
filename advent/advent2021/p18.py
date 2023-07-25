"""Snailfish
https://adventofcode.com/2021/day/18
"""
from copy import deepcopy
from math import ceil, floor

import numpy as np


def solve_a(s: str) -> int:
    if not s:
        return 0
    root_trees = parse_input(s)
    end_tree = root_trees[0]
    for root_tree in root_trees[1:]:
        while end_tree.reduce():
            continue
        while root_tree.reduce():
            continue
        end_tree = end_tree + root_tree

    while end_tree.reduce():
        continue

    return end_tree.magnitude()


class SnailfishTree:
    def __init__(self, val: int | None = None, depth: int = 0):
        self.left, self.right, self.parent = None, None, None
        self.val, self.depth = val, depth

    def parse(
        self,
        input: list | int,
        depth: int = 0,
        parent: "SnailfishTree | None" = None,
    ) -> None:
        self.depth = depth
        self.parent = parent
        if isinstance(input, list):
            self.left = SnailfishTree()
            self.left.parse(input[0], depth + 1, self)
            self.right = SnailfishTree()
            self.right.parse(input[1], depth + 1, self)
        else:
            self.val = input

    def increment_depth(self) -> None:
        self.depth += 1
        if self.left is not None:
            self.left.increment_depth()
        if self.right is not None:
            self.right.increment_depth()

    def flatten_to_list(self, to_add: list["SnailfishTree"]):
        if self.val is not None:
            to_add.append(self)
        else:
            self.left.flatten_to_list(to_add)
            self.right.flatten_to_list(to_add)

    def get_right(self, list_of_nodes: list["SnailfishTree"]) -> "SnailfishTree":
        assert self.val is not None
        ind = list_of_nodes.index(self)
        return list_of_nodes[ind + 1] if ind + 1 < len(list_of_nodes) else None

    def get_left(self, list_of_nodes: list["SnailfishTree"]) -> "SnailfishTree":
        assert self.val is not None
        ind = list_of_nodes.index(self)
        return list_of_nodes[ind - 1] if ind > 0 else None

    def needs_explosion(self) -> bool:
        return self.depth > 4

    def needs_split(self) -> bool:
        return self.val is not None and self.val >= 10

    def explode(self, list_of_nodes: list["SnailfishTree"]) -> None:
        l, r = self.left.val, self.right.val

        right_neighbor = self.right.get_right(list_of_nodes)
        if right_neighbor is not None:
            right_neighbor.val += r

        left_neighbor = self.left.get_left(list_of_nodes)
        if left_neighbor is not None:
            left_neighbor.val += l

        self.val = 0
        self.left = None
        self.right = None

    def split(self):
        assert self.val is not None
        assert self.right is None
        assert self.left is None
        cur_val = self.val
        self.val = None
        self.left = SnailfishTree(floor(cur_val / 2))
        self.right = SnailfishTree(ceil(cur_val / 2))
        self.left.parent = self
        self.right.parent = self
        self.left.depth = self.depth + 1
        self.right.depth = self.depth + 1
        # fin

    def magnitude(self) -> int:
        # The magnitude of a pair is 3 times the magnitude of its left element plus
        # 2 times the magnitude of its right element. The magnitude of a regular
        # number is just that number.
        if self.val is not None:
            return self.val
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __repr__(self) -> str:
        if self.val is not None:
            return f"{self.val}"
        else:
            return f"[{self.left},{self.right}]"

    def __add__(self, other: "SnailfishTree") -> "SnailfishTree":
        assert self.depth == other.depth == 0
        parent = SnailfishTree()
        parent.depth = self.depth
        parent.left = self
        parent.right = other
        parent.left.increment_depth()
        parent.right.increment_depth()
        self.parent = other.parent = parent
        return parent

    def to_list(self) -> list[int]:
        if self.parent is None:
            return self.left.to_list() + self.right.to_list()
        elif self.val is None:
            return [self.left.to_list() + self.right.to_list()]
        else:
            return [self.val]

    def get_max_depth(self, maxd: int) -> int:
        if self.val is not None:
            return max(maxd, self.depth)
        else:
            return max(self.left.get_max_depth(maxd), self.right.get_max_depth(maxd))

    def reduce(self) -> bool:
        flattened_list = []
        self.flatten_to_list(flattened_list)
        # max_depth = self.get_max_depth(-np.inf)
        for leaf in flattened_list:
            if leaf.needs_explosion():
                try:
                    leaf.parent.explode(flattened_list)
                except:
                    print(f"Leaf: {leaf}")
                    print(f"leaf.parent: {leaf.parent}")
                    raise Exception("Your doom!")
                return True

        for leaf in flattened_list:
            if leaf.needs_split():
                leaf.split()
                return True

        return False


def parse_input(s: str):
    data_lines = s.split("\n")
    root_trees = []
    for data_line in data_lines:
        arr = eval(data_line.strip())
        root_tree = SnailfishTree()
        root_tree.parse(arr)
        root_trees.append(root_tree)
    return root_trees


def solve_b(s: str) -> int:
    if not s:
        return 0
    root_trees = parse_input(s)
    max_mag = -np.inf
    for i in range(len(root_trees)):
        for j in range(len(root_trees)):
            if i != j:
                tree1 = deepcopy(root_trees[i])
                tree2 = deepcopy(root_trees[j])
                out = tree1 + tree2
                while out.reduce():
                    pass

                max_mag = max(max_mag, out.magnitude())

    return max_mag
