# main.py

import tkinter as tk
from tkinter import messagebox
from tic_tac_toc_backend import TicTacToeGame

# GUI Application class
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = TicTacToeGame()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font=('Helvetica', 20), width=5, height=2,
                                command=lambda i=i, j=j: self.button_click(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        self.restart_button = tk.Button(self.root, text="Restart", font=('Helvetica', 14), command=self.restart_game)
        self.restart_button.pack(pady=10)

    def button_click(self, row, col):
        valid, player, winner, draw = self.game.make_move(row, col)
        if valid:
            self.buttons[row][col].config(text=player, fg="blue" if player == "X" else "red")
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.disable_buttons()
            elif draw:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def restart_game(self):
        self.game.reset()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
