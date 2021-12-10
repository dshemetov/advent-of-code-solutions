from advent_tools import Puzzle
import numpy as np

def solve_a(s: str) -> int:
    batches = s.split("\n\n")
    numbers = [int(num) for num in batches[0].split(",")]
    boards = np.stack([board_from_str(board_str) for board_str in batches[1:]])
    l, n, m = boards.shape
    board_masks = np.zeros((l, n, m))

    have_winner = False
    for num in numbers:
        for i in range(l):
            board_masks[i][np.where(boards[i] == num)] = 1
            if did_board_win(board_masks[i]):
                have_winner = True
                break
        if have_winner:
            break

    return get_board_score(boards[i], board_masks[i], num)

def board_from_str(s: str) -> np.ndarray:
    return np.array([line.split() for line in s.split("\n")], dtype=int)

def did_board_win(board_mask: np.ndarray) -> bool:
    return board_mask.all(axis=0).any() or board_mask.all(axis=1).any()

def get_board_score(board: np.ndarray, board_mask: np.ndarray, last_num: int) -> int:
    return board[~board_mask.astype(bool)].sum() * last_num

def solve_b(s: str) -> int:
    batches = s.split("\n\n")
    numbers = [int(num) for num in batches[0].split(",")]
    boards = np.stack([board_from_str(board_str) for board_str in batches[1:]])
    l, n, m = boards.shape
    board_masks = np.zeros((l, n, m))

    winner_boards = set()
    for num in numbers:
        for i in range(l):
            board_masks[i][np.where(boards[i] == num)] = 1
            if did_board_win(board_masks[i]):
                winner_boards |= set([i])
                if len(winner_boards) == l:
                    break
        if len(winner_boards) == l:
            break

    return get_board_score(boards[i], board_masks[i], num)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(4, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(4, 2021).input_data)
