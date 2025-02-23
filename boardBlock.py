import pygame


class BoardBlock:
    def __init__(self, screen, rect):
        self.active = False
        self.screen = screen
        self.rect = rect
        self.color = None
        self.onColor = (0, 0, 255)
        self.offColor = None
        self.on = False

    def update_color(self, color):
        self.color = color
        self.offColor = color

    def activate(self):
        self.on = True
        self.color = self.onColor

    def deactivate(self):
        self.on = False
        self.color = self.offColor

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
 