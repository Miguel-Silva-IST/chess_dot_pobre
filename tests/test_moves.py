import unittest
from app.moves import *
from app.board import *
from app.pieces import *


class TestMoves(unittest.TestCase):
    
    def setUp(self) -> None:
        self.board1 = [[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, 1, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]]
        self.board2 = [[-2, -3, -4, -5, -6, -4, -3, -2], [-1, -1, -1, -1, -1, -1, -1, -1], [None, 1, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]] 
    
    def test_possible_moves_pawn(self):
        pawn = Pawn([1,0],1)
        pawn_moves1 = PawnMoves(self.board1, pawn)
        pawn_moves1.check_possible_moves()
        self.assertCountEqual(pawn_moves1.possible_moves, [[2,0],[3,0]])

        pawn_moves2 = PawnMoves(self.board2, pawn)
        pawn_moves2.check_possible_moves()
        self.assertCountEqual(pawn_moves2.possible_moves, [[2,0],[3,0],[2,1]])




if __name__ == '__main__':
    unittest.main()