# Sudoku-Solver
A Sudoku Solver using Brute Force and Backtracking


## Install the project and launch the application
### To install (once only)
- Open git bash where you want to install
- Type commands :
  - `git clone https://github.com/christian-aucane/Sudoku-Solver.git`
  - `cd Sudoku-Solver`
  - `source bash_scripts/install.bash`
### To launch the application (each time it is launched)
- Open git bash at project root
- Type command :
  - `source bash_scripts/run.bash`


## Files

### solvers/
#### base.py
##### BaseSudokuSolver
Base class for all solvers
##### BaseBruteforceSudokuSolver
Inherits from BaseSudokuSolver
Base class for solvers using the bruteforce method

#### backtracking.py
##### BacktrackingSudokuSolver
Inherits from BaseSudokuSolver
Solver using the backtracking method

#### bruteforce.py
##### BruteforceSudokuSolver
Inherits from BaseBruteforceSudokuSolver
Solver using the "classic" bruteforce method (tests all possible values from 1 to 9 in each cell)

#### bruteforce2.py
##### Bruteforce2SudokuSolver
Inherits from BaseBruteforceSudokuSolver
Improved bruteforce solver (tests only possible values for each cell)

### app.py (REQUIRES TO FIRST LAUNCH generate_grids.py)
Launch program

### utils.py
Contains all the code used in several other files
- Folder paths
- count_empty_cells(grid) -> Returns the number of life cells in the grid
- read_file(file_path) -> Reads a file and returns the grid
- get_solver_class(method) -> Returns the solver class corresponding to a method
- generate_grid(input_grid, num_empty_cells) -> Returns a copy of input_grid with num_empty_cells empty cells

### generate_grids.py
Generates grids for each solving method

### generate_stats.py (REQUIRES TO FIRST LAUNCH generate_grids.py)
Generates a JSON file containing the execution times of the different solving methods for different numbers of empty cells (same grid, with one additional cell removed each round).
#### Argument
- method (optionnel) -> Solving method to test

### generate_graphs.py (REQUIRES TO FIRST LAUNCH generate_stats.py)
Generates graphs for each solving method (uses matplotlib)

### show_graphs.py (REQUIRES TO FIRST LAUNCH generate_stats.py)
Displays interactive graphs for each solving method (uses plotly)
#### Argument
- method (optionnel) -> Solving method to display

### bash_scripts/
Contain bash scripts
#### install.bash
A script to install the project
#### run.bash
A script to launch app


## Analysis
The number of possible combinations increases exponentially with respect to the number of empty cells:

- 1 empty cell : 9^1 combinations
- 2 empty cells : 9^2 = 81 combinations
- 3 empty cells : 9^3 = 729 combinations
- 4 empty cells : 9^4 = 6561 combinations
- 5 empty cells : 9^5 = 95 049 combinations
- 6 empty cells : 9^6 = 531 441 combinations
- 7 empty cells : 9^7 = 4 782 969 combinations
- 8 empty cells : 9^8 = 43 046 721 combinations
- 9 empty cells : 9^9 = 387 420 489 combinations
- ...

### A reminder of the rules
![Image of a sudoku grid](img/sudoku_grid.png)

Each row, column, and 3 x 3 region must contain all the digits from 1 to 9 exactly once.

### Bruteforce
#### Explanation of the algorithm
An algorithm employing brute force systematically tries every possible solution until finding one that satisfies the problem constraints. In the case of Sudoku, it generates and tests all combinations of numbers in empty cells, checking each against the game's rules until a valid solution is discovered or all options are exhausted. This approach is straightforward but can be computationally intensive, especially for complex problems.

#### Graphic
![Curves of number of combinations and execution time versus number of empty cells](img/graphs/bruteforce.png)

### Backtracking
#### Explanation of the algorithm
Backtracking is a method to systematically explore all possible solutions to a problem, making it effective in Sudoku solving by ensuring game rules are followed. Cell by cell, each possibility is tested recursively, backtracking if a contradiction is found, until a solution is reached or all possibilities are exhausted. This efficient approach provides a practical solution for Sudoku enthusiasts.

#### Graphic
![Curves of number of combinations and execution time versus number of empty cells](img/graphs/backtracking.png)

### Bruteforce with value selection (bruteforce2)
#### Explanation of the algorithm
Similar to brute force, except instead of testing all values from 1 to 9 for each cell, it first calculates the possible values for each cell, i.e., those that do not violate the Sudoku rules, and then tests all combinations of possible values. The number of combinations depends on the grid. Indeed, depending on the position of the empty cells, there may not necessarily be the same number of combinations.

#### Graphic
![Curves of number of combinations and execution time versus number of empty cells](img/graphs/bruteforce2.png)

### Comparisons
![Execution time comparison curve between bruteforce and backtracking](img/graphs/bruteforce_backtracking.png)

![Execution time comparison curve between bruteforce and bruteforce2](img/graphs/bruteforce_bruteforce2.png)

![Execution time comparison curve between bracktrackin and bruteforce2](img/graphs/bruteforce2_backtracking.png)

In order, the fastest algorithm is backtracking, followed by bruteforce with value selection, and then by bruteforce.

- For **bruteforce**, the resolution time remains reasonable up to 8 empty cells (around 3 seconds).
- For **bruteforce with selection**, the resolution time remains reasonable between 30 and 35 empty cells (It depends on the grid).
- For **backtracking**, the resolution time remains very reasonable regardless of the number of empty cells (less than 1 second).

### Conclusion
To solve a standard grid, one should use backtracking.
