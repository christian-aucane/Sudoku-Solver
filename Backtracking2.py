# Résout le Sudoku en utilisant une boucle while
def solve_sudoku(board):
    empty_location = find_empty_location(board)
    while empty_location:
        row, col = empty_location
        num = 1
        while num <= 9:
            if is_valid_move(board, row, col, num):
                board[row][col] = num
                if solve_sudoku(board):
                    return True
                board[row][col] = 0
            num += 1
        return False
    return True
