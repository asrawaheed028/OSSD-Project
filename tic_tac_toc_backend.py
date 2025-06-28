# backend.py

class TicTacToeGame:
    def _init_(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            winner = self.check_winner()
            draw = self.check_draw()
            player = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True, player, winner, draw
        return False, None, None, None

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]

        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]
        return None

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return self.check_winner() is None

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player="X"