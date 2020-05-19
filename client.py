import pygame
from network import Network
from player import Player
from button import Button
from textbox import *
from redrawWindowFunctions import f0, f1, f2, f3, f4, f5, f6

pygame.font.init()
width=1400
height=800 
win=pygame.display.set_mode((width, height))
pygame.display.set_caption("client")
   
btns=[Button("Rock",50,500,(0,0,255)),Button("Paper",250,500,(255,0,0)),Button("Scissors",450,500,(0,255,0))]
def main():
    clock = pygame.time.Clock()
    run=True
    n=Network()
    player=int(n.getP())
    print("You are player ", player)
    me=Player((0,255,0),"detective",player)
    if player==0:
        print("Role : Mr. X")
    else:
        print("Role : Detective")
    while(run):
        try:
            game=n.send("get")
        except:
            run=False
            print("No game found")
            break
        
        #try:
        if game.caught():
            f6(win, game, player)
        elif not game.connected():
            f0(win, game, player)
        elif game.allDetectivesWent():
            if player>0:
                f1(win, game, player)
            else:
                received_input=f2(win, game, player)
                #pre-process recv_input
                game=n.send(received_input)
                game=n.send("mrxplayed")
        else:
            if player==0:
                f3(win, game, player)
            elif game.detectivesWent[player-1]:
                f4(win, game, player)
            else:
                received_input=f5(win, game, player)
                #pre-process recv_input
                game=n.send(received_input)
                if game.allDetectivesWent():
                    game=n.send("detectivesplayed")
        """except:
            run=False
            print("No game found")
            break"""
                    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            

def menu_screen():
    run =True
    clock=pygame.time.Clock()
    while(run):
        clock.tick(30)
        win.fill((128,128,128))
        font=pygame.font.SysFont("comicsans", 60)
        text=font.render("Click to Play!",1,(255,0,0))
        win.blit(text,(100,200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                run=False
    main()

while True:
    menu_screen()