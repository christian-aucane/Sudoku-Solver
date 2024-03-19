import argparse
from pathlib import Path

GRIDS_PATH = Path(__file__).parent.parent / "grids"

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

def parse_args():
    """
    Parse command line arguments
    
    Returns
    -------
    args : argparse.Namespace
        command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    parser.add_argument('method', choices=["bruteforce", "backtrack", "mook"], default="bruteforce")
    parser.add_argument('interface', choices=["cli", "gui"], default="cli")
    args = parser.parse_args()

    return args

def main():
    
    args = parse_args()

    grid = read_file(GRIDS_PATH / (args.file_name + '.txt'))

    if args.method == 'bruteforce':
        from bruteforce import BruteForceSudokuSolver
        solver = BruteForceSudokuSolver(grid)
    elif args.method == 'backtrack':
        from backtrack import BacktrackSudokuSolver
        solver = BacktrackSudokuSolver(grid)
    elif args.method == 'mook':
        from solvers.mook import MookSudokuSolver
        solver = MookSudokuSolver(grid)

    if args.interface == 'cli':
        from interfaces.cli import main
    elif args.interface == 'gui':
        from interfaces.gui import main
    
    main(solver)
    

if __name__ == '__main__':
    main()
