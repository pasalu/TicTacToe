from Board import Board
from BoardUI import BoardUI
from Tkinter import *

def parse_input(value):
    pieces = value.split(",")
    x = int(pieces[0].strip())
    y = int(pieces[1].strip())

    return x, y

def main():
    board = Board()
    root = Tk()
    player = board.X
    BoardUI(root, board)

    root.mainloop()
    root.destroy()

if __name__ == "__main__":
    main()
