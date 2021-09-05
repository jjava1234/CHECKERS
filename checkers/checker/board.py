from .piece import Piece, Moves, pygame
from .game import Game
window = pygame.display.set_mode((720,720))
pygame.display.set_caption('Checkers')
pygame.init()

class Board():


    def __init__(self):
        self.board_layout = []
        self.rows = 8
        self.cols = 8
        self.selected = None
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

        
        #self.draw_pieces()
        

    def draw_pieces(self):
        piece_group = pygame.sprite.Group()
        for row in self.board_layout:
            for piece in row:
                if piece:
                    piece_group.add(piece)    

        piece_group.draw(window)        
    #        for piece in row:
    #            if piece:
    #                pygame.draw.circle(window, piece.color, (piece.x*90 + 45, piece.y*90 + 45), 25)


    def draw_moves(self, valid_moves):
        moves_group = pygame.sprite.Group()
        for move in valid_moves:
            moves_group.add(Moves(move[0], move[1]))

        moves_group.draw(window)


    def undraw_moves(self, valid_moves):
        for move in valid_moves:
            pass


    def draw_board(self):
        pygame.draw.rect(window, (210,180,140), (0,0, 720,720))
        for row in range(self.rows):
            for col in range((row+1)%2, self.rows, 2):
                pygame.draw.rect(window, (111,78,55), (col*90,row*90, 90, 90))

        self.create_pieces()


    def move_piece(self):
        pass


    def calc_moves_left(self, piece, piece_x, piece_y, team):
        if piece_y not in (0,7) and piece_x != 0:
            x = piece_x-1
            y = piece_y+piece.dir   
            move = self.board_layout[y][x] 
            if move == 0: 
                piece.valid_moves.append((x, y))
            elif y+piece.dir != -1 and y+piece.dir != 8 and x-1 != -1:
                if move.color != team and self.board_layout[y+piece.dir][x-1] == 0:
                    piece.valid_moves.append((x, y))
                    self.calc_moves_left(piece, x-1, y+piece.dir, team)


    def calc_moves_right(self, piece):
        for row in range(self.rows):
            for col in range(self.cols):
                if piece.y not in (0,7) and piece.x != 7:  
                    if not self.board_layout[piece.y+ piece.dir][piece.x+1]:
                        pass
    

    def select(self, x, y, turn):
        piece = self.board_layout[y//90][x//90]
        if not self.selected:
            if piece and piece.color == turn:
                self.selected = piece
                self.calc_moves_left(piece, piece.x, piece.y, piece.color)
                #self.calc_moves_right(piece, piece.x, piece.y, piece.color)
                self.draw_moves(piece.valid_moves)
        else:
            if piece and piece.color == turn:
                if piece != self.selected:
                    self.undraw_moves(self.selected.valid_moves)
                    self.selected = False
                    self.select(piece.x*90, piece.y*90, turn)
                    
            elif (piece.x, piece.y) in self.selected.valid_moves:
                self.move_piece(piece.x, piece.y)
                self.selected.valid_moves = []
                self.selected = None
             

