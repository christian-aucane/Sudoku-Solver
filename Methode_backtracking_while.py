import pygame
import sys
import time

# Vérifie si un nombre peut être placé dans une certaine position du Sudoku
def is_valid_move(board, row, col, num):
    # Vérifie les lignes et les colonnes
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Vérifie le carré 3x3 contenant la position (row, col)
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Trouve la prochaine case vide dans le Sudoku
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Résout le Sudoku en utilisant une boucle while
def solve_sudoku(board):
    empty_location = find_empty_location(board)
    while empty_location:
        row, col = empty_location
        num = 1
        while num <= 9:
            if is_valid_move(board, row, col, num):
                board[row][col] = num
                if solve_sudoku(board):
                    return True
                board[row][col] = 0
            num += 1
        return False
    return True

# Affiche le Sudoku sur le terminal avec distinction des valeurs d'origine
def print_board(board, initial_board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                if initial_board[i][j] == 0:
                    print(board[i][j])
                else:
                    print("\033[1m" + str(board[i][j]) + "\033[0m")  # Met en gras les valeurs d'origine
            else:
                if initial_board[i][j] == 0:
                    print(board[i][j], end=" ")
                else:
                    print("\033[1m" + str(board[i][j]) + "\033[0m", end=" ")  # Met en gras les valeurs d'origine

# Exemple de grille Sudoku à résoudre (0 pour les cases vides)
board = [
    [0, 0, 9, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 1, 0],
    [0, 4, 5, 0, 1, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 8, 2, 0, 0],
    [0, 6, 1, 0, 3, 0, 0, 0, 5],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 7, 4, 2, 0, 0, 5, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7]
]

# Copie de la grille initiale pour l'affichage terminal
initial_board = [row[:] for row in board]

# Affiche la grille initiale sur le terminal
print("Sudoku à résoudre sur le terminal :")
print_board(board, initial_board)

# Résolution du Sudoku
start_time = time.time()
solve_sudoku(board)
end_time = time.time()
print("\nRésolution du Sudoku en", round(end_time - start_time, 5), "secondes.\n")

# Affiche la grille résolue sur le terminal avec distinction des valeurs d'origine
print("Grille résolue sur le terminal avec distinction des valeurs d'origine :")
print_board(board, initial_board)

# Affichage avec Pygame
pygame.init()
pygame.font.init()

# Paramètres de la fenêtre
WINDOW_SIZE = 540
CELL_SIZE = WINDOW_SIZE // 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont('Arial', 40)

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sudoku Solver")

# Fonction pour dessiner la grille
def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), 4)
            pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), 4)
        else:
            pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE))
            pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE))

# Fonction pour dessiner les chiffres
def draw_numbers():
    for i in range(9):
        for j in range(9):
            if initial_board[i][j] == 0:
                text = FONT.render(str(board[i][j]), True, BLACK)
                window.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))
            else:
                text = FONT.render(str(board[i][j]), True, BLUE)
                window.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))

# Boucle principale
# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(WHITE)
    draw_grid()
    draw_numbers()
    pygame.display.update()

pygame.quit()
sys.exit()

