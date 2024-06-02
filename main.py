import pygame

def 
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Blokus')
clock = pygame.time.Clock()
running = True

while running:

    # exit out of game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    # refresh rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
