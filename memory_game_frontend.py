import tkinter as tk
from tkinter import messagebox
from memory_game_backend import MemoryGameBackend

# Initialize Backend
backend = MemoryGameBackend()

# Create the main window
memory_game = tk.Tk()
memory_game.title("Memory Matching Game")
memory_game.geometry("500x550")
memory_game.resizable(False, False)

buttons = {}

# Function to handle button click
def button_click(x, y):
    index = (x * 4) + y
    button = buttons[(x, y)]

    if button["text"] == " " and backend.second_click is None:
        button.config(text=backend.symbols[index])

        if backend.first_click is None:
            backend.first_click = (x, y)
        else:
            backend.second_click = (x, y)
            backend.increase_moves()
            move_label.config(text=f"Moves: {backend.moves}")
            memory_game.after(500, check_match)

# Function to check for matches
def check_match():
    b1 = buttons[backend.first_click]
    b2 = buttons[backend.second_click]
    idx1 = (backend.first_click[0] * 4) + backend.first_click[1]
    idx2 = (backend.second_click[0] * 4) + backend.second_click[1]

    if backend.check_match(idx1, idx2):
        b1.config(bg="#C8E6C9", state="disabled")
        b2.config(bg="#C8E6C9", state="disabled")
    else:
        b1.config(text=" ")
        b2.config(text=" ")

    backend.first_click = None
    backend.second_click = None

    check_win()

# Function to check win condition
def check_win():
    for btn in buttons.values():
        if btn["text"] == " ":
            return
    messagebox.showinfo("Congratulations!", f"You've matched all pairs in {backend.moves} moves!")
    reset_game()

# Function to reset game
def reset_game():
    backend.prepare_game()
    for (x, y), btn in buttons.items():
        btn.config(text=" ", bg="#ECECEC", state="normal")
    move_label.config(text=f"Moves: {backend.moves}")

# Move Counter Label
move_label = tk.Label(memory_game, text="Moves: 0", font=("Arial", 16))
move_label.pack(pady=10)

# Game Grid Frame
grid_frame = tk.Frame(memory_game)
grid_frame.pack()

# Create Buttons and place them in a grid
for i in range(4):
    for j in range(4):
        btn = tk.Button(grid_frame, text=" ", font=("Arial", 20), width=6, height=3,
                        command=lambda x=i, y=j: button_click(x, y))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[(i, j)] = btn

# Reset Button
reset_button = tk.Button(memory_game, text="Reset Game", font=("Arial", 14), bg="#FF7043", fg="white", command=reset_game)
reset_button.pack(pady=20)

# Run the app
memory_game.mainloop()
