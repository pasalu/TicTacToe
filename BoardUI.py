from Tkinter import *
from functools import partial

from Board import Board


class BoardUI:
    BUTTON_WIDTH = 3

    def __init__(self, master, board, player):
        """
        Initializes the UI.
        :param master: The root of the TK widget.
        :param Board board: The board model.
        :param player: The first player.
        """
        self.player = player
        self.board = board.board

        for y in xrange(len(self.board)):
            for x in xrange(len(self.board[0])):
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
        button.config(text=Board.X)

    def set_current_player(self, player):
        self.player = player
