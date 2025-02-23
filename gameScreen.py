import time

import pygame

from belowBoard import BelowBoard
from board import Board

width, height = 576, 1000


class GameScreen:

    def __init__(self, start_time):
        self.game_clock = 15
        self.last_time = start_time
        self.screen_selected = True
        self.score = 0
        self.pending_score = 0
        self.filled_areas = 0
        self.screen = pygame.display.set_mode((width, height))
        self.board = Board(self)
        self.below_board = BelowBoard(self.screen)
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self):
        if self.screen_selected:
            self.screen.fill('white')
            self.board.draw_board()
            self.below_board.draw()
            self.draw_score()
            self.draw_clock()

    def update(self, event):
        self.below_board.update(event)
        self.board.update(event)

    def reset_clock(self):
        self.game_clock = 15
        self.last_time = time.time()

    def draw_clock(self):
        current_time = time.time()
        if current_time - self.last_time >= 1:
            self.game_clock -= 1
            self.last_time = current_time

        if self.game_clock == 0:
            self.screen_selected = False

        img = self.font.render(f"{self.game_clock}", True, (0, 0, 0))
        self.screen.blit(img, (30, 900))

    def update_score(self):
        self.board.update_score()

        self.score += self.pending_score * self.filled_areas
        self.pending_score = 0
        self.filled_areas = 0

    def draw_score(self):
        img = self.font.render(f"{self.score}", True, (0, 0, 0))
        self.screen.blit(img, (470, 900))

    def clear(self):
        self.update_score()
        self.board.clear()
