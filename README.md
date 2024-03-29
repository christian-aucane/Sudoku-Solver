# Sudoku-Solver
A Sudoku Solver using Brute Force and Backtracking


## Install the project and launch the application
### To install (once only)
- Open git bash where you want to install
- Type commands :
  - `git clone https://github.com/christian-aucane/Sudoku-Solver.git`
  - `cd Sudoku-Solver`
  - `source bash_scripts/init.bash`
### To launch the application (each time it is launched)
- Open git bash at project root
- Type command :
  - `source bash_scripts/run.bash`


## TODO

### Section Analyse dans le README
- Nombre de combinaisons exponentielle OK
- calcul du nombre de combinaisons selon le nombre de case vide OK
- Calcul de la complexité algorithmique
- comparaison des algos
- graphiques
- ...? 

### Autre methode de resolution
- calculer valeurs possibles de chaque case
- dans les cases ou une seule posibilité mettre la valeur
- recalculer
- est-ce que ca marche ?
- si non trouver que faire des valeurs possibles


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

## Analyse
Le nombre de combinaisons possibles augmente de manière exponentiel par rapport au nombre de cases vides
- 1 case : 9 combinaisons
- 2 cases : 9^2 = 81 combinaisons
- 3 cases : 9^3 = 729 combinaisons
- 4 cases : 9^4 = 6561 combinaison
- 5 cases : 9^5 = 95 049 combinaison
- 6 cases : 9^6 = 531 441 combinaison
- 7 cases : 9^7 = 4 782 969 combinaison
- 8 cases : 9^8 = 43 046 721 combinaison
- 9 cases : 9^9 = 387 420 489 combinaison
- ...


### Bruteforce
![Courbes du nombre de combinaison et du temps d'execution par rapport au nombre de cases vides](img/bruteforce.png)

### Backtracking
![Courbes du nombre de combinaison et du temps d'execution par rapport au nombre de cases vides](img/backtracking.png)

### Bruteforce 2
![Courbes du nombre de combinaison et du temps d'execution par rapport au nombre de cases vides](img/bruteforce2.png)
