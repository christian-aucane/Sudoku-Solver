from copy import deepcopy
import time


from ..utils import read_file


class BruteForceSolve:
    def __init__(self, grid):
        self.original_grid = grid
        self.grid = deepcopy(grid)

    def print_grid(self):  
        for x in range(9):  
            if x % 3 == 0 and x != 0:   
                print ("- - - - - - - - - - -") 
            for y in range(9):  
                if y % 3 == 0 and y != 0:  
                    print("|", end=" ")
                if y == 8: 
                    print(self.grid[x][y])  
                else: 
                    print(self.grid[x][y], end=" ")

    def find_empty_cell(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    return x, y
        return None, None

    def create_list(self):
        empty_cells = []
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    empty_cells.append((x, y))
        return empty_cells
    
    def create_counter(self, num_empty_cells):
        counter = 0
        max_value = 10 ** num_empty_cells - 1
        while counter <= max_value:
            counter_str = str(counter).zfill(num_empty_cells)
            print(counter_str)
            counter += 1
    
    def replace_value(self, old_value, new_value):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == old_value:
                    self.grid[x][y] = new_value

    def is_valid(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num or self.grid[col][x] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for x in range(3):
            for y in range(3):
                if self.grid[x + start_row][y + start_col] == num:
                    return False
        return True
    
    def add_value(self, empty_cells):
        num_empty_cells = len(empty_cells)
        for i in range(num_empty_cells):
            row, col = empty_cells[i]
            num = self.grid[row][col] + 1
            if num == 10:
                num = 1
            self.grid[row][col] = num
            if self.is_valid(row,col, num):
                break

    def solve(self):
        print("Solving Sudoku...")
        empty_cells = self.create_list()
        if not empty_cells:
            print("Sudoku solved")
            return True

        num_empty_cells = len(empty_cells)
        counter = [1] * num_empty_cells

        while True:
            # Fill the grid with the current combination
            for i in range(num_empty_cells):
                row, col = empty_cells[i]
                self.grid[row][col] = counter[i]

            # Print current combination
            print("Current combination:", counter)

            # Check if the current combination is valid
            valid = True
            for row, col in empty_cells:
                if not self.is_valid(row, col, self.grid[row][col]):
                    valid = False
                    break

            # If the combination is valid, we found the solution
            if valid:
                print("Sudoku solved")
                return True

            # Increment the counter
            index = 0
            while index < num_empty_cells:
                counter[index] += 1
                if counter[index] <= 9:
                    break
                else:
                    counter[index] = 1
                    index += 1
                    if index == num_empty_cells:
                        break

        # If we reach 1 again, we tried all combinations
            if counter == [1] * num_empty_cells:
                break
    
        return False


if __name__ == "__main__":
    start_time = time.time() 


    brute_solver = BruteForceSolve(read_file('grids/output.txt'))
    brute_solver.solve()


    print("The Sudoku is solved.")
    brute_solver.print_grid()

    end_time = time.time()

    execution_time = end_time - start_time
    print("Execution time: ", execution_time, " seconds")
