"""Module with multiple distinct classes and functions that are used across the code"""

from app.colors import BLACK, WHITE



def check_board_in_boundaries(board,pos):
    """
    Retusn 1 if in boundaries, 0 if out
    """
    
    if 0<=pos[0]<len(board.board) and 0<=pos[1]<len(board.board):
        return 1
    else:
        return 0