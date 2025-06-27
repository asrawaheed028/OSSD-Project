import tkinter as tk
from tkinter import messagebox

# Create Main Window
root = tk.Tk()
root.title("Mini Game Hub")
root.geometry("400x400")
root.configure(bg="#F3F3F3")

# Title Label
title_label = tk.Label(root, text="🎮 Mini Game Hub 🎮", font=("Arial", 20, "bold"), bg="#F3F3F3", fg="#333")
title_label.pack(pady=30)

# Start Tic Tac Toe Button
def start_tic_tac_toe():
    messagebox.showinfo("Tic Tac Toe", "Tic Tac Toe window will open here!")

tic_tac_toe_button = tk.Button(root, text="Start Tic Tac Toe", font=("Arial", 14), width=25, bg="#4CAF50", fg="white", command=start_tic_tac_toe)
tic_tac_toe_button.pack(pady=15)

# Start Memory Matching Game Button
def start_memory_match():
    messagebox.showinfo("Memory Match", "Memory Matching Game window will open here!")

memory_match_button = tk.Button(root, text="Start Memory Matching Game", font=("Arial", 14), width=25, bg="#2196F3", fg="white", command=start_memory_match)
memory_match_button.pack(pady=15)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), width=25, bg="#f44336", fg="white", command=root.quit)
exit_button.pack(pady=30)

# Run the app
root.mainloop()
