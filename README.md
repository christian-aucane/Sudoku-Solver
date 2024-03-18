# Sudoku-Solver
A Sudoku Solver using Brute Force and Backtracking

## TODO
- Modéliser la grille avec les contraintes -> classe parente BaseSudokuSolver
- classe BruteForceSudokuSolver -> Hérite de SudokuSolver
- classe BacktrackingSudokuSolver -> Hérite de SudokuSolver
- fichier main qui prend en parametre un nom de fichier de grille, une methode de résolution et affiche dans le terminal et dans une fenetre pygame le resultat

### Découpage du code
#### base.py
##### BaseSudokuSolver

###### attributs
- grille d'origine
- grille en cours
- position
  
###### methodes
- résoudre (abstraite) -> retourne la grille résolue (implémenter dans la classe fille, spécifique a la methode de resolution)

- se déplacer -> change la position pour la prochaine case vide

- trouver ligne
- trouver colonne
- trouver zone
  
- verifier ligne
- vérifier colonne
- vérifier zone

- verifier grille complète
  
