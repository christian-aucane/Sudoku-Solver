
from itertools import product

from tqdm import tqdm


from .base import BaseBruteforceSudokuSolver


class Bruteforce2SudokuSolver(BaseBruteforceSudokuSolver):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.possibles = self.get_all_possibles()

    def possible_values(self, row, col):
        """
        Return possible values for a cell
        
        Parameters
        ----------
        row : int
            Row index
        col : int
            Column index

        Returns
        -------
        list
            List of possible values
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
                if self.grid[i + (row - row % 3)][j + (col - col % 3)] in values:
                    try:
                        values.remove(self.grid[i + (row - row % 3)][j + (col - col % 3)])
                    except ValueError:
                        pass
        return values
    
    def get_all_possibles(self):
        """
        Return all possible combinations of values for each empty cell
        
        Returns
        -------
        list
            List of lists of possible values
        """
        possibles = []
        for row, col in self.empty_cells:
            possibles.append(self.possible_values(row, col))
        return possibles

    @property
    def n_combinations(self):
        """
        Return number of possibilities for the grid
        """
        num_combinations = 1
        for possibilities in self.possibles:
            num_combinations *= len(possibilities)
        return num_combinations

    def solve(self):
        """
        Solve sudoku
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
            self.display()
        return False
