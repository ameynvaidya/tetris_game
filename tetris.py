'''
Main script
'''
import pygame
from pygame.locals import *

import lib.board as board
import lib.piece as piece
import ui.board as ui_board

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640


class TetrisGame:
    def __init__(self, width=10, height=20):
        self._running = True
        self._display_surf = None
        self._width = width
        self._height = height
        self.display_size = SCREEN_WIDTH, SCREEN_HEIGHT
        self._board = board.Board(width, height)
        # set some random blocks on board
        self._board.fill_fake_data()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.display_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Tetris")
        self._board_surf = ui_board.BoardSprite(
            self._board, SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(
            self._board_surf.surf,
            ((SCREEN_WIDTH - self._board_surf.width()) / 2,
                (SCREEN_HEIGHT - self._board_surf.height()) / 2))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = TetrisGame()
    app.on_execute()
