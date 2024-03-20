from random import randint
import argparse


from utils import GRIDS_DIR, read_file

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("num_empty_cases", type=int)
    return parser.parse_args()

def main():
    
    args = parse_args()
    grid = read_file(GRIDS_DIR / "input.txt")

    for _ in range(args.num_empty_cases):
        row = randint(0, 8)
        col = randint(0, 8)
        while True:
            if grid[row][col] == 0:
                
                row = randint(0, 8)
                col = randint(0, 8)
            else:
                grid[row][col] = 0
                break

        print("Empty cell: ", row, col)
    
    print(*grid, sep="\n")
    with open(GRIDS_DIR / "output.txt", "w") as f:
        for row in grid:
            f.write("".join([str(x) if x != 0 else "_" for x in row]) + "\n")

    print("Done!")

if __name__ == "__main__":
    main()
