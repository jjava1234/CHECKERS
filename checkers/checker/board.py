import pygame
from .piece import Piece
from .game import Game
window = pygame.display.set_mode((720,720))
pygame.display.set_caption('Checkers')
pygame.init()

class Board():


    def __init__(self):
        self.board_layout = []
        self.rows = 8
        self.cols = 8
        self.game = Game()
        self.draw_board()

    def create_pieces(self):
        for row in range(self.rows):
            self.board_layout.append([])
            for col in range(self.cols):
                if (row+1)%2 == col%2: 
                    if row < 3:
                        self.board_layout[row].append(Piece(col, row, (255,0,0), 1))
                    elif row > 4:
                        self.board_layout[row].append(Piece(col, row, (0,0,0), -1))
                    else: 
                        self.board_layout[row].append(0)
                else:
                    self.board_layout[row].append(0)
        self.draw_pieces()
        

    def draw_pieces(self):

        for row in self.board_layout:
            for piece in row:
                if piece:
                    pygame.draw.circle(window, piece.color, (piece.x*90 + 45, piece.y*90 + 45), 25)



    def draw_board(self):
        pygame.draw.rect(window, (210,180,140), (0,0, 720,720))
        for row in range(self.rows):
            for col in range((row+1)%2, self.rows, 2):
                pygame.draw.rect(window, (111,78,55), (col*90,row*90, 90, 90))
        
        self.create_pieces()

    def calc_moves_left(self, piece, x, y):
        if piece.y not in (0,7) and piece.x != 0:
            x = piece.x-1
            y = piece.y+piece.dir   
            piece = self.board_layout[y][x] 
            if piece == 0: 
                piece.valid_moves.append[y][x]
            elif piece.dir not in (0,7) and x-1 != 0:
                if piece.color == (0,0,0) and self.board_layout[y+piece.dir][x-1] == 0:
                    piece.valid_moves.append[y][x]
                    self.calc_moves_left(piece, x-1, y+piece.dir)

     
    def calc_moves_right(self, piece):
        for row in range(self.rows):
            for col in range(self.cols):
                if piece.y not in (0,7) and piece.x != 7:  
                    if not self.board_layout[piece.y+ piece.dir][piece.x+1]:
                        


    def validate_move(self, piece, x, y):
        pass
    
    def select(self, x, y):
        if piece := self.board_layout[y//90][x//90] and self.game.turn == "red":
            if (piece.x, piece.y) in piece.valid_moves:
                return piece.valid_moves

            self.calc_moves_left(piece)
            self.calc_moves_right(piece)
             
