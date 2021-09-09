from .constants import *
from .board import Board

class Game():
    def __init__(self):
        self.turn = "red"
        self.red_count = self.black_count = 12
        self.players = [(255,0,0), (0,0,0)]
        self.winner = None

    def restart(self):
        wColor = colors[self.winner]
        win.fill(wColor)
        
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 80)
        winnerText = font.render(self.winner.upper() + " WON", False, (255,255,0))
        win.blit(winnerText, (720//2 - winnerText.get_width()//2, 720//2 - winnerText.get_height()//2))
        
        crown = pygame.transform.scale(pygame.image.load('checker/asset/crown.png'), (220, 125))
        win.blit(crown, (720//2 - crown.get_width()//2, 720//2 - winnerText.get_height() - 80))

        font = pygame.font.SysFont('Comic Sans MS', 20)
        restartText = font.render("press anywhere to restart", False, (255,255,0))
        win.blit(restartText, (720//2 - restartText.get_width()//2, 720/2 + 80))
        
