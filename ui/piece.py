import pygame
import lib.piece as piece

class PieceSprite(pygame.sprite.Sprite):
    def __init__(self, cell_width: int):
        super(PieceSprite, self).__init__()
        self.surf = pygame.Surface((cell_width*4, cell_width*4))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        