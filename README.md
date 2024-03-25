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
### interfaces/
#### cli.py
Gère l'affichage en ligne de commande
#### gui.py
Gère l'affichage avec interface graphique

Contient le code des interfaces CLI et GUI

### solvers/
#### base.py
##### BaseSudokuSolver
Classe de base pour tous les résolveurs
##### BaseBruteforceSudokuSolver
Hérite de BaseSudokuSolver
Classe de base pour les résolveurs utilisant la méthode bruteforce

#### mook.py
##### MookSudokuSolver
Hérite de BaseSudokuSolver
Mook pour tester les interfaces (remplie la grille de manière aléatoire)

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
  
### main.py
Lance le programme
#### Arguments
- file_name -> Nom du fichier contenant la grille SANS extrention (entre 1 et 5)
- method -> Methode de résolution (bruteforce, backtracking ou mook)
- interface -> Type d'interface (cli ou gui)
- --display -d -> Argument optionnel qui permet d'afficher les étapes de résolution en temps réel (fonctionne uniquement en CLI)

### generaate_grid.py
Génère une grille avec le nombre de cases maquantes passé en argument
Prend la grille contenue dans grids/input.txt et écrit le resultat dans grids/output.txt
### Argument
- num_empty_cases -> Nombre de cases vides que l'on veut dans la grille de sortie

### generate_stats.py
Génère un fichier JSON contenant les temps d'execution des différentes methodes de résolution pour différents nombres de cases vides (même grille ou on enlève une case suplémentaire a chaque tour)
### Argument
- method (optionnel) -> Méthode de résolution a tester

### plot_graphs.py (NECESSITE DE LANCER D'ABORD generate_stats.py)
Génère des graphiques pour chaque méthodes de résolution (utilise matplotlib)

### show_graphs.py (NECESSITE DE LANCER D'ABORD generate_stats.py)
Affiche des graphiues intéractifs pour chaque methode de resolution (utilise plotly)
### Argument
- method (optionnel) -> Méthode de résolution a afficher
