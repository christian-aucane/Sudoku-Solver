import sys
from time import time

from base import MookSudokuSolver
from main import read_file

import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 540, 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


# Classe pour le bouton
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_grid(solver, solved=False):
    grid_to_solve = solver.grid_to_solve
    grid_solved = solver.grid

    cell_size = 40
    grid_width = cell_size * 9
    grid_height = cell_size * 9
    margin_x = (WIDTH - grid_width) // 2
    margin_y = (HEIGHT - grid_height) // 2

    # Remplir la grille
    for i in range(9):
        for j in range(9):
            if grid_to_solve[i][j] != 0:
                pygame.draw.rect(screen, WHITE, (margin_x + j * cell_size, margin_y + i * cell_size, cell_size, cell_size))
                font = pygame.font.SysFont(None, 40)
                text = font.render(str(grid_to_solve[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(margin_x + j * cell_size + cell_size // 2, margin_y + i * cell_size + cell_size // 2))
                screen.blit(text, text_rect)
            elif solved:
                pygame.draw.rect(screen, WHITE, (margin_x + j * cell_size, margin_y + i * cell_size, cell_size, cell_size))
                font = pygame.font.SysFont(None, 40)
                text = font.render(str(grid_solved[i][j]), True, RED)
                text_rect = text.get_rect(center=(margin_x + j * cell_size + cell_size // 2, margin_y + i * cell_size + cell_size // 2))
                screen.blit(text, text_rect)


    # Dessiner la grille
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, BLACK, (margin_x + j * cell_size, margin_y + i * cell_size, cell_size, cell_size), 1)

    # Dessiner les blocs
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, GREY, (margin_x + j * cell_size * 3, margin_y + i * cell_size * 3, cell_size * 3, cell_size * 3), 3)
    
    # Dessiner le contours
    pygame.draw.rect(screen, GREY, (margin_x, margin_y, grid_width, grid_height), 10)

def main(solver):
    # Création du bouton
    button = Button(200, 500, 140, 50, "Solve", GREEN)

    # Initialisation des variables
    solved = False
    execution_time = None

    # Début de la boucle principale
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    if not solved:
                        print("Button clicked!")  # Action à exécuter lorsque le bouton est cliqué
                        start = time()
                        solver.solve()
                        end = time()
                        execution_time = end - start
                        print(f"Solved in {execution_time} seconds")
                        solved = True


        screen.fill(WHITE)

        # Afficher le titre 'Sudoku Solver'
        font = pygame.font.SysFont(None, 50)
        text = font.render("Sudoku Solver", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(text, text_rect)

        # Afficher la grille
        draw_grid(solver, solved)

        # Affichage du bouton ou du temps d'execution
        if not solved:
            button.draw(screen)
        else:
            font = pygame.font.SysFont(None, 30)
            text = font.render(f"Solved in {execution_time} seconds", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, 550))
            screen.blit(text, text_rect)
        pygame.display.update()

if __name__ == '__main__':
    grid = read_file("grids/1.txt")
    solver = MookSudokuSolver(grid)
    main(solver)
