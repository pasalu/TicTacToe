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
                place_partial = partial(self.place, button, x, y)
                button.config(command=place_partial)

        self.label = Label(master)
        self.label.grid(row=3, column=0, columnspan=3)
        self.set_label()

    def place(self, button, x, y):
        """
        Place a button on the board.
        :param button: The button that was clicked.
        :param x: The x coordinate of the button.
        :param y: The y coordinate of the button.
        """
        if self.board.place(x, y, self.board.player):
            button.config(text=self.board.player)
            self.board.switch_current_player()
            self.set_label()

    def set_label(self):
        """
        Display the current player or who has won.
        """
        if self.board.has_won(self.board.X):
            self.label.config(text=self.board.X + " wins!")
        elif self.board.has_won(self.board.O):
            self.label.config(text=self.board.O + " wins!")
        elif self.board.is_tie():
            self.label.config(text="It's a tie!")
        else:
            self.label.config(text=self.board.player + "'s turn")
