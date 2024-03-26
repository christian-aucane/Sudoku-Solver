# Sudoku-Solver
A Sudoku Solver using Brute Force and Backtracking


## Fichiers

### solvers/
#### base.py
##### BaseSudokuSolver
Classe de base pour tous les résolveurs
##### BaseBruteforceSudokuSolver
Hérite de BaseSudokuSolver
Classe de base pour les résolveurs utilisant la méthode bruteforce

#### backtracking.py
##### BacktrackingSudokuSolver
Hérite de BaseSudokuSolver
Résolveur utilisant la méthode backtracking

#### bruteforce.py
##### BruteforceSudokuSolver
Hérite de BaseBruteforceSudokuSolver
Résolveur utilisant la méthode bruteforce "classique" (teste toute les valeurs possibles de 1 a 9 dans chaque case)

#### bruteforce2.py
##### Bruteforce2SudokuSolver
Hérite de BaseBruteforceSudokuSolver
Résolveur utilisant une méthode bruteforce améliorée (teste uniquement les valeurs possibles de chaque case)
  
### app.py (NECESSITE DE LANCER D'ABORD generate_grids.py)
Lance le programme

### utils.py
Contient tout le code qui est utilisé dans plusieurs autres fichiers
- Les chemins des dossiers
- count_empty_cells(grid) -> Retourne le nombre de cellules vies dans la grille
- read_file(file_path) -> Lit un fichier et retourne la grille
- get_solver_class(method) -> Retourne la classe de solver correspondant a une methode
- generate_grid(input_grid, num_empty_cells) -> Retourne une copie de input_grid avec num_empty_cells cases vides

### generate_grids.py
Génère des grilles pour chaque methode de resolution

### generate_stats.py (NECESSITE DE LANCER D'ABORD generate_grids.py)
Génère un fichier JSON contenant les temps d'execution des différentes methodes de résolution pour différents nombres de cases vides (même grille ou on enlève une case suplémentaire a chaque tour)
#### Argument
- method (optionnel) -> Méthode de résolution a tester

### generate_graphs.py (NECESSITE DE LANCER D'ABORD generate_stats.py)
Génère des graphiques pour chaque méthodes de résolution (utilise matplotlib)

### show_graphs.py (NECESSITE DE LANCER D'ABORD generate_stats.py)
Affiche des graphiues intéractifs pour chaque methode de resolution (utilise plotly)
#### Argument
- method (optionnel) -> Méthode de résolution a afficher
