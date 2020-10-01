'''
Main script
'''
import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_x,
    QUIT,
)

import lib.board as board
import lib.piece as piece
import ui.board as ui_board
import ui.piece as ui_piece

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
FRAMERATE = 30


class TetrisGame:
    def __init__(self, width=10, height=20):
        self._running = True
        self._display_surf = None
        self.__piece_surf = None
        self._clock = pygame.time.Clock()
        self._width = width
        self._height = height
        self.display_size = SCREEN_WIDTH, SCREEN_HEIGHT
        self._board = board.Board(width, height)
        # set some random blocks on board
        self._board.fill_fake_data()

        # random piece on the tetris board
        self._piece = None
        self._piece_x = 4
        self._piece_y = 10

        self._piece_drop_rate = 1000


    def on_init(self):
        pygame.init()

        self._PIECEDROP = pygame.USEREVENT + 1
        pygame.time.set_timer(self._PIECEDROP, self._piece_drop_rate)

        self._display_surf = pygame.display.set_mode(
            self.display_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Tetris")
        self._board_surf = ui_board.BoardSprite(
            self._board, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Initialize the location of the board and the piece to be in the
        # center of the screen
        board_left_top_x = (SCREEN_WIDTH - self._board_surf.width()) / 2
        board_left_top_y = (SCREEN_HEIGHT - self._board_surf.height()) / 2
        self._board_surf.rect.move_ip(board_left_top_x, board_left_top_y)
        self.piece_init()

    def piece_init(self):
        self._piece = piece.Piece.get_pieces()[random.randrange(7)]
        self._piece_surf = ui_piece.PieceSprite(
            self._board_surf.board_cell_width,
            self._piece)
        self._piece_surf.rect.move_ip(
            self._board_surf.rect.left + 4 * self._board_surf.board_cell_width, self._board_surf.rect.top)
        self._piece_x = 4
        self._piece_y = self._height - 4
        if (self._board.is_piece_out_of_bound(self._piece_x, self._piece_y, self._piece) or 
            self._board.did_piece_collided_with_body(self._piece_x, self._piece_y, self._piece)):
            self._running = False
            return

    def move_piece_down(self):
        if (self._board.is_piece_out_of_bound(self._piece_x, self._piece_y - 1, self._piece) or 
            self._board.did_piece_collided_with_body(self._piece_x, self._piece_y - 1, self._piece)):
            self._board.set_piece(self._piece_x, self._piece_y, self._piece)
            self._board_surf.update(self._board)
            self.piece_init()
            return
        self._piece_y = self._piece_y - 1
        self._piece_surf.rect.move_ip(0, self._board_surf.board_cell_width)

    def move_piece_left(self):
        if (self._board.is_piece_out_of_bound(self._piece_x - 1, self._piece_y, self._piece)):
            return
        if (self._board.did_piece_collided_with_body(self._piece_x - 1, self._piece_y, self._piece)):
            return
        self._piece_x = self._piece_x - 1
        self._piece_surf.rect.move_ip(-self._board_surf.board_cell_width, 0)

    def move_piece_right(self):
        if (self._board.is_piece_out_of_bound(self._piece_x + 1, self._piece_y, self._piece)):
            return
        if (self._board.did_piece_collided_with_body(self._piece_x + 1, self._piece_y, self._piece)):
            return
        self._piece_x = self._piece_x + 1
        self._piece_surf.rect.move_ip(self._board_surf.board_cell_width, 0)

    def rotate_piece(self):
        original_location = self._piece_surf.rect
        piece_next = self._piece.nextRotation()
        if (self._board.is_piece_out_of_bound(self._piece_x, self._piece_y, piece_next)):
            return
        if (self._board.did_piece_collided_with_body(self._piece_x, self._piece_y, piece_next)):
            return
        self._piece = piece_next
        self._piece_surf = ui_piece.PieceSprite(
            self._board_surf.board_cell_width,
            self._piece)
        self._piece_surf.rect = original_location

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self._running = False
            if event.key == K_DOWN:
                self.move_piece_down()
            if event.key == K_LEFT:
                self.move_piece_left()
            if event.key == K_RIGHT:
                self.move_piece_right()
            if event.key == K_x or event.key == K_UP:
                self.rotate_piece()
        elif event.type == self._PIECEDROP:
            self.move_piece_down()
        elif event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._board_surf.surf, self._board_surf.rect)
        self._display_surf.blit(self._piece_surf.surf, self._piece_surf.rect)
        pygame.display.flip()
        self._clock.tick(FRAMERATE)

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
