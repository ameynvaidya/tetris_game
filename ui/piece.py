import pygame
import lib.piece as pc
import lib.point as pt

class PieceSprite(pygame.sprite.Sprite):
    def __init__(self, cell_width: int, piece: pc.Piece):
        super(PieceSprite, self).__init__()
        self.surf = pygame.Surface((cell_width * 4, cell_width * 4), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        for point in piece.getBody():
            point_left = self.rect.left + point.getX() * cell_width
            point_top = self.rect.top + (4 - point.getY() - 1) * cell_width
            pygame.draw.rect(
                self.surf, 
                pc.Piece.piece_color_map()[piece.getColor()],
                (point_left, point_top, cell_width, cell_width)
            )


