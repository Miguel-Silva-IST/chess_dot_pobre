import unittest
from app.pieces import *
from app.board import *


class TestPieces(unittest.TestCase):
    def test_instantiate_white_rook(self):
        w_rook = -2
        piece_name = BoardMapping(w_rook).name
        w_rook_object = Rook([0,0],1) 
        
        self.assertEqual(piece_name, 'WR')
        self.assertEqual(w_rook_object.color, 1)
        


if __name__ == '__main__':
    unittest.main()
        
        