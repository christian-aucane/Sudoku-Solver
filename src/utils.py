import importlib
from pathlib import Path


GRIDS_DIR = Path(__file__).parent.parent / "grids"
SOLVERS_DIR = Path(__file__).parent / "solvers"
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
    solver_module = importlib.import_module(f"solvers.{method}")
    return getattr(solver_module, f"{method.capitalize()}SudokuSolver")
