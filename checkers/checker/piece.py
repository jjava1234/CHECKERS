from .constants import *

class Piece():
    def __init__(self, window, x, y, color, dir):
        self.color = color
        self.valid_moves = {}
        self.king = False        
        self.dir = dir #row direction
        self.size = 30
        self.update(x, y)
        self.draw()
    
    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x*90 +45, self.y*90 +45), self.size)        
        if self.king:
            win.blit(crown, ((self.x*90+45) - crown.get_width()//2, (self.y*90+45) - crown.get_height()//2))
