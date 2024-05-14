#DEFINE CONSTANTS 
ROW_COUNT = 6
COLUMN_COUNT = 8

def create_new_board (): 
    board= [[" ", " ", " ", " ", " ", " "," ", " "], 
            [" ", " ", " ", " ", " ", " "," ", " "], 
            [" ", " ", " ", " ", " ", " "," ", " "], 
            [" ", " ", " ", " ", " ", " "," ", " "], 
            [" ", " ", " ", " ", " ", " "," ", " "], 
            [" ", " ", " ", " ", " ", " "," ", " "]]
#PRINTING BOARD GAME CONNECT 4 
    return board 
def print_board (board): 
    print (
        f""" 
{board [0][0]} | {board [0][1]} | {board [0][2]} | {board [0][3]} | {board [0][4]} | {board [0][5]} | {board [0][6]} | {board [0][7]} 
---------------------------
{board [1][0]} | {board [1][1]} | {board [1][2]} | {board [1][3]} | {board [1][4]} | {board [1][5]} | {board [1][6]} | {board [1][7]}
---------------------------
{board [2][0]} | {board [2][1]} | {board [2][2]} | {board [2][3]} | {board [2][4]} | {board [2][5]} | {board [2][6]} | {board [2][7]} 
---------------------------
{board [3][0]} | {board [3][1]} | {board [3][2]} | {board [3][3]} | {board [3][4]} | {board [3][5]} | {board [3][6]} | {board [3][7]}
---------------------------
{board [4][0]} | {board [4][1]} | {board [4][2]} | {board [4][3]} | {board [4][4]} | {board [4][5]} | {board [4][6]} | {board [4][7]}
---------------------------
{board [5][0]} | {board [5][1]} | {board [5][2]} | {board [5][3]} | {board [5][4]} | {board [5][5]} | {board [5][6]} | {board [5][7]}
"""
    )
def get_next_open_row(board, col):
    for r in range (ROW_COUNT-1, -1, -1):
        if board[r][col] == " ":
            return r
        

def drop_piece(board, row, col, piece):
    board[row][col] = piece