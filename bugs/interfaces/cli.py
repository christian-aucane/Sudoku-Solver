from time import time


def print_grid(solver):
    """
    Print the grid
    
    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
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
            value = solver.original_grid[i][j] if solver.original_grid[i][j] != 0 else solver.grid[i][j]
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

def display(solver):
    """
    Display callback

    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
    """
    print()
    print_grid(solver)
    input()

def main(solver_class, grid, display_steps):
    """
    Main function

    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
    """
    display_callback = lambda solver: display(solver) if display_steps else lambda solver: None
    solver = solver_class(grid=grid, display_callback=display_callback)
    print("Welcome to Sudoku Solver!")
    start = time()
    grid_solved = solver.solve()
    end = time()
    execution_time = end - start
    
    print_grid(solver)
    
    if grid_solved:
        print(f"Solved in {execution_time} seconds")
    else:
        print(f"No solution found in {execution_time} seconds")

    print("Thank you for using Sudoku Solver!")
    