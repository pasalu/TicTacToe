from Board import Board
from UI.MainUI import MainUI


def main():
    board = Board()
    ui = MainUI(board)

    ui.mainloop()
    ui.destroy()


if __name__ == "__main__":
    main()
