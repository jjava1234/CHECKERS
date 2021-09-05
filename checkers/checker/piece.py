import pygame
class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, color, dir, size=30):
        super().__init__()
        self.image = pygame.Surface((80,80), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (color), (40,40), size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x*90 +45
        self.rect.centery = y*90 +45
        self.x = x 
        self.y = y
        self.color = color
        self.king = False
        self.valid_moves = []
        self.dir = dir #row direction

class Moves(Piece):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 0, 255), 0) 
    
        

