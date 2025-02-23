import time

import pygame

from belowBoard import BelowBoard
from board import Board
from gameScreen import GameScreen

pygame.init()

# width, height = 576, 1000
# screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Blokduku')

# game_clock = 15
# last_time = time.time()
#
# B = Board(screen)
# BB = BelowBoard(screen)


# def draw():
#     screen.fill('white')
#     B.draw_board()
#     BB.draw()
#     B.update_score()
#
#
# def update(evnt):
#     BB.update(evnt)
#     B.update(BB, evnt)
#     update_clock()
#
#
# def update_clock(lt, game_clock):
#     current_time = time.time()
#     if current_time - lt >= 1:
#         game_clock -= 1
#         lt = current_time
start_time = time.time()
game_screen = GameScreen(start_time)

running = True

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False
        # update game state
        else:
            game_screen.update(event)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_screen.clear()

    # draw everything
    game_screen.draw()

    # refresh screen
    pygame.display.flip()

pygame.quit()
