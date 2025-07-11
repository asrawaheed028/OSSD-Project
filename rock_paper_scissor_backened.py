# rps_backend.py

import random

# List of choices
CHOICES = ['Rock', 'Paper', 'Scissors']

# Determines the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Gets a random computer choice
def get_computer_choice():
    return random.choice(CHOICES)