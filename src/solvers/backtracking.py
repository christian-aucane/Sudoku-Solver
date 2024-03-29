"""
Sudoku solver using a backtracking algorithm.

This module provides a class BacktrackingSudokuSolver
that extends the functionality of the BaseSudokuSolver class
to provide a solver for Sudoku puzzles using a backtracking algorithm.
"""
from solvers.base import BaseSudokuSolver


class BacktrackingSudokuSolver(BaseSudokuSolver):
    """
    Sudoku solver using a backtracking algorithm.

    This class extends the functionality
    of the BaseSudokuSolver class to provide
    a solver for Sudoku puzzles using a backtracking algorithm.

    Args:
        grid (list): A 9x9 list of integers representing the Sudoku puzzle.

    Attributes:
        Inherited attributes:
            original_grid (list): The original unsolved Sudoku grid.
            grid (list): The current state of the Sudoku grid being solved.

    Properties:
        Inherited properties:
            n_combinations (int): Number of possibilities for the grid
            n_empty_cells (int): Number of empty cells in the grid

    Methods:
        Inherited methods:
            is_valid(self, row, col, num): Check if a number can
                be placed in (row, column) position.
            line(self, row): Return the values of the current line of the grid.
            column(self, col): Return the values of the current
                column of the grid.
            block(self, row, col): Return the values of the current
                block of the grid.
            find_empty_cell(self): Return the (row, column) of the
                first empty cell in the grid.
        Overridden methods:
            solve: Solve the Sudoku puzzle using a backtracking algorithm.
        Additional methods:
            solve_recursive: Solve the Sudoku puzzle
                recursively using backtracking.
    """
    def solve(self):
        """
        Solve sudoku -> Modify self.grid

        Returns:
            bool: True when a solution is found, False otherwise
        """
        # Print number of empty cells and number of possible combinations
        print(f"Number of empty cells: {self.n_empty_cells}")
        print(f"Number of possible combinations: {self.n_combinations:.2e}")

        return self.solve_recursive()

    def solve_recursive(self):
        """
        Solve sudoku recursively -> Modify self.grid

        Returns:
            bool: True when a solution is found, False otherwise
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
