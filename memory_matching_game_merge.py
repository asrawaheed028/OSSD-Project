import tkinter as tk
from tkinter import messagebox
import random

class MemoryGameBackend:
    def __init__(self):
        self.symbols = []
        self.moves = 0
        self.first_click = None
        self.second_click = None
        self.prepare_game()

    def prepare_game(self):
        pairs = ['🍎', '🍌', '🍒', '🍇', '🍋', '🥝', '🍍', '🍉']
        self.symbols = pairs * 2
        random.shuffle(self.symbols)
        self.moves = 0
        self.first_click = None
        self.second_click = None

    def check_match(self, idx1, idx2):
        return self.symbols[idx1] == self.symbols[idx2]

    def increase_moves(self):
        self.moves += 1
        return self.moves

# ✅ Frontend Code (your original)

import tkinter as tk
from tkinter import messagebox
from memory_game_backend import MemoryGameBackend

# Initialize Backend
backend = MemoryGameBackend()

# Color map for text (emoji) color only
symbol_colors = {
    '🍎': "#D32F2F",   # Deep Red
    '🍌': "#FBC02D",   # Golden Yellow
    '🍒': "#C2185B",   # Dark Pink
    '🍇': "#7B1FA2",   # Deep Purple
    '🍋': "#FDD835",   # Lemon Yellow
    '🥝': "#388E3C",   # Rich Green
    '🍍': "#FFA000",   # Vivid Orange
    '🍉': "#43A047"    # Watermelon Green
}
# Create the main window
memory_game = tk.Tk()
memory_game.configure(bg="green")
memory_game.title("Memory Matching Game")

# Make fullscreen
memory_game.attributes("-fullscreen", True)

# Allow ESC key to exit fullscreen
memory_game.bind("<Escape>", lambda event: memory_game.attributes("-fullscreen", False))

buttons = {}

def button_click(x, y):
    index = (x * 4) + y
    button = buttons[(x, y)]

    if button["text"] == " " and backend.second_click is None:
        symbol = backend.symbols[index]
        button.config(text=symbol, fg=symbol_colors[symbol])  # only text color changes

        if backend.first_click is None:
            backend.first_click = (x, y)
        else:
            backend.second_click = (x, y)
            backend.increase_moves()
            move_label.config(text=f"Moves: {backend.moves}")
            memory_game.after(500, check_match)

def check_match():
    b1 = buttons[backend.first_click]
    b2 = buttons[backend.second_click]
    idx1 = (backend.first_click[0] * 4) + backend.first_click[1]
    idx2 = (backend.second_click[0] * 4) + backend.second_click[1]

    if backend.check_match(idx1, idx2):
        b1.config(bg="#C8E6C9", state="disabled")
        b2.config(bg="#C8E6C9", state="disabled")
    else:
        b1.config(text=" ", fg="black")
        b2.config(text=" ", fg="black")

    backend.first_click = None
    backend.second_click = None

    check_win()

def check_win():
    for btn in buttons.values():
        if btn["text"] == " ":
            return
    messagebox.showinfo("Congratulations!", f"You've matched all pairs in {backend.moves} moves!")
    reset_game()

def reset_game():
    backend.prepare_game()
    for (x, y), btn in buttons.items():
        btn.config(text=" ", fg="black", bg="#ECECEC", state="normal")
    move_label.config(text=f"Moves: {backend.moves}")

# Move Counter Label
move_label = tk.Label(memory_game, text="Moves: 0", font=("Arial", 16))
move_label.pack(pady=10)

# Game Grid Frame
grid_frame = tk.Frame(memory_game)
grid_frame.pack()

for i in range(4):
    for j in range(4):
        btn = tk.Button(grid_frame, text=" ", font=("Arial", 20), width=6, height=3,
                        command=lambda x=i, y=j: button_click(x, y))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[(i, j)] = btn

# Reset Button
reset_button = tk.Button(memory_game, text="Reset Game", font=("Arial", 14), bg="#FF7043", fg="white", command=reset_game)
reset_button.pack(pady=20)

# Exit Fullscreen Button
def exit_fullscreen():
    memory_game.attributes("-fullscreen", False)

exit_button = tk.Button(memory_game, text="Exit Fullscreen", font=("Arial", 12), command=exit_fullscreen)
exit_button.pack(pady=5)

# Run the app
memory_game.mainloop()

