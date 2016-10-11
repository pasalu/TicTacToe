"""
Programmer: Peter Salu
Created on: July 30, 2016
"""
import copy

class Board:
    """
    Holds the state for the tic tac toe board.
    """
    X = "X"
    O = "O"
    ROWS = 3
    COLUMNS = 3
    BLANK_BOARD = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __init__(self):
        # For some odd reason just doing list(Board.BLANK_BOARD) won't create a
        # deep copy of the list.
        self.board = copy.deepcopy(Board.BLANK_BOARD)

    def place(self, x, y, player):
        if x < 0 or y < 0 or x > 2 or y > 2:
            return False

        if self.board[y][x] != " ":
            return False

        self.board[y][x] = player

        return True

    def has_won(self, player):
        return False

    def show(self):
        for row in self.board:
            for position in row:
                print position,
            print
