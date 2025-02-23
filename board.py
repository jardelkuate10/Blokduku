import pygame
from boardBlock import BoardBlock

bw = 60  # block width
light_gray = (158, 158, 158)
dark_gray = (128, 128, 128)


class Board:
    def __init__(self, game_screen):
        self.board_blocks = []
        self.active_blocks = []
        self.clear_list = []
        self.areas = []
        self.game_screen = game_screen
        self.load_blocks()
        self.define_areas()
        self.update_colors()

    def load_blocks(self):
        h = 10
        for x in range(9):
            w = 10
            for y in range(9):
                block = BoardBlock(self.game_screen.screen, pygame.Rect(w, h, 60, 60))
                self.board_blocks.append(block)
                w += 62

            h += 62

    def draw_board(self):
        for block in self.board_blocks:
            block.draw()

    def update_colors(self):
        for area in self.areas[0:9]:
            if self.areas.index(area) % 2 == 0:
                for block in area:
                    block.update_color(light_gray)
            else:
                for block in area:
                    block.update_color(dark_gray)

    def define_areas(self):
        # squares
        for i in range(0, 55, 27):
            for j in range(0, 9, 3):
                area = [self.board_blocks[i + j], self.board_blocks[i + j + 1], self.board_blocks[i + j + 2],
                        self.board_blocks[i + j + 9], self.board_blocks[i + j + 10], self.board_blocks[i + j + 11],
                        self.board_blocks[i + j + 18], self.board_blocks[i + j + 19], self.board_blocks[i + j + 20]]

                self.areas.append(area)

        # horizontal
        for i in range(0, 73, 9):
            area = [self.board_blocks[i], self.board_blocks[i + 1], self.board_blocks[i + 2],
                    self.board_blocks[i + 3], self.board_blocks[i + 4], self.board_blocks[i + 5],
                    self.board_blocks[i + 6], self.board_blocks[i + 7], self.board_blocks[i + 8]]

            self.areas.append(area)

        # vertical
        for i in range(9):
            area = [self.board_blocks[i], self.board_blocks[i + 9], self.board_blocks[i + 2 * 9],
                    self.board_blocks[i + 3 * 9], self.board_blocks[i + 4 * 9], self.board_blocks[i + 5 * 9],
                    self.board_blocks[i + 6 * 9], self.board_blocks[i + 7 * 9], self.board_blocks[i + 8 * 9]]

            self.areas.append(area)

    def update_score(self):
        self.clear_list.clear()
        for area in self.areas:
            count = 0
            for block in area:
                if block in self.active_blocks:
                    count += 1

            if count == 9:
                for block in area:
                    if block not in self.clear_list:
                        self.clear_list.append(block)

                self.game_screen.pending_score += 90
                self.game_screen.filled_areas += 1
                print(self.areas.index(area))

    def clear(self):
        for block in self.clear_list:
            block.deactivate()
            self.clear_list.remove(block)
            if block in self.active_blocks:
                self.active_blocks.remove(block)

    def update(self, event):
        shape = self.game_screen.below_board.shape

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            check_list = [False, False, False, False]
            block_list = []

            for block in self.board_blocks:
                for rect in shape.rect_list:

                    if block.rect.collidepoint(rect.x + bw/2, rect.y + bw/2):
                        if not check_list[shape.rect_list.index(rect)]:
                            check_list[shape.rect_list.index(rect)] = True
                            block_list.append(block)
                        else:
                            break

                        if all(check_list):
                            off_list = [False, False, False, False]
                            for blck in block_list:
                                if not blck.on:
                                    off_list[block_list.index(blck)] = True
                            if all(off_list):
                                for blck in block_list:
                                    rect.clamp_ip(blck)
                                    blck.activate()
                                    self.active_blocks.append(blck)

                                shape.can_move = False
                                self.game_screen.below_board.load_shape()
                                self.game_screen.reset_clock()
                            else:
                                return
                        else:
                            break
