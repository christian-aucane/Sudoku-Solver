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
            self.display()
            time.sleep(random.uniform(0.01, 0.02))
        return True
