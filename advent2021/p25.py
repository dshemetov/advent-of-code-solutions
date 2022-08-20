import numpy as np

def solve_a(s: str) -> str:
    return CucumberAutomata(parse_input(s)).update_until_stopped()

def parse_input(s: str):
    lines = s.split("\n")
    cucumber_array = np.array([list(line.strip("\n")) for line in lines])
    return cucumber_array

class CucumberAutomata:
    def __init__(self, array: np.ndarray):
        self.array = array

    def update(self) -> bool:
        n, m = self.array.shape
        was_updated = False

        # Move east
        can_update = [[i, j] for i, j in np.ndindex(n, m) if self.array[i, j] == ">" and self.array[i, (j+1) % m] == "."]
        for i, j in can_update:
            self.array[i, (j+1) % m] = ">"
            self.array[i, j] = "."
        was_updated |= can_update != []

        # Move south
        can_update = [[i, j] for i, j in np.ndindex(n, m) if self.array[i, j] == "v" and self.array[(i+1) % n, j] == "."]
        for i, j in can_update:
            self.array[(i+1) % n, j] = "v"
            self.array[i, j] = "."
        was_updated |= can_update != []

        return was_updated

    def update_until_stopped(self) -> int:
        i = 0
        while self.update():
            i += 1
        return i + 1

def solve_b(s: str) -> str:
    return 0
