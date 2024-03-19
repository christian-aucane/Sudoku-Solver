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
- move_next -> change la position pour la prochaine case vide
- fill_current_cell -> Remplie la case actuele avec la valeur passée en paramètre
- verify_set_of_values -> Vérifie que les valeurs de l'ensemble passée en paramètre sont uniques ou des vides

### propriétés
- line -> Renvoie une liste contenant les valeurs de la ligne actuelle
- column -> Revoie une liste contenant les valeurs de la colonne actuelle
- block -> Renvoie une liste contenant les valeurs du block 3x3 actuel
- is_valid -> Vérifie que la case actuelle n'entre pas en conflit avec la ligne, la colonne et le block 3x3

## Fichiers
### interfaces (un fichier par interface)
Contient le code des interfaces CLI et GUI

### solvers (un fichier par classe)
Contient les classes des solvers BaseSudokuSolver, MookSudokuSolver

### main.py
Lance le programme
Prend en parametre DANS L'ORDRE le nom du fichier (entre 1 et 5) sans extention, une methode (bruteforce, backtracking ou mook) et un type d'interface (cli ou gui)
