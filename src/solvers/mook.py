import random
import time

from .base import BaseSudokuSolver


class MookSudokuSolver(BaseSudokuSolver):
    """
    A Mook Sudoku Solver (to test interfaces)
    """
    def solve(self):
        """
        Fill empty values with random numbers
        """
        while True:
            row, col = self.find_empty_cell()
            if row is None and col is None:
                break
            self.grid[row][col] = random.randint(1, 9)

        time.sleep(random.uniform(0.5, 2.5))
        return True
