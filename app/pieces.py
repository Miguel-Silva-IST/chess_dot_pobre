from enum import Enum
from abc import ABC, abstractmethod

#nao estou a contabilizar comer peças
#1 - será que devia criar classes para o movimento das peças em vez de meter tudo numa class?
#2 - para além de checkar a questao do movimento é preciso checkar o movimentoa a comer a peça



class LiestPieces(Enum):
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
    
    WP = 0
    WR = 1
    WK = 2
    WB = 3
    WQ = 4
    WKI = 5
    BP = 6
    BR = 7
    BK = 8
    BB = 9
    BQ = 10
    BKI = 11 



class Piece(ABC):
    def possible_moves(board : list, pos_i : list) -> list:
        #calculates list of possible moves
        pass
    


class Pawn(Piece):
    def possible_moves(board : list, pos_i : list) -> list:
        piece_moves = [[0,1]]
        pos_f = [pos_i + m for m in piece_moves]
        return [pos_f if not board[pos_f[0]][pos_f[1]]]
        
        
        

        
class Rook(Piece):
    def possible_moves(board : list, pos_i : list) -> list:
        pass

class Knight(Piece):
    def possible_moves(board : list, pos_i : list) -> list:
        pass

class Bishop(Piece):
    def possible_moves(board : list, pos_i : list) -> list:
        pass

class Queen(Piece):
    def possible_moves(board : list, pos_i : list) -> list:
        pass

class King(Piece):
    def possible_moves(board : list, pos_i : list) -> list:
        pass








if __name__ == '__main__':
     print(LiestPieces.__members__)