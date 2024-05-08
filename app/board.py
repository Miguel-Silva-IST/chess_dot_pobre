    #1-initializes the board positions
    #2-each position represented by either - P-pawn, K - knight , B -bishop, R - rook, Q-queen, KI-king 
    #3 - does it make scense to do one class per piece???
    #choose identifier of white and black




class Board:

    def __init__(self):
        self.board = [[None for c in range(8)] for r in range(8)]
        for c in range(8):
            self.board[1][c] = 'WP'
            self.board[6][c] = 'BP'
        
        self.board[0][0],self.board[0][7],self.board[7][0],self.board[7][7] = 'WR','WR','BR','BR'
        self.board[0][1],self.board[0][6],self.board[7][1],self.board[7][6] = 'WK','WK','BK','BK'
        self.board[0][2],self.board[0][5],self.board[7][2],self.board[7][5] = 'WB','WB','BB','BB'
        self.board[0][3], self.board[7][3] = 'WQ','BQ'
        self.board[0][4], self.board[7][4] = 'WKI','BKI'

    
    def __repr__(self):
        board_str = ''
        for row in self.board:
            board_str+=f'{row}\n'
        
        return board_str
            





if __name__ == '__main__':
    
    board = Board()
    print(board)