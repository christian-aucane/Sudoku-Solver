import argparse

def read_file(file_name):
    grid = []
    with open(file_name, 'r') as f:
        for line in f:
            line = [int(x) if x != "_" else 0 for x in line.strip()]
            grid.append(line)
    return grid

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    parser.add_argument('method', choices=["bruteforce", "backtrack"], default="bruteforce")
    parser.add_argument('interface', choices=["cli", "gui"], default="cli")
    args = parser.parse_args()

    return args

def main():
    
    args = parse_args()

    grid = read_file("grids/" + args.file_name + '.txt')

    if args.method == 'bruteforce':
        from bruteforce import BruteForceSudokuSolver
        solver = BruteForceSudokuSolver(grid)
    elif args.method == 'backtrack':
        from backtrack import BacktrackSudokuSolver
        solver = BacktrackSudokuSolver(grid)

    if args.interface == 'cli':
        from cli import main
    elif args.interface == 'gui':
        from gui import main
    
    main(solver)
    

if __name__ == '__main__':
    main()
