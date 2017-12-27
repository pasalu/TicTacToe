from Tkinter import *
from functools import partial
import tkFont

from Board import Board


class BoardUI(Frame):
    """
    View for the TicTacToe Board.
    """
    BUTTON_WIDTH = 20
    BUTTON_HEIGHT = 9

    def __init__(self, master, controller, board):
        """
        Initializes the UI.
        :param master: The root of the TK widget.
        :param controller: The class that handles switching between frames.
        :param Board board: The board model.
        """
        Frame.__init__(self, master)

        self.controller = controller
        self.board = board

        # Being lazy here and just keeping all the buttons in a flat list because we don't need to know their position.
        self.buttons = []

        button_font = tkFont.Font(size=12)

        # Setup button grid.
        for y in xrange(len(self.board.board)):
            for x in xrange(len(self.board.board[0])):
                button = Button(self, height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, font=button_font)
                button.grid(row=y, column=x)
                # Using partial here to freeze the value of button because it will be changed in the loop.
                place_partial = partial(self.place, button, x, y)
                button.config(command=place_partial)

                self.buttons.append(button)

        # Setup status label
        self.label = Label(self)
        self.label.grid(row=3, column=0, columnspan=3)
        self.set_label()

        # Setup reset button
        self.reset = Button(self, text="RESET", command=self.reset)
        self.reset.grid(row=4, column=0, columnspan=3)

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

    def reset(self):
        """
        Reset the board.
        :return:
        """
        self.board.reset()
        self.set_label()

        for button in self.buttons:
            button.config(text="")
