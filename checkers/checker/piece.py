class Piece():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 25
        self.king = False
        self.valid_moves = []
