
def drop_piece (board, column, piece): 
    board = piece 

def check_win(board):
    #GOING IN THE ROWS 
    for i in range(6):
        for j in range(8-3):
            if board[i][j] != " " and board[i][j] == board[i][j+1] and  board[i][j] == board[i][j+2] and  board[i][j] == board[i][j+3]:
                return board[i][j]
    #GOING IN THE COLUMNS 
    for i in range(6-3):
        for j in range(8):
            if board[i][j] != " " and board[i][j] == board[i+1][j] and  board[i][j] == board[i+2][j] and  board[i][j] == board[i+3][j]:
                return board[i][j]
    #GOING DIAGONAL UP TO THE RIGH 
    for i in range(6-3):
        for j in range(8-3):
            if board[i][j] != " " and board[i][j] == board[i+1][j+1] and  board[i][j] == board[i+2][j+2] and  board[i][j] == board[i+3][j+3]:
                return board[i][j]
    #GOING DIAGONAL DOWN AND LEFT 
    for i in range(6-3):
        for j in range(7, 2, -1):
            if board[i][j] != " " and board[i][j] == board[i+1][j-1] and  board[i][j] == board[i+2][j-2] and  board[i][j] == board[i+3][j-3]:
                return board[i][j]