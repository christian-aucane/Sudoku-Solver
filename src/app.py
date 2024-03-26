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
    Button class
    """
    def __init__(self, screen, x, y, width, height, text, color):
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
        self.screen = screen

    def draw(self):
        """
        Draw the button on the screen
        
        Parameters
        ----------
        screen : pygame.Surface
            the screen to draw on
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """
        
        Parameters
        ----------
        pos : tuple
            the position of the mouse
        """
        return self.rect.collidepoint(pos)


class SudokuSolverApp:
    def __init__(self):
        """
        Initialize the app
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.method_selected = ""
        self.grid_selected = ""
        self.solver_class = None
        self.grid = None
    
    def draw_title(self, title):
        """
        Draw the title on the screen
        
        Parameters
        ----------
        title : str
            the title to draw
        """
        font = pygame.font.SysFont(None, 50)

        text = font.render(title, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 50))
        self.screen.blit(text, text_rect)

    def run(self):
        """
        Run the app
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.select_method()

        pygame.quit()
        sys.exit()

    def select_method(self):
        """
        Select the solving method
        """
        buttons = [
            Button(self.screen, 200, 150 + 50 * i + i * 10, 140, 50, method, GREEN) for i, method in enumerate(SOLVERS_MODULES)
        ]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            self.method_selected = button.text
                            self.solver_class = get_solver_class(self.method_selected)
                            self.select_grid()
                
            self.screen.fill(WHITE)

            self.draw_title("Select Solving Method")

            for button in buttons:
                button.draw()

            pygame.display.update()

    def select_grid(self):

        buttons = [
            Button(self.screen, 200, 150 + 50 * (i-1) + i * 10, 140, 50, str(i), GREEN) for i in range(1, 6)
        ]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.select_method()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            self.grid_selected = button.text
                            self.grid = get_grid(self.method_selected, self.grid_selected)
                            self.solve_grid()
            self.screen.fill(WHITE)
            self.draw_title("Select Grid")
            for button in buttons:
                button.draw()
            pygame.display.update()
    
    def solve_grid(self):
        solver = self.solver_class(self.grid)
        button = Button(self.screen, 200, 500, 140, 50, "Solve", GREEN)

        # Initialize execution variables
        finish = False
        execution_time = 0
        grid_solved = False

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.select_grid()
                elif event.type == pygame.MOUSEBUTTONDOWN and button.is_clicked(event.pos):
                    if not finish:
                        # Change the button color and text
                        button.color = RED
                        button.text = "Solving ..."
                        self.update_grid(button, solver, finish, execution_time, grid_solved)

                        # Solve the grid
                        start = time()
                        grid_solved = solver.solve()
                        end = time()
                        execution_time = end - start
                        finish = True
                        print_grid(solver)
                        print(f"Runtime: {execution_time} seconds")

            self.update_grid(button, solver, finish, execution_time, grid_solved)

    def update_grid(self, button, solver, finish, execution_time, grid_solved):
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
        self.screen.fill(WHITE)

        self.draw_title(f"Solve grid {self.grid_selected} with {self.method_selected.capitalize()}")

        # Draw the grid
        self.draw_grid(solver, finish)

        font = pygame.font.SysFont(None, 30)

        # Show button or finish message with execution time
        if not finish:
            button.draw()
        elif grid_solved:
            text = font.render(f"Solved in {execution_time} seconds", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, 550))
            self.screen.blit(text, text_rect)
        else:
            text = font.render(f"No solution found in {execution_time} seconds", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, 550))
            self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw_grid(self, solver, solved=False):
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
                    pygame.draw.rect(self.screen, WHITE, (MARGIN_X + j * CELL_SIZE, MARGIN_Y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    text = font.render(str(solver.original_grid[i][j]), True, BLACK)
                    text_rect = text.get_rect(center=(MARGIN_X + j * CELL_SIZE + CELL_SIZE // 2, MARGIN_Y + i * CELL_SIZE + CELL_SIZE // 2))
                    self.screen.blit(text, text_rect)
                elif solved and solver.grid[i][j] != 0:
                    pygame.draw.rect(self.screen, WHITE, (MARGIN_X + j * CELL_SIZE, MARGIN_Y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    text = font.render(str(solver.grid[i][j]), True, RED)
                    text_rect = text.get_rect(center=(MARGIN_X + j * CELL_SIZE + CELL_SIZE // 2, MARGIN_Y + i * CELL_SIZE + CELL_SIZE // 2))
                    self.screen.blit(text, text_rect)

        # Draw the grid
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(self.screen, BLACK, (MARGIN_X + j * CELL_SIZE, MARGIN_Y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        # Draw the 3x3 blocks
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.screen, GREY, (MARGIN_X + j * CELL_SIZE * 3, MARGIN_Y + i * CELL_SIZE * 3, CELL_SIZE * 3, CELL_SIZE * 3), 3)
        
        # Draw the border
        pygame.draw.rect(self.screen, GREY, (MARGIN_X, MARGIN_Y, GRID_WIDTH, GRID_HEIGHT), 10)


def main():
    app = SudokuSolverApp()
    app.run()


if __name__ == "__main__":
    main()
