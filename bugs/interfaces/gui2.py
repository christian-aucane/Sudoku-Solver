import sys
import pygame

from utils import SOLVERS_MODULES


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


WIDTH, HEIGHT = 540, 600

GRIDS_NAMES = [str(i) for i in range(1, 6)]


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

def choose_grid(screen, events, grids, method_name):
    """
    Backtracking grids

    Parameters
    ----------
    screen : pygame.Surface
        the screen to draw on
    """
    buttons = [] # TODO : ajouter les boutons

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_clicked(event.pos):
                    return f"solve_{method_name}_{button.text}"

    font = pygame.font.SysFont(None, 50)

    text = font.render(method_name.capitalize(), True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text, text_rect)

    pygame.display.update()
    return f"{method_name}_grids"


def main_menu(screen, events):
    """
    Main menu

    Parameters
    ----------
    screen : pygame.Surface
        the screen to draw on
    """
    buttons = [Button(screen, 200, 150 + 50 * SOLVERS_MODULES.index(method), 140, 50, method, GREEN) for method in SOLVERS_MODULES]
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_clicked(event.pos):
                    return f"{button.text}_grids"

    font = pygame.font.SysFont(None, 50)

    text = font.render("Sudoku Solver", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text, text_rect)

    for button in buttons:
        button.draw()

    pygame.display.update()
    return "main"

def show_screen(events, screen_name):
    """
    Show the screen

    Parameters
    ----------
    screen_name : str
        the name of the screen
    """
    screen.fill(WHITE)
    if "solve" in screen_name:
        _, method_name, grid_name = screen_name.split("_")
        return solve(method_name, grid_name)
        
    pygame.display.update()
    return screen_name

def main(*args, **kwargs):
    """
    Main function

    Parameters
    ----------
    solver_class : BaseSudokuSolver child
        the sudoku solver class
    grid : list
        9x9 list of integers
    display_steps : bool
        whether to display the steps
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")

    current_screen = "main"

    screens = {
        "main": lambda events: main_menu(screen, events),
        "backtracking_grids": lambda events: choose_grid(screen, events, BACKTRACKING_GRIDS, "Backtracking"),
    }
    
    while True:
        screen.fill(WHITE)
        events = pygame.event.get()
        current_screen = screens[current_screen](events=events)

        
if __name__ == "__main__":
    main()