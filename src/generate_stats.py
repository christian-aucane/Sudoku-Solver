from copy import deepcopy
import json
from time import time
import argparse

from generate_grids import generate_grid
from utils import STATS_DIR, GRIDS_DIR, get_grid, get_solver_class, read_file


TESTING = {
    'bruteforce': lambda input_grid: resolution_method(input_grid=input_grid, method_name='bruteforce', max_empty_cells=8),
    'bruteforce2': lambda input_grid: resolution_method(input_grid=input_grid, method_name='bruteforce2', max_empty_cells=35),
    'backtracking': lambda input_grid: resolution_method(input_grid=input_grid, method_name='backtracking', max_empty_cells=81),
}


def parse_args():
    """
    Parse command line arguments
    
    Returns:
        argparse.Namespace: command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("method", nargs="?", default=None, help="Resolution method")
    return parser.parse_args()


def test_solver(grid, solver_class):
    """
    Test the solver
    
    Args:
        grid (list): 9x9 list of integers

    Returns:
        tuple: number of combinations and execution time
    """
    solver = solver_class(grid)
    start = time()
    solver.solve()
    end = time()
    return solver.n_combinations, end - start


def test_method(input_grid, method_name, max_empty_cells):
    """
    Test the method

    Args:
        input_grid (list): 9x9 list of integers
        method_name (str): Name of the method
        max_empty_cells (int): Maximum number of empty cells

    Returns:
        dict: Dictionary with the results
    """
    print(f"Testing {method_name}")

    solver_class = get_solver_class(method_name)

    results = {}
    grid = deepcopy(input_grid)
    for num_empty_cells in range(1, max_empty_cells + 1):
        print(f"Empty cells: {num_empty_cells} / {max_empty_cells}")
        grid = generate_grid(grid, num_empty_cells)
        
        n_combinations, execution_time = test_solver(grid, solver_class)

        print(f"Execution Time: {execution_time}")

        results[num_empty_cells] = {
            'n_combinations': n_combinations,
            'execution_time': execution_time
        }
        
    return results


def resolution_method(input_grid, method_name, max_empty_cells):
    """
    Test the resolution method and save the results in a JSON file

    Args:
        input_grid (list): 9x9 list of integers
        method_name (str): Name of the method
        max_empty_cells (int): Maximum number of empty cells

    Returns:
        dict: Dictionary with the results
    """
    results = test_method(
        input_grid=input_grid, method_name=method_name, 
        max_empty_cells=max_empty_cells
    )
    with open(STATS_DIR / f"{method_name}.json", "w") as f:
        json.dump(results, f, indent=4)

    return results


def main():
    """
    Main function
    """
    args = parse_args()

    STATS_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with open(STATS_DIR / "execution_times.json", "r") as f:
            results = json.load(f)
    except FileNotFoundError:
        results = {}

    input_grid = get_grid("solved", 1)
    
    if args.method is not None:
        results[args.method] = TESTING[args.method](input_grid)
    else:
        for method, test in TESTING.items():
            results[method] = test(input_grid)

    with open(STATS_DIR / "execution_times.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Done!")


if __name__ == '__main__':
    main()
