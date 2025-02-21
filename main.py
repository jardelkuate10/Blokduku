import pygame

from belowBoard import BelowBoard
from board import Board

pygame.init()

width, height = 576, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Blokduku')

B = Board(screen)
BB = BelowBoard(screen)


def draw():
    screen.fill('white')
    B.draw_board()
    BB.draw()
    B.update_score()


def update(evnt):
    BB.update(evnt)
    B.update(BB, evnt)


running = True

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False
        # update game state
        else:
            update(event)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
               B.clear()

    # draw everything
    draw()

    # refresh screen
    pygame.display.flip()

pygame.quit()
