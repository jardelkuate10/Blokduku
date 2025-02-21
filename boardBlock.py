import pygame


class BoardBlock:
    def __init__(self, screen, rect):
        self.active = False
        self.screen = screen
        self.rect = rect
        self.color = (128, 128, 128)
        self.onColor = (0, 0, 255)
        self.offColor = (128, 128, 128)
        self.on = False

    def activate(self):
        self.on = True
        self.color = self.onColor

    def deactivate(self):
        self.on = False
        self.color = self.offColor

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
