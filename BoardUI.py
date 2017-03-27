from Tkinter import *
from Board import Board


class BoardUI:
    BUTTON_WIDTH = 3

    def __init__(self, master, player):
        """
        Initializes the UI.
        :param master: The root of the TK widget.
        :param player: The first player.
        """
        self.player = player

        # Top row.
        self.button00 = Button(master, width=BoardUI.BUTTON_WIDTH)
        self.button01 = Button(master, width=BoardUI.BUTTON_WIDTH)
        self.button02 = Button(master, width=BoardUI.BUTTON_WIDTH)

        # Middle row.
        self.button10 = Button(master, width=BoardUI.BUTTON_WIDTH)
        self.button11 = Button(master, width=BoardUI.BUTTON_WIDTH)
        self.button12 = Button(master, width=BoardUI.BUTTON_WIDTH)

        # Bottom row.
        self.button20 = Button(master, width=BoardUI.BUTTON_WIDTH)
        self.button21 = Button(master, width=BoardUI.BUTTON_WIDTH)
        self.button22 = Button(master, width=BoardUI.BUTTON_WIDTH)

        self.button00.grid(row=0, column=0)
        self.button01.grid(row=0, column=1)
        self.button02.grid(row=0, column=2)

        self.button10.grid(row=1, column=0)
        self.button11.grid(row=1, column=1)
        self.button12.grid(row=1, column=2)

        self.button20.grid(row=2, column=0)
        self.button21.grid(row=2, column=1)
        self.button22.grid(row=2, column=2)

        self.button00.config(command=lambda: self.place(self.button00))
        self.button01.config(command=lambda: self.place(self.button01))
        self.button02.config(command=lambda: self.place(self.button02))

        self.button10.config(command=lambda: self.place(self.button10))
        self.button11.config(command=lambda: self.place(self.button11))
        self.button12.config(command=lambda: self.place(self.button12))

        self.button20.config(command=lambda: self.place(self.button20))
        self.button21.config(command=lambda: self.place(self.button21))
        self.button22.config(command=lambda: self.place(self.button22))

    def place(self, button):
        """
        Place a button on the board.
        :param button: The button that was clicked.
        """
        print button
        button.config(text=Board.X)

    def set_current_player(self, player):
        self.player = player
