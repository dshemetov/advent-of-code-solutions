from advent_tools import Puzzle
from typing import List
import numpy as np

def solve_a(s: str) -> int:
    batches = s.split("\n\n")
    numbers = [int(num) for num in batches[0].split(",")]
    boards = [board_from_str(board_str) for board_str in batches[1:]]
    n, m = len(boards[0]), len(boards[0][0])
    board_masks = [np.zeros((n, m)) for board in boards]

    have_winner = False
    for num in numbers:
        for board, board_mask in zip(boards, board_masks):
            board_mask[np.where(board == num)] = 1
            if did_board_win(board_mask):
                have_winner = True
                break
        if have_winner:
            break

    return get_board_score(board, board_mask, num)

def board_from_str(s: str) -> np.ndarray:
    return np.array([line.split() for line in s.split("\n")], dtype=int)

def did_board_win(board_mask: np.ndarray) -> bool:
    n, m = board_mask.shape
    row_wins = (np.all(board_mask[i, :]) for i in range(n))
    col_wins = (np.all(board_mask[:, j]) for j in range(m))
    return any(row_wins) or + any(col_wins)

def get_board_score(board: np.ndarray, board_mask: np.ndarray, last_num: int) -> int:
    return board[~board_mask.astype(bool)].sum() * last_num

def solve_b(s: str) -> int:
    batches = s.split("\n\n")
    numbers = [int(num) for num in batches[0].split(",")]
    boards = [board_from_str(board_str) for board_str in batches[1:]]
    l, n, m = len(boards), len(boards[0]), len(boards[0][0])
    board_masks = [np.zeros((n, m)) for board in boards]

    winner_boards = set()
    for num in numbers:
        for i, (board, board_mask) in enumerate(zip(boards, board_masks)):
            board_mask[np.where(board == num)] = 1
            if did_board_win(board_mask):
                if i in winner_boards:
                    continue
                winner_boards |= set([i])
                if len(winner_boards) == l:
                    break
        if len(winner_boards) == l:
            break

    return get_board_score(board, board_mask, num)


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(4, 2021).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(4, 2021).input_data)
