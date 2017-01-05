from Tkinter import *
from Board import Board

class BoardUI:
    def __init__(self, master):
        self.button1 = Button(master, text = Board.X, fg = "red")
        self.button2 = Button(master, text = Board.O, fg = "red")
        
        self.button1.grid(row = 0, column = 1)
        self.button2.grid(row = 1, column = 1)
