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
    def __init__(self, grid, display_callback=lambda solver: None):
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

    def is_valid(self, row, col, num):
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
        for i in range(9):                                          # Iterate over each row in the grid  
            if self.grid[row][i] == num or self.grid[i][col] == num:   
                return False                                        # If 'num' already exists in the row or column, return False indicating invalidity
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)       # Calculate the starting index of the 3x3 subgrid
        for i in range(3):                                          # Iterate over the 3x3 subgrid
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:  # Check if 'num' already exists in the subgrid
                    return False                                    # If 'num' already exists in the subgrid
        return True                                                 # If 'num' does not already exists in the row, column, or subgrid

    def line(self, y):
        """
        Return values of current line of grid
        """
        return self.grid[y]

    def column(self, x):
        """
        Return values of current column of grid
        """
        return [row[x] for row in self.grid]

    def block(self, x, y):
        """
        Return values of current block of grid
        """
        block_x = x // 3
        block_y = y // 3
        return [self.grid[y][x] for y in range(block_y * 3, block_y * 3 + 3) for x in range(block_x * 3, block_x * 3 + 3)]

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
                    return i, j           # If the current cell is empty, return its coordinates
        return None, None                 # If no empty cell is found, return None for row and col


class BaseBruteforceSudokuSolver(BaseSudokuSolver):
    """
    Base class for bruteforce sudoku solver
    """
    def __init__(self, *args, **kwargs):
        """
        When init instance, the position is the first empty cell

        Parameters
        ----------
        grid : list
            9x9 list of integers
        """
        super().__init__(*args, **kwargs)
        self.empty_cells = self.find_empty_cells()

    def find_empty_cells(self):
        """
        Find all empty cells in the grid
        
        Returns
        -------
        list
            List of empty cells coordinates
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
        """
        for i, (row, col) in enumerate(self.empty_cells):
            self.grid[row][col] = values[i]
            
    def verify_grid(self):
        """
        Verify if all values in grid are unique

        Returns
        -------
        bool
            True if all values in grid are unique, False otherwise
        """
        for row in range(9):
            for col in range(9):
                value = self.grid[row][col]
                if self.line(row).count(value) > 1 or self.column(col).count(value) > 1 or self.block(row, col).count(value) > 1:
                    return False
        return True
