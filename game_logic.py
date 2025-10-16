import random

def new_game(n=4):
    board = [[0]*n for _ in range(n)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty = [(i,j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == 0]
    if not empty:
        return
    i, j = random.choice(empty)
    board[i][j] = random.choice([2, 4])

def compress(board):
    new_board = []
    for i in range(len(board)):
        new_row = [num for num in board[i] if num != 0]
        new_row += [0]*(len(board)-len(new_row))
        new_board.append(new_row)
    return new_board

def merge(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board)-1):
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j+1] = 0
                score += board[i][j]
    return board, score

def reverse(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_left(board):
    board = compress(board)
    board, score = merge(board)
    board = compress(board)
    return board, score

def move_right(board):
    board = reverse(board)
    board, score = move_left(board)
    board = reverse(board)
    return board, score

def move_up(board):
    board = transpose(board)
    board, score = move_left(board)
    board = transpose(board)
    return board, score

def move_down(board):
    board = transpose(board)
    board, score = move_right(board)
    board = transpose(board)
    return board, score

def game_over(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return False
            if i < len(board)-1 and board[i][j] == board[i+1][j]:
                return False
            if j < len(board)-1 and board[i][j] == board[i][j+1]:
                return False
    return True
