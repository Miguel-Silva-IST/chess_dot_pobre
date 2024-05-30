import unittest
from app.moves import *



class TestMoves(unittest.TestCase):
    count = 0
    
    def setUp(self) -> None:
        self.board1 = Board()
        self.board2 = Board([[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, None, -1], [None, 1, None, 1, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, -1, None, -1, None], [1, None, 1, None, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board3 = Board([[None, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [-2, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]]) 
        self.board4 = Board([[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [-2, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board5 = Board([[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [None, None, None, None, None, None, None, None], [None, None, None, -2, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board6 = Board([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, -3, None, None, None, None], [None, None, None, None, None, None, None, None], [None, -3, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, -1, None, None, None, None, None]])
        self.board7 = Board([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, -4, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, -4, None, None, None, None, None, None], [1, None, -1, None, None, None, None, None]])
        self.board8 = Board([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, -5, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, -5, None, None, None, None, None, None], [1, None, -1, None, None, None, None, None]])
        self.board9 = Board([[None, None, -1, None, None, None, None, None], [None, -1, -6, -1, None, None, None, None], [None, None, -1, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]])
        
        self.maxDiff = None
        
        if not TestMoves.count:
            print('Board1 : \n',self.board1)
            print('Board2 : \n',self.board2)
            print('Board3 : \n',self.board3)
            print('Board4 : \n',self.board4)
            print('Board5 : \n',self.board5)
            print('Board6 : \n',self.board6)
            print('Board7 : \n',self.board7)
            print('Board8 : \n',self.board8)
            print('Board9 : \n',self.board9)
        TestMoves.count+=1
        
        
    def test_possible_moves_pawn(self):
        
        pawn1 = self.board1.get_board_piece([1,0])
        pawn2 = self.board2.get_board_piece([1,0])
        pawn3 = self.board1.get_board_piece([6,0])
        pawn4 = self.board1.get_board_piece([1,2])
        pawn5 = self.board2.get_board_piece([6,5])
        pawn6 = self.board2.get_board_piece([1,1])
        
        #Tests pawn normal movement - 1 front, 2 front
        pawn_moves1 = PawnMoves(self.board1, pawn1)
        pawn_moves1.check_possible_moves()
        self.assertCountEqual(pawn_moves1.possible_moves, [[2,0],[3,0]])

        #Tests pawn in second row can move 1 front, 2 front, diag right enemy pawn 
        pawn_moves2 = PawnMoves(self.board2, pawn2)
        pawn_moves2.check_possible_moves()
        self.assertCountEqual(pawn_moves2.possible_moves, [[2,0],[3,0],[2,1]])

        #Tests black pawn movement backwards - move 1 back, moves 2 back
        pawn_moves3 = PawnMoves(self.board1, pawn3)
        pawn_moves3.check_possible_moves()
        self.assertCountEqual(pawn_moves3.possible_moves, [[5,0],[4,0]])
        
        
        #Tests pawn in second row can move 1 front, 2 front, diag left enemy pawn, diag right enemy pawn
        pawn_moves4 = PawnMoves(self.board2, pawn4)
        pawn_moves4.check_possible_moves()
        self.assertCountEqual(pawn_moves4.possible_moves, [[2,2],[3,2],[2,1],[2,3]])
        
        
        #Tests black pawn can move 1 back, 2 back, diag left back enemy pawn, diag right back enemy pawn
        pawn_moves5 = PawnMoves(self.board2, pawn5)
        pawn_moves5.check_possible_moves()
        self.assertCountEqual(pawn_moves5.possible_moves, [[5, 5], [5, 6], [5, 4], [4, 5]])
        
        
        #Tests blocked pawn cant move anywhere
        pawn_moves6 = PawnMoves(self.board2, pawn6)
        pawn_moves6.check_possible_moves()
        self.assertCountEqual(pawn_moves6.possible_moves, [])
        
        
        
        
        
        
    def test_possible_moves_rook(self):
        rook1 = self.board3.get_board_piece([2,0]) 
        rook2 = self.board4.get_board_piece([0,0]) 
        rook3 = self.board5.get_board_piece([3,3]) 
        
        #Tests can move to the right untill reaches wall and to the front untill reaches enemy piece
        rook_moves1 = RookMoves(self.board3, rook1)
        rook_moves1.check_possible_moves()
        self.assertCountEqual(rook_moves1.possible_moves, [[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[3,0],[4,0],[5,0],[6,0]])
        
        #Tests cant move anywhere since is blocked by same color pieces
        rook_moves2 = RookMoves(self.board4, rook2)
        rook_moves2.check_possible_moves()
        self.assertCountEqual(rook_moves2.possible_moves, [])
        
        #Tests rook in the middle of the board can move in 4 dir
        rook_moves3 = RookMoves(self.board5,rook3)
        rook_moves3.check_possible_moves()
        self.assertCountEqual(rook_moves3.possible_moves, [[3, 4], [3, 5], [3, 6], [3, 7], [3, 2], [3, 1], [3, 0], [4, 3], [5, 3], [6, 3], [2, 3]])
    
    
    
    def test_possible_moves_knight(self):
        knight1 = self.board3.get_board_piece([0,1]) 
        knight2 = self.board6.get_board_piece([3,3])
        knight3 = self.board6.get_board_piece([5,1])
        
        #Only can move front/right
        knight_moves1 = KnightMoves(self.board3, knight1)
        knight_moves1.check_possible_moves()
        self.assertCountEqual(knight_moves1.possible_moves, [[2,2]])
        
        #Tests can move anywhere, so expects 8 moves
        knight_moves2 = KnightMoves(self.board6, knight2)
        knight_moves2.check_possible_moves()
        self.assertCountEqual(knight_moves2.possible_moves, [[4, 5],[2, 5],[2, 1],[4, 1],[5, 4],[1, 4],[1, 2],[5, 2]])
        
        #Tests can move anywhere, except for 3 moves: 2 out of boundaries and 1 cant eat own piece - so expects 5 moves
        knight_moves3 = KnightMoves(self.board6, knight3)
        knight_moves3.check_possible_moves()
        self.assertCountEqual(knight_moves3.possible_moves, [[6, 3],[4, 3],[3, 2],[3, 0],[7, 0]])
    
    
    
    def test_possible_moves_bishop(self):
        bishop1 = self.board3.get_board_piece([0,2]) 
        bishop2 = self.board7.get_board_piece([3,3])
        bishop3 = self.board7.get_board_piece([6,1])
        
        #Only can move front/right
        bishop_moves1 = BishopMoves(self.board3, bishop1)
        bishop_moves1.check_possible_moves()
        self.assertCountEqual(bishop_moves1.possible_moves, [])
        
        #Tests can move anywhere, so expects 8 moves
        bishop_moves2 = BishopMoves(self.board7, bishop2)
        bishop_moves2.check_possible_moves()
        self.assertCountEqual(bishop_moves2.possible_moves, [[0, 0],[1, 1],[2, 2],[4, 4],[5, 5],[6, 6],[7, 7], [4,2], [2,4], [1,5], [0,6], [5,1], [6,0]])
        
        #Tests can move anywhere, except for 3 moves: 2 out of boundaries and 1 cant eat own piece - so expects 5 moves
        bishop_moves3 = BishopMoves(self.board7, bishop3)
        bishop_moves3.check_possible_moves()
        self.assertCountEqual(bishop_moves3.possible_moves, [[7, 0], [5,0], [5, 2],[4, 3],[3, 4],[2, 5], [1,6], [0,7]])    
    
    
    def test_possible_moves_queen(self):
        queen1 = self.board1.get_board_piece([0,3]) 
        queen2 = self.board8.get_board_piece([3,3])
        queen3 = self.board8.get_board_piece([6,1])
    
        
        #Cant move anywhere
        queen_moves1 = QueenMoves(self.board3, queen1)
        queen_moves1.check_possible_moves()
        self.assertCountEqual(queen_moves1.possible_moves, [])
        
        #Tests can move anywhere
        queen_moves2 = QueenMoves(self.board8, queen2)
        queen_moves2.check_possible_moves()
        self.assertCountEqual(queen_moves2.possible_moves, [[0, 0],[1, 1],[2, 2],[4, 4],[5, 5],[6, 6],[7, 7],
                                                            [4,2], [2,4], [1,5], [0,6], [5,1], [6,0], [4,3], 
                                                            [5,3], [6,3], [7,3], [2,3], [1,3], [0,3], [3,2], 
                                                            [3,1], [3,0], [3,4],[3,5], [3,6], [3,7] ])
        
        #Tests can move anywhere, except for 3 moves: 2 out of boundaries and 1 cant eat own piece - so expects 5 moves
        queen_moves3 = QueenMoves(self.board8, queen3)
        queen_moves3.check_possible_moves()
        self.assertCountEqual(queen_moves3.possible_moves, [[7, 0], [5,0], [5, 2],[4, 3],[3, 4],[2, 5], [1,6],
                                                            [0,7], [7,1], [5,1], [4,1], [3,1], [2,1], [1,1],
                                                            [0,1], [6,0], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7]]) 
    
    def test_possible_moves_king(self):
        king1 = self.board1.get_board_piece([0,4])
        king2 =  self.board9.get_board_piece([1,2])

        #Cant move anywhere
        king_moves1 = KingMoves(self.board3, king1)
        king_moves1.check_possible_moves()
        self.assertCountEqual(king_moves1.possible_moves, [])

        #Cant only move diagonal
        king_moves2 = KingMoves(self.board9, king2)
        king_moves2.check_possible_moves()
        self.assertCountEqual(king_moves2.possible_moves, [[2,3], [0,1], [2,1], [0,3]])
    
    
    def test_select_wrong_piece(self):
        
        empty_square = self.board1.get_board_piece([3,0])
        
        self.assertIsNone(empty_square)
        
                        
 
        
        



if __name__ == '__main__':
    unittest.main()
    
    
    
