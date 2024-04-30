
def drop_piece (board, column, piece): 
    board = piece 

def check_win(board):
    for i in range(n_rows):
        for j in range(n_cols-3):
            if board[i][j] == board[i][j+1] and  board[i][j] == board[i][j+2] and  board[i][j] == board[i][j+3]:
                return board[i][j]