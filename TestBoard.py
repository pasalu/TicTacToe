from Board import *
from nose.tools import *

class TestBoard():
    def setup(self):
        self.board = Board()

    def test_new_board_expect_blank_board(self):
        assert_equal(self.board.board, self.board.BLANK_BOARD)

    def test_place_when_1_1_x_expect_1_1_x(self):
        self.board.place(1, 1, self.board.X)

        assert_equal(self.board.board[1][1], self.board.X)

    def test_place_when_0_0_x_expect_0_0_x(self):
        self.board.place(0, 0, self.board.X)

        assert_equal(self.board.board[0][0], self.board.X)

    def test_place_when_2_2_o_expect_2_2_o(self):
        self.board.place(2, 2, self.board.O)

        assert_equal(self.board.board[2][2], self.board.O)

    def test_place_when_negative_x_expect_false(self):
        result = self.board.place(-1, 1, self.board.X)

        assert_false(result)

    def test_place_when_negative_y_expect_false(self):
        result = self.board.place(1, -2, self.board.X)

        assert_false(result)

    def test_place_when_both_negative_expect_false(self):
        result = self.board.place(-4, -5, self.board.O)

        assert_false(result)

    def test_place_when_x_greater_than_2_expect_false(self):
        result = self.board.place(3, 0, self.board.X)

        assert_false(result)

    def test_place_when_y_greater_than_2_expect_false(self):
        result = self.board.place(1, 9, self.board.O)

        assert_false(result)

    def test_place_when_both_greater_than_2_expect_false(self):
        result = self.board.place(123412, 123419234, self.board.O)

        assert_false(result)

    def test_place_when_already_taken_expect_false(self):
        self.board.place(1, 2, self.board.O)

        result = self.board.place(1, 2, self.board.X)

        assert_false(result)

    def test_has_won_when_1_1_x_expect_false(self):
        self.board.place(1, 1, self.board.X)

        result = self.board.has_won(self.board.X)

        assert_false(result)

    def test_has_won_when_all_o_on_top_row_expect_true(self):
        self.board.place(0, 0, self.board.O)
        self.board.place(1, 0, self.board.O)
        self.board.place(2, 0, self.board.O)

        result = self.board.has_won(self.board.O)

        assert_true(result)

    def test_has_won_when_all_x_on_diagonal_expect_true(self):
        self.board.place(0, 0, self.board.X)
        self.board.place(1, 1, self.board.X)
        self.board.place(2, 2, self.board.X)

        result = self.board.has_won(self.board.X)

        assert_true(result)

    def test_when_modifying_board_blank_board_doesnt_change(self):
        COPY_OF_BLANK_BOARD = list(self.board.BLANK_BOARD)

        placed_successfully = self.board.place(1, 1, self.board.O)

        assert_true(placed_successfully)
        assert_equal(COPY_OF_BLANK_BOARD, self.board.BLANK_BOARD)
