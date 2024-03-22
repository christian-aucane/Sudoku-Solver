from solvers.base import BaseSudokuSolver


class BacktrackingSudokuSolver(BaseSudokuSolver):

    def solve(self):
        
        print(f"Number of empty cells: {self.n_empty_cells}")
        print(f"Number of possible combinations: {self.n_combinations:.2e}")

        self.solve_recursive()

    def solve_recursive(self):
        row, col = self.find_empty_cell()
        if row is None and col is None:
            return True
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.display()
                if self.solve_recursive():
                    return True
                self.grid[row][col] = 0
                self.display()
        return False
