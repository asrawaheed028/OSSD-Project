import tkinter as tk
from tkinter import messagebox
from tic_tac_toc_backend import TicTacToeGame

# GUI Application class
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="red")  # Changed to red background
        self.game = TicTacToeGame()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

        # Bind ESC to exit fullscreen
        self.root.bind("<Escape>", self.exit_fullscreen)

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="red")  # Match frame background to red
        frame.pack(pady=40)

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font=('Helvetica', 40), width=5, height=2,
                                bg="#ffffff",  # White background for buttons
                                activebackground="#e6e6e6",  # Slight gray on click
                                command=lambda i=i, j=j: self.button_click(i, j))
                btn.grid(row=i, column=j, padx=10, pady=10)
                self.buttons[i][j] = btn

        self.restart_button = tk.Button(self.root, text="Restart", font=('Helvetica', 20),
                                        bg="#d9d9d9", activebackground="#c0c0c0",
                                        command=self.restart_game)
        self.restart_button.pack(pady=20)

    def button_click(self, row, col):
        valid, player, winner, draw = self.game.make_move(row, col)
        if valid:
            color = "red" if player == "X" else "blue"
            self.buttons[row][col].config(text=player, fg=color)
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
                self.buttons[i][j].config(text="", state="normal", fg="black")

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()

    # Start in fullscreen
    root.attributes("-fullscreen", True)
    root.update_idletasks()

    app = TicTacToeApp(root)
    root.mainloop()
