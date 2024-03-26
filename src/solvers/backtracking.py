from solvers.base import BaseSudokuSolver


class BacktrackingSudokuSolver(BaseSudokuSolver):

    def solve(self):
        
        # Print number of empty cells and number of possible combinations
        print(f"Number of empty cells: {self.n_empty_cells}")
        print(f"Number of possible combinations: {self.n_combinations:.2e}")

        return self.solve_recursive()

    def solve_recursive(self):
        """
        Solve sudoku recursively -> Modify self.grid
        
        Returns
        -------
        bool
            True when a solution is found, False otherwise
        """
        row, col = self.find_empty_cell()
        if row is None and col is None:
            return True
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve_recursive():
                    return True
                self.grid[row][col] = 0
        return False
