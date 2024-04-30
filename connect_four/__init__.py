from .board import *
from .actions import *


def create_new_board():
    return[[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
    
def print_board(board):
    for row in board:
        print (".join(map(str, row")

def is_valid_location(board,col):
    return board[ROW_COUNT - 1][col]== 0
    
def get_next_open_row(board, col):
    for r in range (ROW_COUNT):
        if board[r][col] == 0:
            return r
        

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):

    for r in range(ROW_COUNT):
        for c in range (COLUMN_COUNT - 3):
            if board [r][c + 1] == piece and board[r][c + 3 ] == piece:
                return True
            
