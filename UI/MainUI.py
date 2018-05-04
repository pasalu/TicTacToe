from Tkinter import Tk, Frame
from BoardUI import BoardUI
from Menu import Menu
from Board import Board
from AI import AI


class MainUI(Tk):
    """
    Handles switching between frames for TicTacToe. Taken from:
    https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    """

    ROW_INDEX = 0
    COLUMN_INDEX = 0

    def __init__(self):
        Tk.__init__(self)

        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(self.ROW_INDEX, weight=1)
        self.container.grid_columnconfigure(self.COLUMN_INDEX, weight=1)

        self.frames = {}

        self.frames[Menu.__name__] = Menu(master=self.container, controller=self)
        self.frames[Menu.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu.__name__, None)

    def show_frame(self, page_name, ai_strategy):
        board = Board()
        ai = AI(ai_strategy)
        is_multiplayer = ai_strategy is None

        board.set_is_multiplayer(is_multiplayer)

        self.frames[BoardUI.__name__] = BoardUI(self.container, self, board, ai)
        self.frames[BoardUI.__name__].grid(row=0, column=0, sticky="nsew")

        frame = self.frames[page_name]
        frame.tkraise()
