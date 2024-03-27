from tqdm import tqdm
from solvers.base import BaseBruteforceSudokuSolver


class BruteforceSudokuSolver(BaseBruteforceSudokuSolver):
    """
    Sudoku solver using a brute-force approach.

    This class extends the functionality of the BaseBruteforceSudokuSolver class to provide
    a solver for Sudoku puzzles using a brute-force approach.

    :param grid: A 9x9 list of integers representing the Sudoku puzzle.
    :type grid: list

    Attributes:
        original_grid (list): The original unsolved Sudoku grid.
        grid (list): The current state of the Sudoku grid being solved.
        empty_cells (list): A list of coordinates of the empty cells in the grid.
        values (list): A list of values to be applied to the empty cells.

    Methods:
        next_values: Generate the next set of values to be applied to the empty cells.
        solve: Solve the Sudoku puzzle using a brute-force approach.
    """
    def __init__(self, *args, **kwargs):
        """
        When init instance, values is 1 for each empty cells

        Args:
            grid (list): 9x9 list of integers
        """
        super().__init__(*args, **kwargs)
        self.values = [1] * len(self.empty_cells)

    def next_values(self):
        """
        Generate next values

        Returns:
            bool: True when values are generated, False otherwise
        """
        for i in range(len(self.values)):
            self.values[i] += 1
            if self.values[i] <= 9:
                return True
            else:
                self.values[i] = 1
        return False

    def solve(self):
        """
        Solve sudoku -> Modify self.grid

        Returns:
            bool: True when a solution is found, False otherwise
        """

        # Print number of empty cells and number of possible combinations
        print(f"Number of empty cells: {self.n_empty_cells}")
        print(f"Number of possible combinations: {self.n_combinations:.2e}")
        
        progress_bar = tqdm(total=self.n_combinations)
        
        while not self.verify_grid():
            self.apply_values(self.values)
            if not self.next_values():
                return False
            progress_bar.update(1)
        return True
