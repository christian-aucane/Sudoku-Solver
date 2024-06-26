"""
Sudoku Solver App

This module contains the main application for
solving Sudoku puzzles using Pygame.

It includes a class `Button` for creating interactive buttons,
and a `SudokuSolverApp` class for running the application.
"""
import sys
from time import time

import pygame

from utils import SOLVERS_MODULES, get_grid, get_solver_class, print_grid

# Colors
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


class Button:
    """
    Button class for creating interactive buttons on a Pygame screen.

    Args:
        screen (pygame.Surface): The screen to draw the button on.
        x (int): The x coordinate of the button.
        y (int): The y coordinate of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        text (str): The text displayed on the button.
        color (tuple): The color of the button.

    Attributes:
        rect (pygame.Rect): The rectangle representing the button.
        text (str): The text displayed on the button.
        color (tuple): The color of the button.
        screen (pygame.Surface): The screen to draw the button on.

    Methods:
        draw(): Draw the button on the screen.
        is_clicked(pos): Check if the button is clicked given a mouse position.
        set_color(color): Change the button color.
    """
    def __init__(self, screen, x, y, width, height, text, color):
        """
        Initialize the button

        Args:
            screen (pygame.Surface): the screen to draw on
            x (int): x coordinate of the button
            y (int): y coordinate of the button
            width (int): width of the button
            height (int): height of the button
            text (str): text of the button
            color (tuple): color of the button
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.screen = screen

    def draw(self):
        """
        Draw the button on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        font = pygame.font.SysFont("", 30)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """
        Check if the button is clicked given a mouse position

        Args:
            pos (tuple): the position of the mouse

        Returns:
            bool: True if the button is clicked, False otherwise
        """
        return self.rect.collidepoint(pos)

    def set_color(self, color):
        """
        Change the button color

        Args:
            color (tuple): the new color
        """
        self.color = color


class SudokuSolverApp:
    """
    Main application for solving Sudoku puzzles using Pygame.

    Attributes:
        screen (pygame.Surface): The Pygame screen surface.
        running (bool): Flag indicating if the application is running.
        method_selected (str): The solving method selected by the user.
        grid_selected (str): The Sudoku grid selected by the user.
        solver_class (class): The class of the selected Sudoku solver.
        grid (list): The Sudoku grid to be solved.

    Methods:
        draw_title(title): Draw the title on the screen.
        quit(): Quit the app.
        run(): Run the Sudoku solver application.
        select_method(): Select the solving method.
        select_grid(): Select the Sudoku grid to solve.
        solve_grid(): Solve the selected Sudoku grid.
        update_grid(button, solver, finish, execution_time, grid_solved):
            Update the screen display.
        draw_grid(solver, finish): Draw the Sudoku grid on the screen.
    """
    def __init__(self):
        """
        Initialize the app
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku Solver")
        self.running = True
        self.method_selected = ""
        self.grid_selected = ""
        self.solver_class = None
        self.grid = None

    def draw_title(self, title):
        """
        Draw the title on the screen

        Args:
            title (str): the title
        """
        font = pygame.font.SysFont("", 50)

        text = font.render(title, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 50))
        self.screen.blit(text, text_rect)

    def quit(self):
        """
        Quit the app
        """
        self.running = False
        pygame.quit()
        sys.exit()

    def run(self):
        """
        Run the app
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            self.select_method()

    def select_method(self):
        """
        Select the solving method
        """
        buttons = [
            Button(
                self.screen, 200, 150 + 50 * i + i * 10, 140, 50, method, GREEN
            ) for i, method in enumerate(SOLVERS_MODULES)
        ]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            self.method_selected = button.text
                            self.solver_class = get_solver_class(
                                self.method_selected
                            )
                            self.select_grid()

            self.screen.fill(WHITE)

            self.draw_title("Select Solving Method")

            for button in buttons:
                button.draw()

            pygame.display.update()

    def select_grid(self):
        """
        Select the Sudoku grid to solve
        """
        buttons = [
            Button(
                screen=self.screen,
                x=200, y=150 + 50 * (i-1) + i * 10,
                width=140, height=50,
                text=str(i), color=GREEN
            ) for i in range(1, 6)
        ]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_BACKSPACE:
                    self.select_method()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            self.grid_selected = button.text
                            self.grid = get_grid(
                                self.method_selected, self.grid_selected
                            )
                            self.solve_grid()
            self.screen.fill(WHITE)
            self.draw_title("Select Grid")
            for button in buttons:
                button.draw()
            pygame.display.update()

    def solve_grid(self):
        """
        Solve the selected Sudoku grid
        """
        solver = self.solver_class(self.grid)
        button = Button(self.screen, 200, 500, 140, 50, "Solve", GREEN)

        # Initialize execution variables
        finish = False
        execution_time = 0
        grid_solved = False

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_BACKSPACE:
                    self.select_grid()
                elif event.type == pygame.MOUSEBUTTONDOWN \
                        and not finish and button.is_clicked(event.pos):
                    # Change the button color and text
                    button.set_color(RED)
                    button.text = "Solving ..."
                    self.update_grid(
                        button, solver, finish, execution_time, grid_solved
                    )

                    # Solve the grid
                    start = time()
                    grid_solved = solver.solve()
                    end = time()
                    execution_time = end - start
                    finish = True
                    print_grid(solver)
                    print(f"Grid solved in {execution_time} seconds!")

            self.update_grid(
                button, solver, finish, execution_time, grid_solved
            )

    def update_grid(
        self, button, solver, finish, execution_time, grid_solved
    ):
        """
        Update the screen

        Args:
            button (Button): the button
            solver (BaseSudokuSolver child): the sudoku solver
            finish (bool): if the grid is finish
            execution_time (float): the execution time
            grid_solved (bool): if the grid is solved
        """
        # Clear the screen
        self.screen.fill(WHITE)

        self.draw_title(
            f"Solve grid {self.grid_selected} " +
            f"with {self.method_selected.capitalize()}"
        )

        # Draw the grid
        self.draw_grid(solver, finish)

        font = pygame.font.SysFont("", 30)

        # Show button or finish message with execution time
        if not finish:
            button.draw()
        elif grid_solved:
            text = font.render(
                f"Solved in {execution_time} seconds", True, BLACK
            )
            text_rect = text.get_rect(center=(WIDTH // 2, 550))
            self.screen.blit(text, text_rect)
        else:
            text = font.render(
                f"No solution found in {execution_time} seconds", True, BLACK
            )
            text_rect = text.get_rect(center=(WIDTH // 2, 550))
            self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw_grid(self, solver, solved=False):
        """
        Draw the grid on the screen

        Args:
            solver (BaseSudokuSolver child): the sudoku solver
            solved (bool): if the grid is solved
        """
        font = pygame.font.SysFont("", 40)

        # Fill the grid with values
        for i in range(9):
            for j in range(9):
                if solver.original_grid[i][j] != 0:
                    pygame.draw.rect(
                        self.screen, WHITE,
                        (
                            MARGIN_X + j * CELL_SIZE,
                            MARGIN_Y + i * CELL_SIZE,
                            CELL_SIZE, CELL_SIZE
                        )
                    )
                    text = font.render(
                        str(solver.original_grid[i][j]), True, BLACK
                    )
                    text_rect = text.get_rect(
                        center=(
                            MARGIN_X + j * CELL_SIZE + CELL_SIZE // 2,
                            MARGIN_Y + i * CELL_SIZE + CELL_SIZE // 2
                        )
                    )
                    self.screen.blit(text, text_rect)
                elif solved and solver.grid[i][j] != 0:
                    pygame.draw.rect(
                        self.screen, WHITE,
                        (
                            MARGIN_X + j * CELL_SIZE,
                            MARGIN_Y + i * CELL_SIZE,
                            CELL_SIZE, CELL_SIZE
                        )
                    )
                    text = font.render(
                        str(solver.grid[i][j]), True, RED
                    )
                    text_rect = text.get_rect(
                        center=(
                            MARGIN_X + j * CELL_SIZE + CELL_SIZE // 2,
                            MARGIN_Y + i * CELL_SIZE + CELL_SIZE // 2
                        )
                    )
                    self.screen.blit(text, text_rect)

        # Draw the grid
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(
                    self.screen, BLACK,
                    (
                        MARGIN_X + j * CELL_SIZE,
                        MARGIN_Y + i * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE
                    ),
                    1
                )

        # Draw the 3x3 blocks
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(
                    self.screen, GREY,
                    (
                        MARGIN_X + j * CELL_SIZE * 3,
                        MARGIN_Y + i * CELL_SIZE * 3,
                        CELL_SIZE * 3, CELL_SIZE * 3
                    ),
                    3
                )

        # Draw the border
        pygame.draw.rect(
            self.screen, GREY,
            (MARGIN_X, MARGIN_Y, GRID_WIDTH, GRID_HEIGHT),
            10
        )


def main():
    app = SudokuSolverApp()
    app.run()


if __name__ == "__main__":
    main()
