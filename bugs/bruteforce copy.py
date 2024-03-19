from .base import BaseSudokuSolver


class BruteForceSudokuSolver(BaseSudokuSolver):

    def solve(self):
        ...
    
    def force_brute_christian(self):
        grid_completed = False
        while not grid_completed:
            cell_valid = False
            
            value = 1
            while not cell_valid:
                self.fill_current_cell(value)
                if self.is_valid:
                    print("case complétée, valeur : ", self.x, self.y, value)
                    break
                else:
                    # print("case non complétée, valeur : ", value)
                    value += 1
                    if value > 9:
                        self.fill_current_cell(0)
                        return False

            grid_completed = not self.move_next()
        return True

    def force_brute_william(self):
        """
        Solve Sudoku using brute force
        """
        if not self.move_next():
            return True

        for num in range(1, 10):
            if self.is_valid_move(num):
                self.grid[self.y][self.x] = num
                if self.force_brute_william():
                    return True
                self.grid[self.y][self.x] = 0  

        return False

    def is_valid_move(self, num):
        """
        Check if a number can be placed in the current position
        """
        return num not in self.line and num not in self.column and num not in self.block
    