"""
Sudoku solver using a modified brute-force approach.

This module provides a class for solving Sudoku puzzles
using a modified brute-force approach.
"""
from itertools import product

from tqdm import tqdm

from .base import BaseBruteforceSudokuSolver


class Bruteforce2SudokuSolver(BaseBruteforceSudokuSolver):
    """
    Sudoku solver using a modified brute-force approach.

    This class extends the functionality of the
    BaseBruteforceSudokuSolver class to provide
    a solver for Sudoku puzzles using a modified brute-force approach.

    Args:
        grid (list): A 9x9 list of integers representing the Sudoku puzzle.

    Attributes:
        Inherited attributes:
            original_grid (list): The original unsolved Sudoku grid.
            grid (list): The current state of the Sudoku grid being solved.
            empty_cells (list): A list of coordinates
                of the empty cells in the grid.
        Aditional attributes:
            possibles (list): A list of all possible combinations
                of values for each empty cell.

    Properties:
        Inherited properties:
            n_combinations (int): Number of possibilities for the grid
            n_empty_cells (int): Number of empty cells in the grid

    Methods:
        Inherited methods:
            is_valid(self, row, col, num): Check if a number
                can be placed in (row, column) position.
            line(self, row): Return the values of the current
                line of the grid.
            column(self, col): Return the values of the
                current column of the grid.
            block(self, row, col): Return the values of the
                current block of the grid.
            find_empty_cell(self): Return the (row, column) of the
                first empty cell in the grid.
            find_empty_cells(self): Return (row, col) for all empty
                cells in the grid.
            apply_values(self, values): Apply values to the grid.
            verify_grid(self): Verify if all values in the grid
                are unique in each row, column, and block.
                Returns True if valid, False otherwise.
        Overridden methods:
            solve(self): Solve the Sudoku puzzle using a
                modified brute-force approach.
        Additional methods:
            possible_values(self, row, col): Return possible values for a cell.
            get_all_possibles(self): Return all possible combinations
                of values for each empty cell.
            n_combinations(self): Return the number of
                possible combinations for the grid.
    """
    def __init__(self, *args, **kwargs):
        """
        When init instance, values is 1 for each empty cells

        Args:
            grid (list): 9x9 list of integers
        """
        super().__init__(*args, **kwargs)

        self.possibles = self.get_all_possibles()

    @property
    def n_combinations(self):
        """
        Return number of possibilities for the grid

        Returns:
            int: Number of possibilities
        """
        num_combinations = 1
        for possibilities in self.possibles:
            num_combinations *= len(possibilities)
        return num_combinations

    def possible_values(self, row, col):
        """
        Return possible values for a cell

        Args:
            row (int): row index
            col (int): column index

        Returns:
            list: possible values
        """
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if self.grid[i][col] in values:  # check column
                try:
                    values.remove(self.grid[i][col])
                except ValueError:
                    pass
            if self.grid[row][i] in values:  # check line
                try:
                    values.remove(self.grid[row][i])
                except ValueError:
                    pass
        for i in range(3):  # check square
            for j in range(3):
                if self.grid[i + (row - row % 3)][j + (col - col % 3)]\
                        in values:
                    try:
                        values.remove(
                            self.grid[i + (row - row % 3)][j + (col - col % 3)]
                        )
                    except ValueError:
                        pass
        return values

    def get_all_possibles(self):
        """
        Return all possible combinations of values for each empty cell

        Returns:
            list: list of lists of possible values
        """
        possibles = []
        for row, col in self.empty_cells:
            possibles.append(self.possible_values(row, col))
        return possibles

    def solve(self):
        """
        Solve sudoku

        Returns:
            bool: True when a solution is found, False otherwise
        """
        # Generate all possible combinations of values for each empty cell
        combinations = product(*self.possibles)

        # Print number of empty cells and number of possible combinations
        print(f"Number of empty cells: {len(self.empty_cells)}")
        print(f"Number of possible combinations: {self.n_combinations:.2e}")

        # Test each combination
        for combination in tqdm(combinations, total=self.n_combinations):
            self.apply_values(combination)
            if self.verify_grid():
                return True
        return False
