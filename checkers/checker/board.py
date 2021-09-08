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
        self.CL = self.CR = False #capture left abbreviation and capture right abbreviation

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
            

    def undraw_moves(self, valid_moves):
        for move in valid_moves:
            if move[0]%2 == move[1]%2:
                pygame.draw.rect(window, (210,180,140), (move[0]*90, move[1]*90, 90,90))            
            else:
                pygame.draw.rect(window, (111,78,55), (move[0]*90, move[1]*90, 90, 90))
                
    def undraw_piece(self, x, y):
            if x%2 == y%2:
                pygame.draw.rect(window, (210,180,140), (x*90, y*90, 90,90))            
            else:
                pygame.draw.rect(window, (111,78,55), (x*90, y*90, 90, 90))

    def redraw_pieces(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if piece := self.board_layout[row][col]:
                    piece.draw(window, col, row, piece.color, 30)



    def draw_moves(self, valid_moves):
        for valid_move in valid_moves:
            pygame.draw.circle(window, (0,0,255), (valid_move[0]*90 + 45, valid_move[1]*90 + 45), 15)


    def draw_board(self):
        pygame.draw.rect(window, (210,180,140), (0,0, 720,720))
        for row in range(self.rows):
            for col in range((row+1)%2, self.rows, 2):
                pygame.draw.rect(window, (111,78,55), (col*90,row*90, 90, 90))
        if not self.board_layout:
            self.create_pieces()
        self.redraw_pieces()


    def switch_turns(self, player):
        self.selected.valid_moves.clear()
        self.selected = None
        self.CL = self.CR = False
        self.turn = self.game.players[(self.game.players.index(player)+1)%2]

    def check_board(self, valid_move):
        if pos := self.selected.valid_moves[valid_move]:
            print("BOARD LAYOUT:", self.board_layout[pos[1]][pos[0]])
            self.board_layout[pos[1]][pos[0]] = 0
            #print("NEW LAYOUT IS:", self.board_layout[pos[1]][pos[0]])
            return True
        print("RETURNED FALSE")
        return False


    def move_piece(self, piece, valid_move, player):
        
        # check if a capture occured
        pCaptured = self.check_board(valid_move) # pCaptured abbr. for piece captured
        
        self.selected.valid_moves.clear()
        # swap piece position and empty ("0") position in board layout
        self.board_layout[valid_move[1]][valid_move[0]], self.board_layout[piece.y][piece.x] = self.board_layout[piece.y][piece.x], self.board_layout[valid_move[1]][valid_move[0]]
        # update piece's x and y values
        self.board_layout[valid_move[1]][valid_move[0]].update(valid_move[0], valid_move[1])
        
        self.draw_board()
        
        if (self.CL or self.CR) and pCaptured:
            self.calc_moves_left(piece, piece.x, piece.y, piece.color, pCaptured)
            self.calc_moves_right(piece, piece.x, piece.y, piece.color, pCaptured)                             

        if not self.selected.valid_moves:
            self.switch_turns(player)
            print(self.turn)

        else:
            self.draw_moves(self.selected.valid_moves)
            


    def calc_moves_left(self, piece, piece_x, piece_y, team, pCaptured = False):
        x = piece_x-1
        y = piece_y+piece.dir 
        if y > -1 and y < 8 and x > -1:
            move = self.board_layout[y][x] 
            #print("PIECE RIGHT:", x,y, "MOVE:", move)
            if move == 0:
                if not self.CL and not pCaptured:
                    piece.valid_moves[(x, y)] = None

            elif y+piece.dir > -1 and y+piece.dir < 8 and x-1 > -1:
                if move.color != team and self.board_layout[y+piece.dir][x-1] == 0:
                    piece.valid_moves[(x-1, y+piece.dir)] = (x,y)
                    self.CL = True

    def calc_moves_right(self, piece, piece_x, piece_y, team, pCaptured = False):
        x = piece_x+1
        y = piece_y+piece.dir
        if y > -1 and y < 8 and x < 8:
            move = self.board_layout[y][x] 
            #print("PIECE LEFT:", x,y, "MOVE", move)
            if move == 0:
                if not self.CR and not pCaptured:
                    piece.valid_moves[(x, y)] = None

            elif y+piece.dir > -1 and y+piece.dir < 8 and x+1 < 8:
                if move.color != team and self.board_layout[y+piece.dir][x+1] == 0:
                    # value of dictionary == captured piece's pos
                    piece.valid_moves[(x+1, y+piece.dir)] = (x,y) 
                    
                    self.CR = True



    def select(self, x, y):
        piece = self.board_layout[y//90][x//90]
        player = self.turn

        # if piece instance and no piece is already selected
        if piece and piece != self.selected:
            if piece.color == player:
                # if player selects a different piece
                if self.selected:
                    self.undraw_moves(self.selected.valid_moves)
                    self.selected.valid_moves.clear()
                    self.CL = self.CR = False
                self.selected = piece
                self.calc_moves_left(piece, piece.x, piece.y, piece.color)
                self.calc_moves_right(piece, piece.x, piece.y, piece.color)
                self.draw_moves(piece.valid_moves)

        # if player selects a move
        else:
            if self.selected:
                for valid_move in self.selected.valid_moves:
                    if (x//90, y//90) == valid_move:
                        self.undraw_piece(self.selected.x, self.selected.y)
                        self.undraw_moves(self.selected.valid_moves)
                        self.move_piece(self.selected, valid_move, player)
                        break            
                    
