import numpy as np

def solve_a(s: str) -> int:
    nums = np.array(s.split(","), dtype=int)
    point = int(np.median(nums))
    return np.abs(point - nums).sum()

def solve_b(s: str) -> int:
    nums = np.array(s.split(","), dtype=int)
    positions = round(np.mean(nums)) + np.array([-1, 0, 1])
    return min(position_cost(n, nums) for n in positions)

def position_cost(n: int, nums: np.ndarray) -> int:
    return sum(m*(m+1)//2 for m in np.abs(n - nums))
