import pygame
import lib.board as board

class BoardSprite(pygame.sprite.Sprite):
    def __init__(self, board: board.Board, screen_width: int, screen_height: int):
        super(BoardSprite, self).__init__()
        width = board.width()
        height = board.height()
        aspect_ratio = width / height
        self._board_display_height = int(screen_height * 0.9)
        self._board_display_width = int(
            aspect_ratio * self._board_display_height)
        self.surf = pygame.Surface(
            (self._board_display_width, self._board_display_height))
        piece_color = {
            1: (0, 255, 255),  # aqua Stick
            2: (0, 0, 255),   # blue  L Inverse
            3: (255, 165, 0),  # orange L
            4: (255, 255, 0),  # yellow Square
            5: (0, 255, 0),  # green S
            6: (217, 49, 255),  # purple Pyramid
            7: (255, 0, 0),  # red S Inverse
            0: (0, 0, 0),  # black blank
        }
        padding = 5
        rect_left = self.surf.get_rect().left + padding
        rect_top = self.surf.get_rect().top + padding
        rect_bottom = self.surf.get_rect().bottom - padding
        rect_right = self.surf.get_rect().right - padding
        rect_width = self.surf.get_rect().width - padding * 2
        rect_height = self.surf.get_rect().height - padding * 2

        # Outer boundry
        pygame.draw.rect(self.surf, (255, 255, 255), self.surf.get_rect(), 5)
        pygame.draw.rect(self.surf, (255, 255, 255), self.surf.get_rect(), 5)

        for x in range(width):
            for y in range(height):
                cell_left = (rect_left + x * rect_width/width)
                cell_top = (rect_top + (height - y - 1)
                            * rect_height/height)
                cell_width = cell_height = rect_width/width
                pygame.draw.rect(
                    self.surf,
                    piece_color[board.get_grid(x, y)],
                    (cell_left, cell_top, cell_width, cell_height))

        # inside grid (for reference)
        for i in range(1, width):
            ref_line_x = (rect_left + i*rect_width/width)
            pygame.draw.line(
                self.surf,
                (50, 50, 50),
                (ref_line_x, rect_top),
                (ref_line_x, rect_bottom), 1)

        for i in range(1, height):
            ref_line_y = (rect_top + i*rect_height/height)
            pygame.draw.line(
                self.surf,
                (50, 50, 50),
                (rect_left, ref_line_y),
                (rect_right, ref_line_y), 1)

    def height(self) -> int:
        return self._board_display_height

    def width(self) -> int:
        return self._board_display_width