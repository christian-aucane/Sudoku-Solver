import sys
from time import time

import pygame

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen dimensions
WIDTH, HEIGHT = 540, 600

# Grid dimensions
CELL_SIZE = 40
GRID_WIDTH = CELL_SIZE * 9
GRID_HEIGHT = CELL_SIZE * 9
MARGIN_X = (WIDTH - GRID_WIDTH) // 2
MARGIN_Y = (HEIGHT - GRID_HEIGHT) // 2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


class Button:
    """
    Button class
    """
    def __init__(self, x, y, width, height, text, color):
        """
        Initialize the button
        
        Parameters
        ----------
        x : int
            x coordinate of the button
        y : int
            y coordinate of the button
        width : int
            width of the button
        height : int
            height of the button
        text : str
            text of the button
        color : tuple
            color of the button
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        """
        Draw the button on the screen
        
        Parameters
        ----------
        screen : pygame.Surface
            the screen to draw on
        """
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """
        
        Parameters
        ----------
        pos : tuple
            the position of the mouse
        """
        return self.rect.collidepoint(pos)


def draw_grid(solver, solved=False):
    """
    Draw the grid on the screen

    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
    solved : bool
        if the grid is solved
    """
    font = pygame.font.SysFont(None, 40)

    # Fill the grid with values
    for i in range(9):
        for j in range(9):
            if solver.original_grid[i][j] != 0:
                pygame.draw.rect(screen, WHITE, (MARGIN_X + j * CELL_SIZE, MARGIN_Y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                text = font.render(str(solver.original_grid[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(MARGIN_X + j * CELL_SIZE + CELL_SIZE // 2, MARGIN_Y + i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)
            elif solved and solver.grid[i][j] != 0:
                pygame.draw.rect(screen, WHITE, (MARGIN_X + j * CELL_SIZE, MARGIN_Y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                text = font.render(str(solver.grid[i][j]), True, RED)
                text_rect = text.get_rect(center=(MARGIN_X + j * CELL_SIZE + CELL_SIZE // 2, MARGIN_Y + i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)


    # Draw the grid
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, BLACK, (MARGIN_X + j * CELL_SIZE, MARGIN_Y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Draw the 3x3 blocks
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, GREY, (MARGIN_X + j * CELL_SIZE * 3, MARGIN_Y + i * CELL_SIZE * 3, CELL_SIZE * 3, CELL_SIZE * 3), 3)
    
    # Draw the border
    pygame.draw.rect(screen, GREY, (MARGIN_X, MARGIN_Y, GRID_WIDTH, GRID_HEIGHT), 10)


def update_screen(button, solver, finish, execution_time, grid_solved):
    """
    Update the screen

    Parameters
    ----------
    button : Button
        the button
    solver : BaseSudokuSolver child
        the sudoku solver
    finish : bool
        if the grid is finish
    execution_time : float
        the execution time
    """
    # Clear the screen
    screen.fill(WHITE)

    # Show title 'Sudoku Solver'
    font = pygame.font.SysFont(None, 50)
    text = font.render("Sudoku Solver", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text, text_rect)

    # Draw the grid
    draw_grid(solver, finish)

    font = pygame.font.SysFont(None, 30)

    # Show button or finish message with execution time
    if not finish:
        button.draw(screen)
    elif grid_solved:
        text = font.render(f"Solved in {execution_time} seconds", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 550))
        screen.blit(text, text_rect)
    else:
        text = font.render(f"No solution found in {execution_time} seconds", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 550))
        screen.blit(text, text_rect)
    pygame.display.flip()

def display(solver):
    """
    Display callback

    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
    """
    # TODO : debuger la fonction (Pourquoi ca ne s'affiche pas ?)
    print("Displaying grid")
    draw_grid(solver)
    pygame.display.flip()


def main(solver_class, grid, display_steps):
    """
    Main function

    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
    """
    display_callback = lambda solver: display(solver) if display_steps else lambda solver: None
    solver = solver_class(grid=grid, display_callback=display_callback)
    # Create the button
    button = Button(200, 500, 140, 50, "Solve", GREEN)

    # Initialize execution variables
    finish = False
    execution_time = 0
    grid_solved = False

    # Start the main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    if not finish:
                        # Change the button color and text
                        button.color = RED
                        button.text = "Solving ..."
                        update_screen(button, solver, finish, execution_time, grid_solved)

                        # Solve the grid
                        start = time()
                        grid_solved = solver.solve()
                        end = time()
                        execution_time = end - start
                        finish = True

        update_screen(button, solver, finish, execution_time, grid_solved)
