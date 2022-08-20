import numpy as np
import re

def solve_a(s: str) -> int:
    matches = (m.groups() for m in re.finditer("(\d+),(\d+) -> (\d+),(\d+)", s))
    lines = np.array([[(x1, y1), (x2, y2)] for x1, y1, x2, y2 in matches], dtype=int)
    n, m = lines.max(axis=(0, 1)) + 1
    grid = np.zeros((n, m))

    for pt1, pt2 in lines:
        if (pt1 == pt2).any():
            xs, ys = make_line(pt1, pt2).T
            grid[xs, ys] += 1

    return (grid > 1).sum()

def make_line(pt1: np.ndarray, pt2: np.ndarray) -> np.ndarray:
    n = np.abs(pt1 - pt2).max()
    d = (pt1 - pt2) // n
    return np.vstack([pt2 + d * i for i in range(n+1)])

def get_intersection(line1: np.ndarray, line2: np.ndarray) -> np.ndarray:
    (x1, y1), (x2, y2) = line1
    (v1, w1), (v2, w2) = line2
    t, s = np.linalg.inv(np.array([[x2-x1, v1-v2], [y2-y1, w1-w2]])) @ np.array([v1 - x1, w1 - y1])
    return (1-t) * line1[0] + t * line1[1]

def solve_b(s: str) -> int:
    matches = (m.groups() for m in re.finditer("(\d+),(\d+) -> (\d+),(\d+)", s))
    mat = np.array([[(x1, y1), (x2, y2)] for x1, y1, x2, y2 in matches], dtype=int)
    n, m = mat.max(axis=(0, 1)) + 1
    grid = np.zeros((n, m))

    for pt1, pt2 in mat:
        xs, ys = make_line(pt1, pt2).T
        grid[xs, ys] += 1

    return (grid > 1).sum()
