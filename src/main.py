"""
Main module

This module contains the main function

Arguments
---------

file_name : str
    name of the file containing the grid withpout the extension
method : str
    method to solve the sudoku (bruteforce, backtracking, mook)
interface : str
    interface to use (cli, gui)
--display -d : bool
    display the fill steps
"""
import argparse
import importlib
from pathlib import Path

from utils import GRIDS_DIR, SOLVERS_MODULES, read_file


def parse_args():
    """
    Parse command line arguments
    
    Returns
    -------
    args : argparse.Namespace
        command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file_name', choices=[x.name[:-4] for x in GRIDS_DIR.iterdir()], 
        help='name of the file containing the grid withpout the extension'
    )
    parser.add_argument(
        'method', choices=SOLVERS_MODULES,
        help="method to solve the sudoku"
    )
    parser.add_argument(
        'interface', choices=["cli", "gui"],
        help="type of interface"
    )
    parser.add_argument(
        '--display', '-d', action='store_true', 
        help="display the fill steps"
    )
    return parser.parse_args()

def main():
    """
    Main function
    """
    args = parse_args()

    grid = read_file(GRIDS_DIR / (args.file_name + '.txt'))

    # Import the solver class
    solver_module = importlib.import_module(f"solvers.{args.method}")
    solver_class = getattr(solver_module, f"{args.method.capitalize()}SudokuSolver")

    # Import the interface main function
    main = importlib.import_module(f"interfaces.{args.interface}").main
    main(solver_class, grid, args.display)


if __name__ == '__main__':
    main()
