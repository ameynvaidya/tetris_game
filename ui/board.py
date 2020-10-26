import pygame
import lib.board as b
import lib.piece as p
class BoardSprite(pygame.sprite.Sprite):
    def __init__(self, board: b.Board, screen_width: int, screen_height: int):
        super(BoardSprite, self).__init__() 
        width = board.width()
        height = board.height()
        self._board = board
        self.board_cell_width = int(screen_height * 0.9 / height)

        self._board_display_width = self.board_cell_width * width
        self._board_display_height = self.board_cell_width * height
        self.surf = pygame.Surface(
            (self._board_display_width, self._board_display_height))
        self.rect = self.surf.get_rect()
        self.update()

    def update(self) -> None:
        width = self._board.width()
        height = self._board.height()
        rect_left = self.surf.get_rect().left
        rect_top = self.surf.get_rect().top
        rect_bottom = self.surf.get_rect().bottom
        rect_right = self.surf.get_rect().right
        rect_width = self.surf.get_rect().width
        rect_height = self.surf.get_rect().height

        # fill Board surface
        self.surf.fill((100,100,100))

        for x in range(width):
            for y in range(height):
                if (self._board.get_grid(x, y, self._board._commited_grid) != 0):
                    cell_left = (rect_left + x * self.board_cell_width)
                    cell_top = (rect_top + (height - y - 1)
                                * self.board_cell_width)
                    pygame.draw.rect(
                        self.surf,
                        p.Piece.piece_color_map()[self._board.get_grid(x, y, self._board._commited_grid)],
                        (cell_left, cell_top, self.board_cell_width, self.board_cell_width))

        # inside grid (for reference)
        for i in range(width + 1):
            ref_line_x = (rect_left + i * self.board_cell_width)
            pygame.draw.line(
                self.surf,
                (50, 50, 50),
                (ref_line_x, rect_top),
                (ref_line_x, rect_bottom), 1)

        for i in range(height + 1):
            ref_line_y = (rect_top + i * self.board_cell_width)
            pygame.draw.line(
                self.surf,
                (50, 50, 50),
                (rect_left, ref_line_y),
                (rect_right, ref_line_y), 1)

    def height(self) -> int:
        return self._board_display_height

    def width(self) -> int:
        return self._board_display_width