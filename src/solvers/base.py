from copy import deepcopy

from utils import count_empty_cells

"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""


class BaseSudokuSolver:
    """
    Base class for Sudoku solvers.

    This class provides basic functionality for solving Sudoku puzzles.

    :param grid: A 9x9 list of integers representing the Sudoku puzzle.
    :type grid: list

    Attributes:
        original_grid (list): The original unsolved Sudoku grid.
        grid (list): The current state of the Sudoku grid being solved.

    Methods:
        solve: Solve the Sudoku puzzle.
        is_valid: Check if a number can be placed in the current position.
        line: Return the values of the current line of the grid.
        column: Return the values of the current column of the grid.
        block: Return the values of the current block of the grid.
        find_empty_cell: Find the first empty cell in the grid.
    """
    def __init__(self, grid):
        """
        When init instance, the position is the first empty cell

        Args:
            grid (list): 9x9 list of integers
        """
        self.original_grid = grid
        self.grid = deepcopy(grid)

    @property
    def n_combinations(self):
        """
        Return number of possibilities for the grid

        Returns:
            int: Number of possibilities
        """
        n_empty_cells = count_empty_cells(self.original_grid)
        return 9 ** n_empty_cells

    @property
    def n_empty_cells(self):
        """
        Return number of empty cells in the grid

        Returns:
            int: Number of empty cells
        """
        return count_empty_cells(self.original_grid)

    def solve(self):
        """
        Solve sudoku -> Modify self.grid
        IMPLEMENT IN SUBCLASS

        Returns:
            bool: True when a solution is found, False otherwise
        """
        raise NotImplementedError("Subclasses must implement this!")

    def is_valid(self, row, col, num):
        """
        Check if a number can be placed in the current position

        Args:
            row (int): row index
            col (int): column index
            num (int): number to be placed

        Returns:
            bool: True if the number can be placed, False otherwise
        """
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def line(self, y):
        """
        Return values of current line of grid

        Args:
            y (int): line index

        Returns:
            list: values of the line
        """
        return self.grid[y]

    def column(self, x):
        """
        Return values of current column of grid

        Args:
            x (int): column index

        Returns:
            list: values of the column
        """
        return [row[x] for row in self.grid]

    def block(self, x, y):
        """
        Return values of current block of grid

        Args:
            x (int): block x index
            y (int): block y index

        Returns:
            list: values of the block
        """
        block_x = x // 3
        block_y = y // 3
        return [
            self.grid[y][x]
            for y in range(block_y * 3, block_y * 3 + 3)
            for x in range(block_x * 3, block_x * 3 + 3)
        ]

    def find_empty_cell(self):
        """
        Find the first empty cell in the grid

        Returns:
            tuple: (row, col) coordinates of the empty cell
                or None, None if no empty cell is found
        """
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None, None


class BaseBruteforceSudokuSolver(BaseSudokuSolver):
    """
    Base class for brute-force Sudoku solvers.

    This class extends the functionality of the
    BaseSudokuSolver class to provide
    methods for solving Sudoku puzzles using a brute-force approach.

    :param grid: A 9x9 list of integers representing the Sudoku puzzle.
    :type grid: list

    Attributes:
        original_grid (list): The original unsolved Sudoku grid.
        grid (list): The current state of the Sudoku grid being solved.
        empty_cells (list): A list of coordinates
            of the empty cells in the grid.

    Methods:
        solve: Solve the Sudoku puzzle using a brute-force approach.
        find_empty_cells: Find all empty cells in the grid.
        apply_values: Apply values to the grid.
        verify_grid: Verify if all values in the grid
            are unique in each row, column, and block.
    """
    def __init__(self, *args, **kwargs):
        """
        When init instance, the position is the first empty cell

        Args:
            grid (list): 9x9 list of integers
        """
        super().__init__(*args, **kwargs)
        self.empty_cells = self.find_empty_cells()

    def find_empty_cells(self):
        """
        Find all empty cells in the grid

        Returns:
            list: list of (row, col) coordinates of the empty cells
        """
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    empty_cells.append((row, col))
        return empty_cells

    def apply_values(self, values):
        """
        Apply values to grid

        Args:
            values (list): list of values to be applied
        """
        for i, (row, col) in enumerate(self.empty_cells):
            self.grid[row][col] = values[i]

    def verify_grid(self):
        """
        Verify if all values in grid are unique

        Returns:
            bool: True if all values in grid are unique
                in each row, column, and block, False otherwise
        """
        for row in range(9):
            for col in range(9):
                value = self.grid[row][col]
                if self.line(row).count(value) > 1\
                    or self.column(col).count(value) > 1\
                        or self.block(row, col).count(value) > 1:
                    return False
        return True
