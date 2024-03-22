from pathlib import Path
from importlib import import_module
from copy import deepcopy
from random import randint

BASE_DIR = Path(__file__).parent.parent
GRIDS_DIR = BASE_DIR / "grids"
STATS_DIR = BASE_DIR / "stats"
SOURCES_DIR = BASE_DIR / "src"
SOLVERS_DIR = SOURCES_DIR / "solvers"
SOLVERS_MODULES = [x.name[:-3] for x in SOLVERS_DIR.iterdir() if x.is_file() and x.name != "base.py" and x.name != "__init__.py"]

def read_file(file_path):
    """
    Read grid from file
    
    Parameters
    ----------
    file_path : str
        path of the file
    """
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            line = [int(x) if x != "_" else 0 for x in line.strip()]
            grid.append(line)
    return grid


def get_solver_class(method):
    solver_module = import_module(f"solvers.{method}")
    return getattr(solver_module, f"{method.capitalize()}SudokuSolver")


def generate_grid(input_grid, num_empty_cells):
    """
    Generate a grid with num_empty_cells empty cells

    Parameters
    ----------
    input_grid : list
        9x9 list of integers - Full grid without empty cells
    num_empty_cells : int
        number of empty cells

    Returns
    -------
    list
        9x9 list of integers with num_empty_cells empty cells
    """
    output_grid = deepcopy(input_grid)
    for _ in range(num_empty_cells):
        row = randint(0, 8)
        col = randint(0, 8)
        while True:
            if output_grid[row][col] == 0:
                
                row = randint(0, 8)
                col = randint(0, 8)
            else:
                output_grid[row][col] = 0
                break
    return output_grid
