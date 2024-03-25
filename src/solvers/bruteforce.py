from tqdm import tqdm
from solvers.base import BaseBruteforceSudokuSolver


class BruteforceSudokuSolver(BaseBruteforceSudokuSolver):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.values = [1] * len(self.empty_cells)

    def next_values(self):
        """
        Generate next values

        Returns
        -------
        bool
            True if next values are generated, False otherwise
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

        Returns
        -------
        bool
            True when a solution is found, False otherwise
        """

        # Print number of empty cells and number of possible combinations
        print(f"Number of empty cells: {self.n_empty_cells}")
        print(f"Number of possible combinations: {self.n_combinations:.2e}")
        
        progress_bar = tqdm(total=self.n_combinations)
        
        while not self.verify_grid():
            self.apply_values(self.values)
            if not self.next_values():
                return False
            self.display()
            progress_bar.update(1)
        return True
