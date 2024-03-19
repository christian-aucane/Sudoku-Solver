
import random
import time

from solvers.base import BaseSudokuSolver


class MookSudokuSolver(BaseSudokuSolver):
    """
    A Mook Sudoku Solver (to test interfaces)
    """
    def solve(self):
        """
        Fill empty values with random numbers
        """
        while True:
            self.fill_current_box(random.randint(1, 9))
            if not self.move_next():
                break

        time.sleep(random.uniform(0.5, 2.5))
