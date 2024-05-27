from abc import ABC, abstractmethod
from app.colors import WHITE, BLACK
#nao estou a contabilizar comer peças
#1 - será que devia criar classes para o movimento das peças em vez de meter tudo numa class?
#2 - para além de checkar a questao do movimento é preciso checkar o movimentoa a comer a peça



class Piece:
    """
    Stores for each piece: 
    1 - board position
    2 - piece color (0 : "black" , 1 : "white") - instantiate in if no main game
    3 - moves available directions
    4 - moves intensity (0 : "can only move 1 box", 1 : "if it can move multiple")
    5 - piece points 
    """
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color 



class Pawn(Piece):

    def __init__(self, pos, color):
        
        super().__init__(pos, color)
        if self.color == WHITE:
            self.dir_moves = [[1,0]]
        elif self.color == BLACK:
            self.dir_moves = [[-1,0]]
            
        self.points = 1
        self.n_moves = 0
        

        
class Rook(Piece):
    
    def __init__(self, pos, color):
                
        super().__init__(pos, color)
        self.dir_moves = [[0,1],[0,-1],[1,0],[-1,0]]
        self.points = 4
        self.n_moves = 1
        

class Knight(Piece):
    
    def __init__(self, pos, color):
        
        super().__init__(pos, color)
        self.dir_moves = [[1,2],[-1,2],[-1,-2],[1,-2],[2,1],[-2,1],[-2,-1],[2,-1]]
        self.points = 3
        self.n_moves = 0

class Bishop(Piece):
    
    def __init__(self, pos, color):
        
        super().__init__(pos, color)
        self.dir_moves = [[1,1],[-1,-1],[-1,1],[1,-1]]
        self.points = 3
        self.n_moves = 1

class Queen(Piece):
        
    def __init__(self, pos, color):
        
        super().__init__(pos, color)
        self.dir_moves = [[1,1],[-1,-1],[-1,1],[1,-1],[0,1],[0,-1],[1,0],[-1,0]]
        self.points = 6
        self.n_moves = 1


class King(Piece):
        
    def __init__(self, pos, color):
        
        super().__init__(pos, color)
        self.dir_moves = [[1,1],[-1,-1],[-1,1],[1,-1],[0,1],[0,-1],[1,0],[-1,0]]
        self.n_moves = 0







if __name__ == '__main__':
    pawn = Pawn([0,0], WHITE)
    print(pawn.__class__.__name__)
    
     