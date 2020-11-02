'''
Main script
'''
import pygame
import random
import time
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    K_a,
    K_h,
    K_x,
    K_p,
    K_d,
    QUIT,
)

import lib.board as board
import lib.piece as piece
import lib.brain as brain
import ui.ai_piece as ui_ai_piece
import ui.board as ui_board
import ui.piece as ui_piece
import ui.score as ui_score
import ui.next_piece as ui_next_piece
import ui.drop_piece as ui_drop_piece
import ui.debug_board as ui_debug_board
import ui.instructions as ui_instructions

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
FRAMERATE = 100


class TetrisGame:
    def __init__(self, filename: str = None, width=10, height=20):
        self._running = True
        self._paused = False
        self._debug = False
        self._auto = False
        self._hint = False

        self._display_surf = None
        self._piece_surf = None
        self._debug_board_surf = None
        self._score_surf = None
        self._next_surf = None
        self._hold_piece_surf = None
        self._instructions_surf = None
        self._ai_piece_surf = None

        self._clock = pygame.time.Clock()
        self._width = width
        self._height = height
        self.display_size = SCREEN_WIDTH, SCREEN_HEIGHT
        self._board = board.Board(width, height)

        self._piece = None
        self._next_piece = None
        self._piece_x = 4
        self._piece_y = 10
        self._piece_drop_rate = 1000
        self._auto_drop_rate = 10

        self._brain = brain.Brain(self._board)

        # self._input_piece_order = []
        # if filename:
        #     inp_file = open(filename, "r")
        #     for row in inp_file:
        #         self._input_piece_order.append(int(row))
        #     inp_file.close()
        # else:
        #     for _ in range(10000):
        #         self._input_piece_order.append(random.randrange(7))
        # self._input_piece_counter = 0


    def on_init(self):
        pygame.init()

        self._PIECEDROP = pygame.USEREVENT + 1
        pygame.time.set_timer(self._PIECEDROP, self._piece_drop_rate)

        self._AUTOPLAY = pygame.USEREVENT + 2
        pygame.time.set_timer(self._AUTOPLAY, self._auto_drop_rate)

        self._display_surf = pygame.display.set_mode(
            self.display_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Tetris")


        self._board_surf = ui_board.BoardSprite(
            self._board, SCREEN_WIDTH, SCREEN_HEIGHT)
        self._debug_board_surf = ui_debug_board.DebugBoardSprite(
            self._board_surf.board_cell_width, self._board)
        self._score_surf = ui_score.ScoreSprite(self._board)
        self._score_surf.rect.move_ip(20, 300)
        self._instructions_surf = ui_instructions.InstructionsSprite()
        self._instructions_surf.rect.move_ip(470, 30)


        debug_board_left_top_x = (
            SCREEN_WIDTH - self._debug_board_surf.rect.width) / 2
        debug_board_left_top_y = (
            SCREEN_HEIGHT - self._debug_board_surf.rect.height) / 2
        self._debug_board_surf.rect.move_ip(
            debug_board_left_top_x, debug_board_left_top_y)


        board_left_top_x = (SCREEN_WIDTH - self._board_surf.width()) / 2
        board_left_top_y = (SCREEN_HEIGHT - self._board_surf.height()) / 2
        self._board_surf.rect.move_ip(board_left_top_x, board_left_top_y)

        self._piece = None
        self._next_piece = piece.Piece.get_pieces()[random.randrange(7)]

        self.piece_init()

    def piece_init(self):
        self._piece = self._next_piece
        self._next_piece = piece.Piece.get_pieces()[random.randrange(7)]
        self.update_next_piece()

        self._piece_surf = ui_piece.PieceSprite(
            self._board_surf.board_cell_width,
            self._piece)
        self._piece_x = 4
        self._piece_y = self._height - 4
        self._piece_surf.rect.move_ip(
            self._board_surf.rect.left + self._piece_x * self._board_surf.board_cell_width, self._board_surf.rect.top)

        if (self._board.is_piece_out_of_bound(self._piece_x, self._piece_y, self._piece) or
                self._board.did_piece_collided_with_body(self._piece_x, self._piece_y, self._piece)):
            self.on_game_end()
            return
        (self._ai_piece_x, self._ai_piece_y, self._ai_rotation_count,
         self._ai_piece) = self._brain.find_best_position(self._piece, self._piece_x, self._piece_y)
        self.ai_piece_render()
        self.drop_piece_render()


    def update_next_piece(self):
        self._next_piece_surf = ui_next_piece.NextPieceSprite(
            self._board_surf.board_cell_width,
            self._next_piece)

    def ai_piece_render(self):
        if not self._hint:
            return
        self._ai_piece_surf = ui_ai_piece.AIPieceSprite(
            self._board_surf.board_cell_width,
            self._ai_piece
        )
        self._ai_piece_surf.rect.move_ip(
            self._board_surf.rect.left + self._ai_piece_x * self._board_surf.board_cell_width, 
            self._board_surf.rect.top)
        self._ai_piece_surf.rect.move_ip(
            0, (self._height - (self._ai_piece_y + 4)) * self._board_surf.board_cell_width)

    def drop_piece_render(self):
        self._drop_piece_surf = ui_drop_piece.DropPieceSprite(
            self._board_surf.board_cell_width,
            self._piece)
        self._drop_piece_surf.rect.move_ip(
            self._board_surf.rect.left + self._piece_x * self._board_surf.board_cell_width, 
            self._board_surf.rect.top)
        self._drop_piece_y = self._board.drop_height(
            self._piece_x, self._piece_y, self._piece)
        self._drop_piece_surf.rect.move_ip(
            0, (self._height - (self._drop_piece_y + 4)) * self._board_surf.board_cell_width)

    def on_piece_finalize(self):
        self._board.set_piece(self._piece_x, self._piece_y, self._piece)
        self._board.commit_transaction()
        self._debug_board_surf.update(self._debug)
        self._board_surf.update()
        self._score_surf.update()
        self.piece_init()

    def piece_drop(self):
        self._piece_y = self._board.drop_height(self._piece_x, self._piece_y, self._piece)
        self.on_piece_finalize()
        return

    def move_piece_down(self):
        new_x = self._piece_x
        new_y = self._piece_y - 1
        if (self._board.is_piece_out_of_bound(new_x, new_y, self._piece) or
                self._board.did_piece_collided_with_body(new_x, new_y, self._piece)):
            self.on_piece_finalize()
            return
        self._piece_x = new_x
        self._piece_y = new_y
        self._piece_surf.rect.move_ip(0, self._board_surf.board_cell_width)

    def move_piece_left(self):
        new_x = self._piece_x - 1
        new_y = self._piece_y
        if (self._board.is_piece_out_of_bound(new_x, new_y, self._piece)):
            return
        if (self._board.did_piece_collided_with_body(new_x, new_y, self._piece)):
            return
        self._piece_x = new_x
        self._piece_y = new_y
        self._piece_surf.rect.move_ip(-self._board_surf.board_cell_width, 0)
        self.drop_piece_render()

    def move_piece_right(self):
        new_x = self._piece_x + 1
        new_y = self._piece_y
        if (self._board.is_piece_out_of_bound(new_x, new_y, self._piece)):
            return
        if (self._board.did_piece_collided_with_body(new_x, new_y, self._piece)):
            return
        self._piece_x = new_x
        self._piece_y = new_y
        self._piece_surf.rect.move_ip(self._board_surf.board_cell_width, 0)
        self.drop_piece_render()

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
        self.drop_piece_render()

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.on_game_end()
            if event.key == K_DOWN:
                self.move_piece_down()
            if event.key == K_LEFT:
                self.move_piece_left()
            if event.key == K_RIGHT:
                self.move_piece_right()
            if event.key == K_UP:
                self.rotate_piece()
            if event.key == K_p:
                self._paused = ~self._paused
            if event.key == K_SPACE:
                self.piece_drop()
            if event.key == K_d:
                self._debug = ~self._debug
                self._debug_board_surf.update(self._debug)
            if event.key == K_a:
                self._auto = ~self._auto
            if event.key == K_h:
                self._hint = ~self._hint
                if self._hint:
                    self.ai_piece_render()
        elif event.type == self._PIECEDROP:
            if not self._paused:
                self.move_piece_down()
        elif event.type == self._AUTOPLAY:
            if self._auto:
                if self._ai_rotation_count > 0:
                    self.rotate_piece()
                    self._ai_rotation_count = self._ai_rotation_count - 1
                move_x = self._ai_piece_x - 4
                if move_x != 0:
                    if move_x < 0:
                        self.move_piece_left()
                        self._ai_piece_x = self._ai_piece_x + 1
                    else:
                        self.move_piece_right()
                        self._ai_piece_x = self._ai_piece_x - 1
                if self._ai_rotation_count == 0 and move_x == 0:
                    self.piece_drop()
        elif event.type == QUIT:
            self.on_game_end()

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._score_surf.surf, self._score_surf.rect)
        self._display_surf.blit(self._instructions_surf.surf, self._instructions_surf.rect)
        self._display_surf.blit(self._next_piece_surf.surf, self._next_piece_surf.rect)
        self._display_surf.blit(self._debug_board_surf.surf, self._debug_board_surf.rect)
        self._display_surf.blit(self._board_surf.surf, self._board_surf.rect)
        self._display_surf.blit(self._piece_surf.surf, self._piece_surf.rect)
        if self._ai_piece_surf:
            self._display_surf.blit(self._ai_piece_surf.surf, self._ai_piece_surf.rect)
        self._display_surf.blit(
            self._drop_piece_surf.surf, self._drop_piece_surf.rect)
        pygame.display.flip()
        self._clock.tick(FRAMERATE)

    def on_cleanup(self):
        pygame.quit()

    def on_game_end(self):
        self._running = False
        print(f"SCORE: {self._board.score}, LINES: {self._board.lines}")

    def on_execute(self):
        if self.on_init() == False:
            self.on_game_end()
            self._running = False
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    # fo = open("input_1000.txt", "w+")
    # for _ in range(1000):
    #     time.sleep(0.001)
    #     fo.write(str(random.randrange(7)) + "\n")
    # fo.close()
    app = TetrisGame()
    app.on_execute()
