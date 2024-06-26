from pathlib import Path
from importlib import import_module


BASE_DIR = Path(__file__).parent.parent
ORIGINAL_GRIDS_DIR = BASE_DIR / "original_grids"
GRIDS_DIR = BASE_DIR / "grids"
STATS_DIR = BASE_DIR / "stats"
GRAPHS_DIR = STATS_DIR / "graphs"

SOURCES_DIR = BASE_DIR / "src"
SOLVERS_DIR = SOURCES_DIR / "solvers"
SOLVERS_MODULES = [
    x.name[:-3] for x in SOLVERS_DIR.iterdir()
    if x.is_file() and x.name != "base.py" and x.name != "__init__.py"
]


def count_empty_cells(grid):
    """
    Get count empty cells

    Args:
        grid (list): 9x9 list of integers
    Returns:
        int: count empty cells
    """
    return sum(x == 0 for row in grid for x in row)


def read_file(file_path):
    """
    Read grid from file

    Args:
        file_path (str): path of the file
    Returns:
        list: 9x9 list of integers
    """
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            line = [int(x) if x != "_" else 0 for x in line.strip()]
            grid.append(line)
    return grid


def get_solver_class(method):
    """
    Get solver class

    Args:
        method (str): name of the method

    Returns:
        class: solver class
    """
    solver_module = import_module(f"solvers.{method}")
    return getattr(solver_module, f"{method.capitalize()}SudokuSolver")


def get_grid(method, grid):
    """
    Get grid

    Args:
        method (str): name of the method
        grid (str): name of the grid without extention

    Returns:
        list: 9x9 list of integers
    """
    grid = read_file(GRIDS_DIR / method / f"{grid}.txt")
    return grid


def print_grid(solver):
    """
    Print the grid in terminal

    Args:
        solver (BaseSudokuSolver child): the sudoku solver
    """
    for i in range(len(solver.original_grid)):
        # Print dashes to separate 3x3 blocks
        if i % 3 == 0 and i != 0:
            print("-"*23)
        for j in range(len(solver.original_grid[0])):
            # Print dashes to separate 3x3 blocks
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # Value is from the original grid if it is not empty
            value = solver.original_grid[i][j]\
                if solver.original_grid[i][j] != 0\
                else solver.grid[i][j]
            if value == 0:
                value = " "
            empty = not bool(solver.original_grid[i][j])

            # Go to the line if you reach the end of the line
            printable_value = f"{value}\n" if j == 8 else f"{value} "

            # Values are printed in red if they are not in the original grid
            if empty:
                print(f"\033[31m{printable_value}\033[0m", end="")
            else:
                print(printable_value, end="")
