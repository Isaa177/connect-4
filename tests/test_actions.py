from connect_four.board import create_new_board
from connect_four.actions import drop_piece

#BOARD GAME 
def test_drop_piece():
    board = create_new_board()
    drop_piece(board, 0, "X")
    assert board == [['','', '','','','','',''],
                    ['','', '','','','','',''],
                    ['','', '','','','','',''],
                    ['','', '','','','','',''],
                    ['','', '','','','','',''],
                    ['X','', '','','','','','']]
    

#CHECK WIN VERTICAL 
def test_check_win():
    board = [['','', '','','','','',''],
                    ['','', '','','','','',''],
                    ['X','', '','','','','',''],
                    ['X','', '','','','','',''],
                    ['X','', '','','','','',''],
                    ['X','', '','','','','','']]
    assert check_win(board)== "X"