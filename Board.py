"""
Programmer: Peter Salu
Created on: July 30, 2016
"""

class Board:
    """
    Holds the state for the tic tac toe board.
    """
    X = "X"
    O = "O"

    def __init__(self):
        self.board = [[]];

    def show(self):
        print "X: ", self.X, "O: ", self.O, "self.board: ", self.board
