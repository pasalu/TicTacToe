from Tkinter import Tk, Frame
from BoardUI import BoardUI
from Menu import Menu
from Board import Board


class MainUI(Tk):
    """
    Handles switching between frames for TicTacToe. Taken from:
    https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    """

    ROW_INDEX = 0
    COLUMN_INDEX = 0

    def __init__(self, board):
        """
        :param Board board:
        """

        Tk.__init__(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(self.ROW_INDEX, weight=1)
        container.grid_columnconfigure(self.COLUMN_INDEX, weight=1)

        self.frames = {}

        self.frames[BoardUI.__name__] = BoardUI(container, self, board)
        self.frames[BoardUI.__name__].grid(row=0, column=0, sticky="nsew")

        self.frames[Menu.__name__] = Menu(master=container, controller=self)
        self.frames[Menu.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu.__name__)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
