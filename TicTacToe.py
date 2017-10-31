from Board import Board
from UI.MainUI import MainUI


def main():
    board = Board()
    # root = Tk()
    ui = MainUI(board)

    ui.mainloop()
    ui.destroy()

if __name__ == "__main__":
    main()
