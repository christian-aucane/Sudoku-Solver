from solvers.base import BaseSudokuSolver


class BacktrackingSudokuSolver(BaseSudokuSolver):

    def solve(self):
        row, col = self.find_empty_cell()
        if row is None and col is None:
            return True
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.display()
                if self.solve():
                    return True
                self.grid[row][col] = 0
                self.display()
        return False
