from time import time

from base import MookSudokuSolver
from main import read_file



def print_grid(solver):
    grid_to_solve = solver.grid_to_solve
    grid_solved = solver.grid
    for i in range(len(grid_to_solve)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(grid_to_solve[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            value = str(grid_to_solve[i][j]) + "\n" if j == 8 else str(grid_to_solve[i][j]) + " "

            if value == "0 " or value == "0\n":
                value = str(grid_solved[i][j]) + "\n" if j == 8 else str(grid_solved[i][j]) + " "
                print(f"\033[31m{value}\033[0m", end="")  # Print in red
            else:
                print(value, end="")

def main(solver):
    print("Welcome to Sudoku Solver!")
    start = time()
    solver.solve()
    end = time()
    print("Solved in {} seconds".format(end - start))

    print_grid(solver)


if __name__ == '__main__':
    grid = read_file("grids/1.txt")
    solver = MookSudokuSolver(grid)
    main(solver)
