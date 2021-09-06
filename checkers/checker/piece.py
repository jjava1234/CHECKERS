import pygame
class Piece():
    def __init__(self, window, x, y, color, dir, size=30):
        self.color = color
        self.king = False
        self.valid_moves = []
        self.dir = dir #row direction
        self.draw(window, x, y, color, 30)
        self.update(x, y)

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window, x, y, color, size):
        pygame.draw.circle(window, (color), (x*90 +45, y*90 +45), size)        

        

        

