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

    :param grid: A 9x9 list of integers representing the Sudoku puzzle.
    :type grid: list

    Attributes:
        original_grid (list): The original unsolved Sudoku grid.
        grid (list): The current state of the Sudoku grid being solved.
        empty_cells (list): A list of coordinates
            of the empty cells in the grid.
        possibles (list): A list of all possible combinations
            of values for each empty cell.

    Methods:
        possible_values: Return possible values for a cell.
        get_all_possibles: Return all possible combinations
            of values for each empty cell.
        n_combinations: Return the number of
            possible combinations for the grid.
        solve: Solve the Sudoku puzzle using a modified brute-force approach.
    """
    def __init__(self, *args, **kwargs):
        """
        When init instance, values is 1 for each empty cells

        Args:
            grid (list): 9x9 list of integers
        """
        super().__init__(*args, **kwargs)

        self.possibles = self.get_all_possibles()

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
            if self.grid[i][col] in values:
                try:
                    values.remove(self.grid[i][col])
                except ValueError:
                    pass
            if self.grid[row][i] in values:
                try:
                    values.remove(self.grid[row][i])
                except ValueError:
                    pass
        for i in range(3):
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
