import random
import copy

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

def sudoku_solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if sudoku_solver(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def has_unique_solution(board):
    temp_board = copy.deepcopy(board)
    return sudoku_solver(temp_board)

def create_puzzle(board, num_clues = 30):
    # start with a full board and remove numbers
    puzzle = copy.deepcopy(board)
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)

    while len(cells) > 81 - num_clues:
        row, col = cells.pop()
        removed_value = puzzle[row][col]
        puzzle[row][col] = 0

        # check if the puzzle still has a unique solution
        if not has_unique_solution(puzzle):
            puzzle[row][col] = removed_value # restore

    return puzzle

# complete_board = generate_complete_sudoku()
# for row in complete_board:
#     print(row)

