import pygame
from checker.game import Game
from checker.board import Board 

def main():
    run = True
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()                          
                Board.validate_move(pos[0]/90, pos[1]/90)
    


        pygame.display.update()                
        Game()    

    pygame.quit()


main()