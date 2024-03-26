import argparse
from copy import deepcopy
from random import randint

from utils import ORIGINAL_GRIDS_DIR, get_solver_class, get_grid, GRIDS_DIR, count_empty_cells, read_file


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
    while count_empty_cells(output_grid) < num_empty_cells:
        row = randint(0, 8)
        col = randint(0, 8)
        if output_grid[row][col] == 0:
            continue
        output_grid[row][col] = 0
    return output_grid


def solve_grids():
    output_dir = GRIDS_DIR / "solved"
    solver_class = get_solver_class("backtracking")
    output_dir.mkdir(parents=True, exist_ok=True)
    for i in range(1, 6):
        grid = read_file(ORIGINAL_GRIDS_DIR / f"{i}.txt")
        solver = solver_class(grid)
        solver.solve()
        write_grid_in_file(solver.grid, output_dir / f"{i}.txt")

def write_grid_in_file(grid, file_path):
    with open(file_path, "w") as f:
        for row in grid:
            f.write("".join([str(x) if x != 0 else "_" for x in row]) + "\n")

def main():

    GRIDS_DIR.mkdir(parents=True, exist_ok=True)
    print("Solving grids...")
    
    solve_grids()

    print("Generating grids...")
    bruteforce_dir = GRIDS_DIR / "bruteforce"
    bruteforce2_dir = GRIDS_DIR / "bruteforce2"
    backtracking_dir = GRIDS_DIR / "backtracking"
    bruteforce_dir.mkdir(parents=True, exist_ok=True)
    bruteforce2_dir.mkdir(parents=True, exist_ok=True)
    backtracking_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1, 6):
        input_grid = get_grid("solved", i)
        bruteforce_output_grid = generate_grid(input_grid, 6)
        write_grid_in_file(bruteforce_output_grid, bruteforce_dir / f"{i}.txt")

        bruteforce2_output_grid = generate_grid(input_grid, 30)
        write_grid_in_file(bruteforce2_output_grid, bruteforce2_dir / f"{i}.txt")

        backtracking_grid = read_file(ORIGINAL_GRIDS_DIR / f"{i}.txt")
        write_grid_in_file(backtracking_grid, backtracking_dir / f"{i}.txt")
    
    print("Done!")

if __name__ == "__main__":
    main()
