# Project Euler 736
from heapq import *

def get_p(p, pt):
    x, y = pt
    for f in reversed(p):
        (x, y) = (x + 1, 2 * y) if f == "r" else (2 * x, y + 1)
    return (x, y)

# A* search algorithm
def A_star(start_state, heuristic_distance, choices):
    """
    Parameters
    ----------
    start: list
    h: function: list -> float

    Returns
    ---------
    path: list
        The sequence of states from start to goal.
    """
    priority_queue = []
    current_state = start_state
    current_path = ""

    while current_state[0] - current_state[1] != 0:
        # for choice in "rs":
        for choice in choices:
            future_path = current_path + choice
            distance = heuristic_distance(future_path)
            heappush(priority_queue, (distance, future_path))

        _, current_path = heappop(priority_queue)
        current_state = get_p(current_path, start_state)

    return current_path

def rs_distance(path):
    difference = path.count("s") - path.count("r")
    return abs(1 - difference) + len(path)

path = "rrsrssssr"
print(get_p(path, (45, 90)))

# finds the even length path hella fast
path = A_star([45, 90], rs_distance, choices=["r", "s"])
print(path)

# odd length path; takes 10GB+
path = A_star([45, 90], rs_distance, choices=["rr", "rs", "sr", "ss"])
print(path)