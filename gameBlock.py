import random

import pygame

bw = 60  # block width
sp = 62  # space


class GameBlock:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect_list = []
        self.color = (0, 0, 255)
        self.shape = ''
        self.selected = False
        self.can_move = True
        self.determine_shape()

    def draw(self):
        for rect in self.rect_list:
            pygame.draw.rect(self.screen, self.color, rect)

    def update(self, event):
        if self.can_move:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for rect in self.rect_list:
                    if rect.collidepoint(event.pos):
                        self.selected = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.selected = False
            elif event.type == pygame.MOUSEMOTION:
                if self.selected:
                    for rect in self.rect_list:
                        rect.x += event.rel[0]
                        rect.y += event.rel[1]

    def determine_shape(self):
        num = random.randint(1, 4)

        match num:
            case 1:  # Square
                self.shape = 'Square'
                self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                self.rect_list.append(pygame.Rect(self.x + sp, self.y, bw, bw))
                self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                self.rect_list.append(pygame.Rect(self.x + sp, self.y + sp, bw, bw))
            case 2:  # Line
                l_num = random.randint(1, 2)
                match l_num:
                    case 1:  # Vertical Line
                        self.shape = 'Ver Line'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + 2 * sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + 3 * sp, bw, bw))
                    case 2:  # Horizontal Line
                        self.shape = 'Hor Line'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + 2 * sp, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + 3 * sp, self.y, bw, bw))
            case 3:  # L
                l_num = random.randint(1, 4)
                match l_num:
                    case 1:  # regular L
                        self.shape = 'Reg L'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + 2 * sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y + 2 * sp, bw, bw))
                    case 2:  # reverse L
                        self.shape = 'Rev L'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + 2 * sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x - sp, self.y + 2 * sp, bw, bw))
                    case 3:  # upsidedown L
                        self.shape = 'Up L'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + 2 * sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y, bw, bw))
                    case 4:  # reverse upsidedown L
                        self.shape = 'R Up L'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + 2 * sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x - sp, self.y, bw, bw))
            case 4:  # Z
                z_num = random.randint(1, 4)
                match z_num:
                    case 1:  # regular Z
                        self.shape = 'Reg z'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x - sp, self.y + sp, bw, bw))
                    case 2:  # reverse Z
                        self.shape = 'Rev Z'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x - sp, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y + sp, bw, bw))
                    case 3:  # vertical Z
                        self.shape = 'Ver Z'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x + sp, self.y + 2 * sp, bw, bw))
                    case 4:  # reverse vertical Z
                        self.shape = 'R Ver Z'
                        self.rect_list.append(pygame.Rect(self.x, self.y, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x - sp, self.y + sp, bw, bw))
                        self.rect_list.append(pygame.Rect(self.x - sp, self.y + 2 * sp, bw, bw))
