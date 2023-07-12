import random

class Tetromino:
    def __init__(self):
        self.shape = random.choice(["I", "J", "L", "O", "S", "T", "Z"])
        self.rotation = 0
        self.x = 0
        self.y = 0

    def update(self, grid):
        # Update the tetromino's position based on user input and gravity
        pass

    def rotate(self):
        # Rotate the tetromino
        pass

    def move_left(self):
        # Move the tetromino to the left
        pass

    def move_right(self):
        # Move the tetromino to the right
        pass

    def move_down(self):
        # Move the tetromino down
        pass
