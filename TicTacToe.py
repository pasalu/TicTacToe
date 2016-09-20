from Board import *

def main():
    board = Board()
    board.place(0, 0, board.X)
    board.place(0, 1, board.X)
    board.place(0, 2, board.X)
    board.place(1, 1, board.O)
    board.place(2, 2, board.O)
    board.show()

if __name__ == "__main__":
    main()
