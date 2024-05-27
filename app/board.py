#As standard reference, white rook is located at pos [0,0]


from enum import Enum

class BoardMapping(Enum):
    """
    ex. WK - white knight
    
    1st char:
    W - white
    B - black
    
    2nd char:
    P - pawn
    R - rook
    K - knight
    B - bishop
    Q - queen
    KI - king
    """
    
    WP = -1
    WR = -2
    WK = -3
    WB = -4
    WQ = -5
    WKI = -6
    BP = 1
    BR = 2
    BK = 3
    BB = 4
    BQ = 5
    BKI = 6



class Board:

    def __init__(self):
        self.board = [[None for c in range(8)] for r in range(8)]
        for c in range(8):
            self.board[1][c] = -1
            self.board[6][c] = 1
        
        self.board[0][0],self.board[0][7],self.board[7][0],self.board[7][7] = -2,-2,2,2
        self.board[0][1],self.board[0][6],self.board[7][1],self.board[7][6] = -3,-3,3,3
        self.board[0][2],self.board[0][5],self.board[7][2],self.board[7][5] = -4,-4,4,4
        self.board[0][3], self.board[7][3] = -5,5
        self.board[0][4], self.board[7][4] = -6,6

    
    def __repr__(self):
        board_str = '' 
        for row in self.board:
            aux_board_row = list(map(lambda x: None if x is None else BoardMapping(x).name, row))
            board_str+=f'{aux_board_row}\n'
        
        return board_str
            





if __name__ == '__main__':
    
    board = Board()
    print(board)