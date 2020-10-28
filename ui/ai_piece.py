import pygame
import lib.piece as pc
import lib.point as pt

class AIPieceSprite(pygame.sprite.Sprite):
    def __init__(self, cell_width: int, piece: pc.Piece):
        super(AIPieceSprite, self).__init__()
        self.piece_width = 4
        self.surf = pygame.Surface((cell_width * self.piece_width, cell_width * self.piece_width), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        for point in piece.getBody():
            point_left = self.rect.left + point.getX() * cell_width
            point_top = self.rect.top + (4 - point.getY() - 1) * cell_width
            pygame.draw.rect(
                self.surf, 
                (20,20,20),
                (point_left, point_top, cell_width, cell_width),
                2
            )