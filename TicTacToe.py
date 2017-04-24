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

    print ("Welcome to Tic Tac Toe! We'll be starting you off with 2 player " 
           "mode for now.")

    while True:
        coordinates = raw_input(player + " player Enter the x, y coordinates "
                "of your piece: ")
        x, y = parse_input(coordinates)

        if not board.place(x, y, player):
            print ("Enter coordinates that haven't been taken between 0 and 2.")
            continue

        board.show()

        if board.has_won(player):
            print (player + " Won!")
            break

        if player == board.X:
            player = board.O
        else:
            player = board.X

if __name__ == "__main__":
    main()
