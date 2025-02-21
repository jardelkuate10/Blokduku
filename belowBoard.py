from gameBlock import GameBlock

width, height = 576, 1000
bw = 60  # block width
sp = 62  # space

square_x = 102
line_x = 102
L_x = 102
Z_x = 102

shape1_2_y = 600
shape3_y = 800


class BelowBoard:
    def __init__(self, screen):
        self.screen = screen
        self.shape = None
        self.load_shape()

    def load_shape(self):
        self.shape = GameBlock(self.screen, width / 2 - bw, 700)

    def draw(self):
        self.shape.draw()

    def update(self, event):
        self.shape.update(event)
