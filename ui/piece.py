import pygame
import lib.piece as pc
import lib.point as pt

class PieceSprite(pygame.sprite.Sprite):
    def __init__(self, cell_width: int, piece: pc.Piece):
        super(PieceSprite, self).__init__()
        self.piece_width = 4
        self.surf = pygame.Surface((cell_width * self.piece_width, cell_width * self.piece_width), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        for point in piece.getBody():
            point_left = self.rect.left + point.getX() * cell_width
            point_top = self.rect.top + (4 - point.getY() - 1) * cell_width
            pygame.draw.rect(
                self.surf, 
                pc.Piece.piece_color_map()[piece.getColor()],
                (point_left, point_top, cell_width, cell_width),
            )
            pygame.draw.rect(
                self.surf, 
                (50,50,50),
                (point_left, point_top, cell_width, cell_width),
                1
            )
        # Render border for the piece
        # for i in range(self.piece_width + 2):
        #     ref_line_x = self.rect.left + i * cell_width - 1
        #     pygame.draw.line(
        #         self.surf,
        #         (0, 0, 0),
        #         (ref_line_x, self.rect.top),
        #         (ref_line_x, self.rect.bottom), 2)

        # for i in range(self.piece_width + 2):
        #     ref_line_y = self.rect.top + i * cell_width - 1
        #     pygame.draw.line(
        #         self.surf,
        #         (0, 0, 0),
        #         (self.rect.left, ref_line_y),
        #         (self.rect.right, ref_line_y), 2)


