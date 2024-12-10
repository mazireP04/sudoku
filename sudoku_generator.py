import random

def is_valid(board, row, col, num):
    '''Check if it is valid to put the num at a particular position '''

    # check if it doesn't clash with its row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # check if it doesn't clash with its column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # check if it doesn't clash with its cell
    start_row, start_col = 3 * (row // 3 ), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def fill_grid(board):
    ''' fill the grid with valid numbers '''

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # shuffle numbers to randomize the board
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_grid(board):
                            return True
                        board[row][col] = 0 # backtrack
                return False
    return True

def generate_complete_sudoku():
    ''' generates the entirely filled sudoku board'''
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(board)
    return board