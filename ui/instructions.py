import pygame

class InstructionsSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(InstructionsSprite, self).__init__()
        pygame.font.init()
        self.surf = pygame.Surface((200, 200))
        self.rect = self.surf.get_rect()

        self.surf.fill((0, 0, 0))
        myfont = pygame.font.SysFont('Arial', 15)
        myfont.set_bold(True)
        lines = []
        lines.append(u"\u2191" + ": Rotate")
        lines.append(u"\u2190" + ": Move Left")
        lines.append(u"\u2192" + ": Move Right")
        lines.append(u"\u2193" + ": Move Down Quickly")
        lines.append("SPACE : Drop Piece")
        lines.append("H : Toggle Hint")
        lines.append("A : Toggle Auto Play")

        i = 0
        for l in lines:
            instructions_text = myfont.render(l, False, (200, 200, 200))
            instructions_text_rect = instructions_text.get_rect()
            instructions_text_rect.move_ip(0, i * 30)
            self.surf.blit(instructions_text, instructions_text_rect)
            i = i + 1