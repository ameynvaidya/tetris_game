'''
Main script
'''
import pygame
from pygame.locals import *

import lib.board as board
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
        self._board.set_grid(0, 0, 1)
        self._board.set_grid(1, 0, 1)
        self._board.set_grid(2, 0, 1)
        self._board.set_grid(3, 0, 1)

        self._board.set_grid(0, 1, 2)
        self._board.set_grid(1, 1, 2)
        self._board.set_grid(2, 1, 2)
        self._board.set_grid(0, 2, 2)

        self._board.set_grid(3, 1, 3)
        self._board.set_grid(3, 2, 3)
        self._board.set_grid(3, 3, 3)
        self._board.set_grid(4, 1, 3)

        self._board.set_grid(5, 2, 4)
        self._board.set_grid(5, 3, 4)
        self._board.set_grid(6, 2, 4)
        self._board.set_grid(6, 3, 4)

        self._board.set_grid(0, 4, 5)
        self._board.set_grid(0, 3, 5)
        self._board.set_grid(1, 3, 5)
        self._board.set_grid(1, 2, 5)

        self._board.set_grid(4, 0, 6)
        self._board.set_grid(5, 0, 6)
        self._board.set_grid(6, 0, 6)
        self._board.set_grid(5, 1, 6)

        self._board.set_grid(6, 1, 7)
        self._board.set_grid(7, 1, 7)
        self._board.set_grid(7, 0, 7)
        self._board.set_grid(8, 0, 7)

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
