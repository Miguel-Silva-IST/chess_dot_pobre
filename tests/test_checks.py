import unittest
from app.moves import *
from app.board import *




class TestCheck(unittest.TestCase):
    count = 0
    
    def setUp(self) -> None:
        self.player = Player(WHITE)
        self.board1 = Board()
        self.board2 = Board([[None, -3, -4, -5, -6, -4, -3, -2], [None, None, None, None, None, None, None, None], [-2, None, None, None, None, None, None, None], [None, None, None, None, 2, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board3 = Board([[None, -3, -4, -5, -6, -4, -3, -2], [None, None, None, None, None, None, None, None], [-2, None, None, None, None, None, 4, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board4 = Board([[None, -3, -4, -5, -6, -4, -3, -2], [None, None, None, None, None, -1, None, None], [-2, None, None, None, None, None, 4, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board5 = Board([[None, -3, -4, -5, -6, -4, -3, -2], [None, None, None, None, None, -1, 3, None], [-2, None, None, None, None, None, 4, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])
        self.board6 = Board([[None, -3, -4, -5, -6, -4, -3, -2], [None, None, None, 1, None, -1, None, None], [-2, None, None, None, None, None, 4, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [1, None, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]])


        self.maxDiff = None
        
        if not TestCheck.count:
            print('Board1 : \n',self.board1)
            print('Board2 : \n',self.board2)
            print('Board3 : \n',self.board3)
            print('Board4 : \n',self.board4)
            print('Board5 : \n',self.board5)
            print('Board6 : \n',self.board6)
            #print('Board7 : \n',self.board7)
            #print('Board8 : \n',self.board8)
            #print('Board9 : \n',self.board9)
        TestCheck.count+=1

    
    def test_initial_board_king_not_in_check(self):
        verify_check = VerifyCheck(self.board1, self.player)
        result = verify_check.verify_check()
        self.assertEqual(result,0)
    

    def test_king_in_check_by_rook(self):
        verify_check = VerifyCheck(self.board2, self.player)
        result = verify_check.verify_check()
        self.assertEqual(result,1)
    

    def test_king_in_check_by_bishop(self):
        verify_check = VerifyCheck(self.board3, self.player)
        result = verify_check.verify_check()
        self.assertEqual(result,1)


    def test_king_not_in_check_because_covered_by_pawn(self):
        verify_check = VerifyCheck(self.board4, self.player)
        result = verify_check.verify_check()
        self.assertEqual(result,0)

    
    def test_king_in_check_by_knight(self):
        verify_check = VerifyCheck(self.board5, self.player)
        result = verify_check.verify_check()
        self.assertEqual(result,1)
    

    def test_king_in_check_by_pawn(self):
        verify_check = VerifyCheck(self.board6, self.player)
        result = verify_check.verify_check()
        self.assertEqual(result,1)


        
    
