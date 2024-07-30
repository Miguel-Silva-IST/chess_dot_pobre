"""Module with multiple distinct classes and functions that are used across the code"""

from app.colors import BLACK, WHITE
from app.board import *
import copy

def check_board_in_boundaries(board,pos):
    """
    Retusn 1 if in boundaries, 0 if out
    """
    
    if 0<=pos[0]<len(board.board) and 0<=pos[1]<len(board.board):
        return 1
    else:
        return 0



def find_king(player, board):
    """Returns king value"""
    
    if player.color == WHITE:
        king_val = BoardMapping['WKI'].value
    elif player.color == BLACK:
        king_val == BoardMapping['BKI'].value
    
    
    board_state = board.board
    board_size = len(board_state)
    
    for r in range(board_size):
        for c in range(board_size):
            if board_state[r][c] == king_val:
                king_pos = [r,c]
                break
    
    return board.get_board_piece(king_pos)
            


def verify_piece_in_line_king(piece, king):
    """
    Function used to avoid verify unecessary checks. Returns 1 if in line
    """
    
    #verify rows, cols, diag
    if piece.pos[0] == king.pos[0]:
        return 1
    elif piece.pos[1] == king.pos[1]:
        return 1
    elif abs(piece.pos[0] - king.pos[0])/abs(piece.pos[1]-king.pos[1]) == 1:
        return 1
    else:
        return 0 
    
    