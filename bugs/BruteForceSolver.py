from copy import deepcopy

class BaseSudokuSolver:
    def __init__(self, grid):
        self.grid_to_solve = grid
        self.grid = deepcopy(grid)
        self.x = 0
        self.y = 0

    def solve(self) -> list[list[int]]:
        """
        Solve sudoku -> Return solved grid
        """
        raise NotImplementedError("Subclasses must implement this!")

    def clear(self):
        """
        Clear grid
        """
        self.grid = deepcopy(self.grid_to_solve)
        self.x = 0
        self.y = 0

    def move_next(self):
        """
        Move to next empty position in grid
        """
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.x = j
                    self.y = i
                    return True
        return False

    @property
    def line(self):
        """
        Return current line of grid
        """
        return self.grid[self.y]
        
    @property
    def column(self):
        """
        Return current column of grid
        """
        return [x[self.x] for x in self.grid]
    
    @property
    def block(self):
        """
        Return current block of grid
        """
        block_x = self.x // 3
        block_y = self.y // 3
        return [self.grid[y][x] for y in range(block_y * 3, block_y * 3 + 3) for x in range(block_x * 3, block_x * 3 + 3)]
    
    def verify_line(self):
        """
        Verify if all values in line are unique
        """
        for value in self.line:
            if self.line.count(value) > 1 and value != 0:
                return False
        return True
    
    def verify_column(self):
        """
        Verify if all values in column are unique
        """
        for value in self.column:
            if self.column.count(value) > 1 and value != 0:
                return False
        return True
    
    def verify_block(self):
        """
        Verify if all values in block are unique
        """
        for value in self.block:
            if self.block.count(value) > 1 and value != 0:
                return False
        return True
    
    def verify_grid(self):
        """
        Verify if all values in grid are unique
        """
        return self.verify_line() and self.verify_column() and self.verify_block()


class MookSudokuSolver(BaseSudokuSolver):
    def solve(self):
        return self.force_brute()

    def force_brute(self):
        """
        Solve Sudoku using brute force
        """
        if not self.move_next():
            return True

        for num in range(1, 10):
            if self.is_valid_move(num):
                self.grid[self.y][self.x] = num
                if self.force_brute():
                    return True
                self.grid[self.y][self.x] = 0

        return False

    def is_valid_move(self, num):
        """
        Check if a number can be placed in the current position
        """
        return num not in self.line and num not in self.column and num not in self.block
