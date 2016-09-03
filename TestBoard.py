from Board import *

class TestBoard:
    def setup(self):
        self.board = Board()

    def test_new_board_expect_blank_board(self):
        assert self.board.board == [[]]
