from Tkinter import *
from functools import partial

from Board import Board


class BoardUI:
    """
    View for the TicTacToe Board.
    """
    BUTTON_WIDTH = 3

    def __init__(self, master, board):
        """
        Initializes the UI.
        :param master: The root of the TK widget.
        :param Board board: The board model.
        """
        self.board = board

        for y in xrange(len(self.board.board)):
            for x in xrange(len(self.board.board[0])):
                button = Button(master, width=BoardUI.BUTTON_WIDTH)
                button.grid(row=y, column=x)
                # Using partial here to freeze the value of button because it will be changed in the loop.
                place_partial = partial(self.place, button)
                button.config(command=place_partial)

    def place(self, button):
        """
        Place a button on the board.
        :param button: The button that was clicked.
        """
        button.config(text=self.board.player)
        self.board.switch_current_player()
