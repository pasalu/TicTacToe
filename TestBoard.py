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

    def test_place_when_current_player_won_expect_false(self):
        self.board.place(0, 0, self.board.O)
        self.board.place(1, 0, self.board.O)
        self.board.place(2, 0, self.board.O)
        current_player_has_won = self.board.has_won(self.board.O)

        result = self.board.place(1, 1, self.board.X)

        assert_true(current_player_has_won, "Current player lost")
        assert_false(result, "Place returned true after player won")

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

    def test_switch_current_player_player_switches(self):
        old_current_player = self.board.player

        self.board.switch_current_player()
        new_current_player = self.board.player

        assert_not_equal(old_current_player, new_current_player)

    def test_is_tie_when_blank_board_expect_false(self):
        result = self.board.is_tie()

        assert_false(result)

    def test_is_tie_when_full_board_expect_true(self):
        self.fill_board()

        result = self.board.is_tie()

        assert_true(result)

    def test_is_tie_when_x_won_expect_false(self):
        self.board.place(1, 1, self.board.X)
        self.board.place(0, 1, self.board.O)
        self.board.place(2, 0, self.board.X)
        self.board.place(2, 2, self.board.O)
        self.board.place(0, 2, self.board.X)

        result = self.board.is_tie()

        assert_false(result)

    def test_reset_expect_blank_board(self):
        self.board.place(1, 1, self.board.X)
        self.board.place(1, 0, self.board.O)
        self.board.place(2, 2, self.board.X)
        self.board.reset()

        assert_equal(self.board.board, self.board.BLANK_BOARD)

    def test_reset_expect_current_player_x(self):
        self.board.place(1, 1, self.board.X)
        self.board.place(1, 0, self.board.O)
        self.board.place(2, 2, self.board.X)
        self.board.reset()

        assert_equal(self.board.player, self.board.X)

    def test_reset_expect_board_same_as_new_board(self):
        other_board = Board()

        self.board.place(1, 1, self.board.X)
        self.board.place(1, 0, self.board.O)
        self.board.place(2, 2, self.board.X)
        self.board.reset()

        assert_equal(other_board.__dict__, self.board.__dict__)

    def test_get_actions_when_blank_board_expect_9_actions(self):
        actions = self.board.get_actions()

        assert_equal(9, len(actions))

    def test_get_actions_when_full_board_expect_0_actions(self):
        self.fill_board()

        actions = self.board.get_actions()

        assert_equal(0, len(actions))

    def test_get_actions_when_blank_board_expect_player_in_all_positions(self):
        actions = self.board.get_actions()

        assert_equal((0, 0, self.board.X), actions[0])
        assert_equal((1, 0, self.board.X), actions[1])
        assert_equal((2, 0, self.board.X), actions[2])
        assert_equal((0, 1, self.board.X), actions[3])
        assert_equal((1, 1, self.board.X), actions[4])
        assert_equal((2, 1, self.board.X), actions[5])
        assert_equal((0, 2, self.board.X), actions[6])
        assert_equal((1, 2, self.board.X), actions[7])
        assert_equal((2, 2, self.board.X), actions[8])

    def test_get_actions_when_space_occupied_expect_not_in_list(self):
        self.board.place(0, 2, self.board.X)

        actions = self.board.get_actions()
        is_occupied_space_in_board = (0, 2, self.board.X) in actions

        assert_false(is_occupied_space_in_board)

    def fill_board(self):
        self.board.place(0, 0, self.board.O)
        self.board.place(0, 1, self.board.X)
        self.board.place(0, 2, self.board.O)
        self.board.place(1, 0, self.board.X)
        self.board.place(1, 1, self.board.X)
        self.board.place(1, 2, self.board.O)
        self.board.place(2, 0, self.board.X)
        self.board.place(2, 1, self.board.O)
        self.board.place(2, 2, self.board.X)
