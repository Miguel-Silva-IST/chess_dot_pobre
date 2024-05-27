#movements checks
#1 each piece has x possible moves
#2 moves restricted by (a : obstacle pieces) & (b : board_boundaries)
#3 can eat piece if diff color
#4 check if after move king is on check - if yes then impossible move

#EXCEPTION - MOVEMENTS ARE OPOSIT IF WHITE/BLACK PIECES FOR SOME PIECES
#pieces that change move dir - pawn
from app.colors import WHITE, BLACK
from app.pieces import *
import copy



class PossibleMoves:
    """
    Checks all possible moves - for now excludes king check - see if implement here or separatly
    """
    
    def __init__(self, board, piece):
        self._board = board
        self._piece = piece
        
    
    def check_board_in_boundaries(self,pos):
        """
        Retusn 1 if in boundaries, 0 if out
        """
        
        if 0<=pos[0]<=7 and 0<=pos[1]<=7:
            return 1
        else:
            return 0
    
    
    #esta funcao podera ter que ser ajustada porque o que faz sentido é -> piece é instanciado e define-se logo a cor com base no numero. Nao faz sentido haver uma funcao so para ir buscar a cor da peca
    def get_piece_color(self, number):
        """
        Returns 1 if is white piece, and 0 if black
        """
        
        if number<0:
            return WHITE
        elif number>0:
            return BLACK
        else:
            raise ValueError('Value is not int')
    
    def get_board_square(self, pos):
        """Returns the value in the square"""
        
        return self._board[pos[0]][pos[1]]
        
        
    
    
    #iterates in all directions to get possible moves
    def check_possible_moves(self):
        pos_i = self._piece.pos
        self.possible_moves = []
        
        for dir in self._piece.dir_moves:
            pos_f = copy.copy(pos_i)
            while True:
                pos_f[0] += dir[0]
                pos_f[1] += dir[1]
                
                val_square = self.get_board_square(pos_f)                 
                
                #check board boundaries - if doesnt satisfy then jumps
                if not self.check_board_in_boundaries(pos_f):
                    break                    
                
                #check if empty square
                if not val_square:
                    self.possible_moves.append(pos_f)
                
                #in case not empty verifies if can eat - if yes then adds that pos, else breaks
                else: 
                    color_block = self.get_piece_color(val_square)
                    
                    #if blocking piece has diff color then can eat and add to pos
                    if self._piece.color != color_block:
                        self.possible_moves.append(pos_f)
                    
                    #in either case, since blocking piece is there, it stops moving
                    break      
                
                #if piece can only move one square breaks 
                if not self._piece.n_moves:
                    break
                
                        


class PawnMoves(PossibleMoves):    
    
    def check_diagonal_eat(self):
        """
        Checks for diagonal moves for eating enimy pieces and returns new possible moves
        """
        diag_moves = []
        
        #movements differ depending on side of board
        if self._piece.color == WHITE:
            diag_pos_r, diag_pos_l = [self._piece.pos[0]+1, self._piece.pos[1]+1], [self._piece.pos[0]+1, self._piece.pos[1]-1]
        elif self._piece.color == BLACK:
            diag_pos_r, diag_pos_l = [self._piece.pos[0]-1, self._piece.pos[1]+1], [self._piece.pos[0]-1, self._piece.pos[1]-1]
        
        #first checks if diag pos is in boundaries, then checks if there is piece to eat
        if self.check_board_in_boundaries(diag_pos_r):
            diag_piece_r = self.get_board_square(diag_pos_r)
            if diag_piece_r:
                diag_piece_r_color = self.get_piece_color(diag_piece_r)
                if diag_piece_r_color!= self._piece.color:
                    diag_moves.append(diag_pos_r)
        
        #first checks if diag pos is in boundaries, then checks if there is piece to eat
        if self.check_board_in_boundaries(diag_pos_l):
            diag_piece_l = self.get_board_square(diag_pos_l)
            if diag_piece_l:
                diag_piece_l_color = self.get_piece_color(diag_piece_l)
                if diag_piece_l_color!= self._piece.color:
                    diag_moves.append(diag_pos_l)
        
        return diag_moves
                
    
    
    def check_first_move(self):
        if self._piece.color == WHITE:
            begin_row = 1
            move = 2
        if self._piece.color == BLACK:
            begin_row = 6
            move = -2
        
        
        if self._piece.pos[0] == begin_row:
            second_row_pos = [self._piece.pos[0]+move, self._piece.pos[1]]
            #if no piece in second row then moves
            if not self.get_board_square(second_row_pos):
                return [second_row_pos]
            else:
                return []

        else:
            return []
    
    
    def check_en_passant(self):
        pass                    
        
    
    
    def check_possible_moves(self):
        
        super().check_possible_moves()
        
        diag_moves = self.check_diagonal_eat()
        first_pawn_moves = self.check_first_move()
        
        if diag_moves:
            self.possible_moves.extend(diag_moves)
        if first_pawn_moves:
            self.possible_moves.extend(first_pawn_moves)
                



class RookMoves(PossibleMoves):
    pass


class KnightMoves(PossibleMoves):
    pass


class BishopMoves(PossibleMoves):
    pass

class King(PossibleMoves):
    
    def check_rock_n_roll(self):
        pass
    
    def check_possible_moves(self):
        
        super().check_possible_moves()
        
        #add here extra possible move for rock n roll






class VerifyCheck:
    def __init__(self):
        pass



class UpdateBoard:
    pass




if __name__ == '__main__':
    pawn = Pawn([1,0],1)
    board1 = [[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, 1, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]]
    board2 = [[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [None, 1, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]]
    pawn_moves = PawnMoves(board2, pawn)
    pawn_moves.check_possible_moves()
    print(pawn_moves.possible_moves)