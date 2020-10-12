import pygame
import lib.board as bo
import lib.piece as pc


class DebugBoardSprite(pygame.sprite.Sprite):
    def __init__(self, cell_width: int, board: bo.Board):
        super(DebugBoardSprite, self).__init__()

        pygame.font.init()

        self._board = board
        self._cell_width = cell_width

        width = board.width()
        height = board.height()

        self.surf = pygame.Surface((
            cell_width * (width + 2),
            cell_width * (height + 2)))
        self.rect = self.surf.get_rect()
        self.update()



    def update(self, debug=False):
        self.surf.fill((160, 160, 160))
        if not debug:
            return
        width = self._board.width()
        height = self._board.height()
        myfont = pygame.font.SysFont('Arial', 15)
        myfont.set_bold(True)

        for i in range(height):
            row_num_surface = myfont.render(f"{i:02d}", False, (0, 0, 0))
            row_num_surface_rect = row_num_surface.get_rect()
            row_num_surface_rect.move_ip(3, (height - i) * self._cell_width)
            self.surf.blit(row_num_surface, row_num_surface_rect)

            row_stat_surface = myfont.render(
                f"{self._board.row_stats[i]:02d}", False, (255, 0, 0))
            row_stat_surface_rect = row_stat_surface.get_rect()
            row_stat_surface_rect.move_ip(
                self._cell_width * (width + 1) + 3, (height - i) * self._cell_width)
            self.surf.blit(row_stat_surface, row_stat_surface_rect)
