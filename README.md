# Sudoku-Solver
A Sudoku Solver using Brute Force and Backtracking

## TODO
- classe BruteForceSudokuSolver -> Hérite de SudokuSolver
- classe BacktrackingSudokuSolver -> Hérite de SudokuSolver
- fichier main qui prend en parametre un nom de fichier de grille, une methode de résolution et affiche dans le terminal et dans une fenetre pygame le resultat

## BaseSudokuSolver
### attributs
- grille d'origine
- grille à résoudre
- position

### methodes
- solve (abstraite) -> retourne la grille résolue (implémenter dans la classe fille, spécifique a la methode de resolution)
- reset -> Restaure la grille a son état d'origine
- is_valid -> Vérifie si une valeur est valide pour une case
- find_empty_cell -> Trouve la prochaine cellule vide

## Fichiers
### interfaces (un fichier par interface)
Contient le code des interfaces CLI et GUI

### solvers (un fichier par classe)
Contient les classes des solvers BaseSudokuSolver, MookSudokuSolver, BruteforceSudokuSolver, BacktrackingSudokuSolver

### main.py
Lance le programme
#### Arguments
- file_name -> Nom du fichier contenant la grille SANS extrention (entre 1 et 5)
- method -> Methode de résolution (bruteforce, backtracking ou mook)
- interface -> Type d'interface (cli ou gui)
- --display -d -> Argument optionnel qui permet d'afficher les étapes de résolution en temps réel (fonctionne uniquement en CLI)
