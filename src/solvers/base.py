from copy import deepcopy

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
    Base class for sudoku solver
    """
    def __init__(self, grid, display_callback):
        """
        When init instance, the position is the first empty cell

        Parameters
        ----------
        grid : list
            9x9 list of integers
        """
        self.original_grid = grid
        self.grid = deepcopy(grid)
        self.display = lambda: display_callback(self)

    def solve(self):
        """
        Solve sudoku -> Modify self.grid
        IMPLEMENT IN SUBCLASS

        Returns
        -------
        bool
            True when a solution is found, False otherwise
        """
        raise NotImplementedError("Subclasses must implement this!")

    def reset(self):
        """
        Reset grid
        """
        self.grid = deepcopy(self.original_grid)

    def is_valid(self, row, col, num):  # Check if 'num' already exists in the current row or column
        """
        Check if a number can be placed in the current position
        
        Parameters
        ----------
        row : int
            Row index
        col : int
            Column index
        num : int
            Number to check
        """
        for i in range(9):  # Iterate over each row in the grid  
            if self.grid[row][i] == num or self.grid[i][col] == num:   
                return False     # If 'num' already exists in the row or column, return False indicating invalidity
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)   # Calculate the starting index of the 3x3 subgrid
        for i in range(3):  # Iterate over the 3x3 subgrid
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:  # Check if 'num' already exists in the subgrid
                    return False    # If 'num' already exists in the subgrid
        return True # If 'num' does not already exists in the row, column, or subgrid

    def find_empty_cell(self):
        """
        Find the first empty cell in the grid
        
        Returns
        -------
        tuple
            Row index and column index of the empty cell (None, None) if no empty cell is found
        """
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:  # Check if the current cell is empty
                    return i, j  # If the current cell is empty, return its coordinates
        return None, None  # If no empty cell is found, return None for row and col
