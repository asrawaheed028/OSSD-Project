import random

class MemoryGameBackend:
    def _init_(self):
        self.symbols = []
        self.moves = 0
        self.first_click = None
        self.second_click = None
        self.prepare_game()

    def prepare_game(self):
        """Create and shuffle the symbols list."""
        pairs = ['🍎', '🍌', '🍒', '🍇', '🍋', '🥝', '🍍', '🍉']
        self.symbols = pairs * 2
        random.shuffle(self.symbols)
        self.moves = 0
        self.first_click = None
        self.second_click = None

    def check_match(self, idx1, idx2):
        """Check if two indexes have matching symbols."""
        return self.symbols[idx1] == self.symbols[idx2]

    def increase_moves(self):
        """Increment move count."""
        self.moves += 1
        return self.moves