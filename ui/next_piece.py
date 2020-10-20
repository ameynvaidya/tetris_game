import pygame
import lib.piece as pc
import lib.board as b
import ui.piece as ui_piece

class NextPieceSprite(pygame.sprite.Sprite):
    def __init__(self, cell_width: int, piece : pc.Piece):
        super(NextPieceSprite, self).__init__()

        pygame.font.init()

        self._cell_width = cell_width
        self._piece = piece
        self.surf = pygame.Surface((cell_width * 6, cell_width * 5))
        self.rect = self.surf.get_rect()
        self.update()

    def update(self):
        self.surf.fill((0, 0, 0))
        myfont = pygame.font.SysFont('Arial', 15)
        myfont.set_bold(True)
        label_text = myfont.render("NEXT", False, (200, 200, 200))
        label_text_rect = label_text.get_rect()
        label_text_rect.move_ip(self._cell_width, self._cell_width)
        self.surf.blit(label_text, label_text_rect)
        self._piece_surf = ui_piece.PieceSprite(
            self._cell_width,
            self._piece)
        self._piece_surf.rect.move_ip(self._cell_width, self._cell_width)
        self.surf.blit(self._piece_surf.surf, self._piece_surf.rect)
