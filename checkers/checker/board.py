import pygame
from .piece import Piece

window = pygame.display.set_mode((720,720))
pygame.display.set_caption('Checkers')
pygame.init()

class Board():
    def __init__(self):
        self.board = []
        self.rows = self.columns = 8
    
    def draw_pieces():
        pass

    def draw_board(self):
    
        pygame.draw.rect(window, (111,78,55), (0,0, 720,720))

        for row in range(self.rows):
            self.board_layout.append([])
            for col in range((row+1)%2, self.rows, 2):
                    pygame.draw.rect(window, (210,180,140), (col*90,row*90, 90, 90))

    def     
    #pygame.draw.circle(window, (0,255,0), (column,row), 30)

