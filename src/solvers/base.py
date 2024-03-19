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
    def __init__(self, grid):
        """
        When init instance, the position is the first empty box

        Parameters
        ----------
        grid : list
            9x9 list of integers
        """
        self.original_grid = grid
        self.grid = deepcopy(grid)
        self.x = 0
        self.y = 0
        self.move_next()

    def solve(self):
        """
        Solve sudoku -> Modify self.grid
        IMPLEMENT IN SUBCLASS
        >>> BaseSudokuSolver(
        ... [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ... [0, 0, 0, 0, 0, 0, 0, 0, 0]]).solve()
        """
        raise NotImplementedError("Subclasses must implement this!")

    def reset(self):
        """
        Reset grid
        """
        self.grid = deepcopy(self.original_grid)
        self.x = 0
        self.y = 0
        self.move_next()

    def move_next(self):
        """
        Move to next empty position in grid
        Returns
        -------
        bool        
            True when an empty box is found, False otherwise
        """
        while self.grid[self.y][self.x] != 0:
            if self.y < 8:
                self.y += 1
            else:
                self.y = 0
                if self.x < 8:
                    self.x += 1
                else:
                    return False
        return True

    def fill_current_cell(self, value):
        """
        Fill current box with value

        Parameters
        ----------
        value : int
            value to fill current box with
        """
        self.grid[self.y][self.x] = value
    
    @property
    def line(self):
        """
        Return values of current line of grid
        """
        return self.grid[self.y]

    @property
    def column(self):
        """
        Return values of current column of grid
        """
        return [x[self.y] for x in self.grid]

    @property
    def block(self):
        """
        Return values of current block of grid
        """
        block_x = self.x // 3
        block_y = self.y // 3
        return [self.grid[y][x] for y in range(block_y * 3, block_y * 3 + 3) for x in range(block_x * 3, block_x * 3 + 3)]

    @staticmethod
    def verify_set_of_values(set_of_values):
        """
        Verify if all values a set of values are unique (call with self.line, self.column or self.block)
        """
        for value in set_of_values:
            if set_of_values.count(value) > 1 and value != 0:
                return False
        return True

    @property
    def is_valid(self):
        """
        Verify if all values in line, column and block are unique
        """
        return self.verify_set_of_values(self.line) \
            and self.verify_set_of_values(self.column) \
            and self.verify_set_of_values(self.block)
    