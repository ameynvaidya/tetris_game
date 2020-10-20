import pygame
import lib.board as b

class ScoreSprite(pygame.sprite.Sprite):
    def __init__(self, board: b.Board):
        super(ScoreSprite, self).__init__()

        pygame.font.init()

        self._board = board
        self.surf = pygame.Surface((150, 100))
        self.rect = self.surf.get_rect()
        self.update()

    def update(self):
        self.surf.fill((0, 0, 0))
        myfont = pygame.font.SysFont('Arial', 15)
        myfont.set_bold(True)
        score_text = myfont.render(
            f"SCORE : {self._board.score:05d}", False, (200, 200, 200))
        score_text_rect = score_text.get_rect()
        self.surf.blit(score_text, score_text_rect)
        lines_text = myfont.render(
            f"LINES : {self._board.lines:05d}", False, (200, 200, 200))
        lines_text_rect = lines_text.get_rect()
        lines_text_rect.move_ip(0, 30)
        self.surf.blit(lines_text, lines_text_rect)