import copy
from .piece import Piece, pygame

window = pygame.display.set_mode((720,720))
pygame.display.set_caption('Checkers')
pygame.init()
        
class Board():
    def __init__(self, game):
        self.board_layout = []
        self.rows = 8
        self.cols = 8
        self.game = game
        self.turn = game.players[0]
        self.selected = None

        self.draw_board()
        self.DJL = self.DJR = False #double jumping left abbreviation and double jumping right abbreviation

    def create_pieces(self):
        for row in range(self.rows):
            self.board_layout.append([])
            for col in range(self.cols):
                if (row+1)%2 == col%2: 
                    if row < 3:
                        self.board_layout[row].append(Piece(window, col, row, (255,0,0), 1))
                    elif row > 4:
                        self.board_layout[row].append(Piece(window, col, row, (0,0,0), -1))
                    else: 
                        self.board_layout[row].append(0)
                else:
                    self.board_layout[row].append(0)
            

    def redraw_pieces(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if piece := self.board_layout[row][col]:
                    piece.draw(window, col, row, piece.color, 30)



    def draw_moves(self, valid_moves):
        for move in valid_moves:
            pygame.draw.circle(window, (0,0,255), (move[0]*90 + 45, move[1]*90 + 45), 15)


    def undraw_moves(self, valid_moves):
        pass
        for move in valid_moves:
            if move[0]%2 == move[1]%2:
                pygame.draw.rect(window, (210,180,140), (move[0]*90, move[1]*90, 90,90))            
            else:
                pygame.draw.rect(window, (111,78,55), (move[0]*90, move[1]*90, 90, 90))

    def draw_board(self):
        pygame.draw.rect(window, (210,180,140), (0,0, 720,720))
        for row in range(self.rows):
            for col in range((row+1)%2, self.rows, 2):
                pygame.draw.rect(window, (111,78,55), (col*90,row*90, 90, 90))
        if not self.board_layout:
            self.create_pieces()
        self.redraw_pieces()


    def move_piece(self, piece, valid_move, playerColor):

        #swap piece position and "0" position in board layout 
        self.board_layout[valid_move[1]][valid_move[0]], self.board_layout[piece.y][piece.x] = self.board_layout[piece.y][piece.x], 0
        #update piece's x and y values
        self.board_layout[valid_move[1]][valid_move[0]].update(valid_move[0], valid_move[1])
        self.draw_board()
        

        if self.DJL or self.DJR:
            #self.board_layout[piece.y+piece.dir][piece.x +(piece.x - valid_move[0] + 1)] = 0
            #if playerColor == (0,0,0):
            #    self.game.red_count -= 1
            #else:
            #    self.game.black_count -= 1
            self.select(valid_move[0], valid_move[1])
        else:
            self.selected.valid_moves.clear()
            self.selected = None
            self.turn = self.game.players[(self.game.players.index(playerColor)+1)%2]


    def calc_moves_left(self, piece, piece_x, piece_y, team):
        x = piece_x-1
        y = piece_y+piece.dir 
        if y not in (-1, 8) and x != -1:
            move = self.board_layout[y][x] 
            if move == 0:
                if not self.DJL:
                    piece.valid_moves.append((x, y))
                else:
                    self.DJL = False
            elif move.color != team and self.board_layout[y+piece.dir][x-1] == 0:
                piece.valid_moves.append((x-1, y+piece.dir))
                self.DJL = True
                

    def calc_moves_right(self, piece, piece_x, piece_y, team):
        x = piece_x+1
        y = piece_y+piece.dir
        if y+piece.dir not in (-1, 8) and piece_x+1 != 8:
            move = self.board_layout[y][x] 
            if move == 0:
                if not self.DJR:
                    piece.valid_moves.append((x, y))
                else: 
                    self.DJR = False
            elif move.color != team and self.board_layout[y+piece.dir][x+1] == 0:
                piece.valid_moves.append((x+1, y+piece.dir))
                self.DJR = True


    def select(self, x, y):
        piece = self.board_layout[y//90][x//90]
        if not piece:
            x = x//90
            y = y//90
        playerColor = self.turn
        #if no piece is already selected 
        if not self.selected:
            if piece and piece.color == playerColor:
                self.selected = piece
                self.calc_moves_left(piece, piece.x, piece.y, piece.color)
                if not piece.valid_moves:
                    self.DJL = False
                self.calc_moves_right(piece, piece.x, piece.y, piece.color)
                if not piece.valid_moves:
                    self.DJR = False                
                #if statement is for double jumping 
                if piece.valid_moves:
                    self.draw_moves(piece.valid_moves)

        else:
            print(self.selected.valid_moves)

            #if player clicks on a different piece
            if piece and piece.color == playerColor:
                if piece != self.selected:
                    self.undraw_moves(self.selected.valid_moves)
                    self.selected = None
                    self.select(piece.x*90, piece.y*90)
            #if player selects a move
            elif (x, y) in self.selected.valid_moves:
                self.move_piece(self.selected, (x, y), playerColor)

             


             

