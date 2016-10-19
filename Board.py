import copy

class Board:
    """
    Holds the state for the tic tac toe board.
    """
    X = "X"
    O = "O"
    ROWS = 3
    COLUMNS = 3
    BLANK_BOARD = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __init__(self):
        # For some odd reason just doing list(Board.BLANK_BOARD) won't create a
        # deep copy of the list.
        self.board = copy.deepcopy(Board.BLANK_BOARD)

    def place(self, x, y, player):
        if x < 0 or y < 0 or x > 2 or y > 2:
            return False

        if self.board[y][x] != " ":
            return False

        self.board[y][x] = player

        return True

    def has_won(self, player):
        # Top row.
        if (self.board[0][0] == player and
            self.board[0][1] == player and
            self.board[0][2] == player):
            return True
        # Middle row.
        elif (self.board[1][0] == player and
              self.board[1][1] == player and
              self.board[1][2] == player):
            return True
        # Bottom row.
        elif (self.board[1][0] == player and
              self.board[1][1] == player and
              self.board[1][2] == player):
            return True
        # Left column.
        elif (self.board[0][0] == player and
              self.board[1][0] == player and
              self.board[2][0] == player):
            return True
        # Middle column.
        elif (self.board[0][1] == player and
              self.board[1][1] == player and
              self.board[2][1] == player):
            return True
        # Middle column.
        elif (self.board[0][2] == player and
              self.board[1][2] == player and
              self.board[2][2] == player):
            return True
        # Left to right diagonal.
        elif (self.board[0][0] == player and
              self.board[1][1] == player and
              self.board[2][2] == player):
            return True
        # Right to left diagonal.
        elif (self.board[0][2] == player and
              self.board[1][1] == player and
              self.board[2][0] == player):
            return True
        else:
            return False


    def show(self):
        for row in self.board:
            for position in row:
                print position,
            print
