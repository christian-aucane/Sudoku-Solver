from copy import deepcopy
import json
from time import time

from utils import STATS_DIR, GRIDS_DIR, generate_grid, get_solver_class, read_file


def test_solver(grid, solver_class):
    solver = solver_class(grid)
    start = time()
    solver.solve()
    end = time()
    return end - start


def test_method(input_grid, method_name, max_empty_cells, n_iterations, step=1):
    print(f"Testing {method_name}")

    solver_class = get_solver_class(method_name)

    results = {}
    grid = deepcopy(input_grid)
    for num_empty_cells in range(1, max_empty_cells + 1, step):
        print("Empty cells:", num_empty_cells)
        grid = generate_grid(grid, num_empty_cells)
        total_time = 0
        for i in range(n_iterations):
                print(f"Iteration: {i + 1} / {n_iterations}")
                execution_time = test_solver(grid, solver_class)
                total_time += execution_time
                print(f"Time: {execution_time}")

        results[num_empty_cells] = total_time / n_iterations
        
    return results


def main():
    input_grid = read_file(GRIDS_DIR / "input.txt")

    results_bruteforce = test_method(
        input_grid=input_grid, method_name='bruteforce', 
        max_empty_cells=8, n_iterations=3
    )
    with open(STATS_DIR / "bruteforce.json", "w") as f:
        json.dump(results_bruteforce, f, indent=4)

    results_bruteforce2 = test_method(
        input_grid=input_grid, method_name='bruteforce2', 
        max_empty_cells=51, n_iterations=10
    )

    with open(STATS_DIR / "bruteforce2.json", "w") as f:
        json.dump(results_bruteforce2, f, indent=4)

    results_backtracking = test_method(
        input_grid=input_grid, method_name='backtracking', 
        max_empty_cells=81, n_iterations=100
    )

    with open(STATS_DIR / "backtracking.json", "w") as f:
        json.dump(results_backtracking, f, indent=4)

    results = {
        'bruteforce': results_bruteforce, 
        'bruteforce2': results_bruteforce2, 
        'backtracking': results_backtracking
    }

    STATS_DIR.mkdir(parents=True, exist_ok=True)

    with open(STATS_DIR / "execution_times.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Done!")

if __name__ == '__main__':
    main()
