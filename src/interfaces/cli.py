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
            empty = bool(solver.original_grid[i][j])

            # Go to the line if you reach the end of the line
            printable_value = f"{value}\n" if j == 8 else f"{value} "

            # Values are printed in red if they are not in the original grid
            if empty:
                print(f"\033[31m{printable_value}\033[0m", end="")
            else:
                print(printable_value, end="")


def main(solver):
    """
    Main function

    Parameters
    ----------
    solver : BaseSudokuSolver child
        the sudoku solver
    """
    print("Welcome to Sudoku Solver!")
    start = time()
    solver.solve()
    end = time()
    print(f"Solved in {end - start} seconds")

    print_grid(solver)

    print("Thank you for using Sudoku Solver!")
    