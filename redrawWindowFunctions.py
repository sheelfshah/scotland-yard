import pygame
from textbox import *
from move_validator import taxi_move, bus_move, underground_move, blackticket_move, ticket_checker
from get_coordinates import get_coordinates

width=1400
height=800

coordinates=get_coordinates()
colors=[
    (255,255,255),
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,0,255),
    (0,255,255),
]

def f6(win,game,p):
    win.fill((50,50,205))
    font=pygame.font.SysFont("comicsans",80)
    text=font.render("Mr. X was caught at position: "+str(game.moves[0]),1,(255,255,255),True)
    win.blit(text,(width/2-text.get_width()/2,height/2-text.get_height()/2))
    pygame.display.update()

def f0(win,game,p):
    win.fill((128,128,128))
    font=pygame.font.SysFont("comicsans",80)
    text=font.render("Waiting for "+str(6-game.ready)+" more players to join",1,(255,0,0),True)
    win.blit(text,(width/2-text.get_width()/2,height/2-text.get_height()/2))
    pygame.display.update()

def f1(win,game,player):
    win.fill((128,128,128))
    picture = pygame.image.load("bm5.jpg")
    picture = pygame.transform.scale(picture, (1200, 730))
    picture_rect = picture.get_rect()
    picture_rect = picture_rect.move((0, 70))
    win.blit(picture, picture_rect)
    text_top="Waiting for Mr. X to move"
    text_top_left=""
    text_top_right="Your Position: "+ str(game.moves[player])
    font=pygame.font.SysFont("comicsans", 60)
    text_top=font.render(text_top,1,(255,255,255))
    win.blit(text_top,(width/2-text_top.get_width()/2,5))
    text_top_left=font.render(text_top_left,1,(255,255,255))
    win.blit(text_top_left,(5,5))
    font=pygame.font.SysFont("comicsans", 40)
    text_top_right=font.render(text_top_right,1,colors[player])
    win.blit(text_top_right,(1100,5))
    text_bottom_right=get_ticket_text(game,player)
    for i in range(3):
        tbr=font.render(text_bottom_right[i],1,(255,255,255))
        win.blit(tbr,(1250,600+i*42))
    for j in range(5):
        i=game.moves[j+1]
        pygame.draw.rect(win, colors[j+1], (coordinates[i-1][0]-12, coordinates[i-1][1]-12, 24, 24),3)
    text_middle_right=["Last known"]
    text_middle_right+=["position: "]
    text_middle_right+=[str(game.lastKnownMove)]
    for i in range(3):
        tmb=font.render(text_middle_right[i],1,(255,255,255))
        win.blit(tmb,(1220,250+i*42))
    pygame.display.update()

def f2(win,game,player):
    while True:
        win.fill((128,128,128))
        picture = pygame.image.load("bm5.jpg")
        picture = pygame.transform.scale(picture, (1200, 730))
        picture_rect = picture.get_rect()
        picture_rect = picture_rect.move((0, 70))
        win.blit(picture, picture_rect)
        text_top="Waiting for Mr. X to move"
        text_top_left=""
        text_top_right="Your Position: "+ str(game.moves[player])
        font=pygame.font.SysFont("comicsans", 60)
        text_top=font.render(text_top,1,(255,255,255))
        win.blit(text_top,(width/2-text_top.get_width()/2,5))
        text_top_left=font.render(text_top_left,1,(255,255,255))
        win.blit(text_top_left,(5,5)) 
        font=pygame.font.SysFont("comicsans", 40)
        text_top_right=font.render(text_top_right,1,colors[player])
        win.blit(text_top_right,(1100,45))
        text_bottom_right=get_ticket_text(game,player)
        for i in range(5):
            tbr=font.render(text_bottom_right[i],1,(255,255,255))
            win.blit(tbr,(1250,550+i*42))
        for j in range(-1,5):
            i=game.moves[j+1]
            pygame.draw.rect(win, colors[j+1], (coordinates[i-1][0]-12, coordinates[i-1][1]-12, 24, 24),3)
        text_middle_right=["Last known"]
        text_middle_right+=["position: "]
        text_middle_right+=[str(game.lastKnownMove)]
        for i in range(3):
            tmb=font.render(text_middle_right[i],1,(255,255,255))
            win.blit(tmb,(1220,250+i*42))
        pygame.display.update()
        textBox = TextBox(30)
        shiftDown = False
        if not game.mrxWent:
            input_string=get_input_textBox(textBox, win)
            if is_valid(input_string, player, game.moves[player], game):
                pygame.display.update()
                return input_string 

def f3(win,game,player):
    win.fill((128,128,128))
    picture = pygame.image.load("bm5.jpg")
    picture = pygame.transform.scale(picture, (1200, 730))
    picture_rect = picture.get_rect()
    picture_rect = picture_rect.move((0, 70))
    win.blit(picture, picture_rect)
    text_top="Waiting for all detectives to move"
    text_top_left=game.mrxVehicle
    text_top_right="Your Position: "+ str(game.moves[player])
    font=pygame.font.SysFont("comicsans", 60)
    text_top=font.render(text_top,1,(255,255,255))
    font=pygame.font.SysFont("comicsans", 40)
    win.blit(text_top,(width/2-text_top.get_width()/2-100,5))
    text_top_left=font.render(text_top_left,1,(255,255,255))
    win.blit(text_top_left,(5,45))
    text_top_right=font.render(text_top_right,1,colors[player])
    win.blit(text_top_right,(1100,5))
    text_bottom_right=get_ticket_text(game,player)
    for i in range(5):
        tbr=font.render(text_bottom_right[i],1,(255,255,255))
        win.blit(tbr,(1250,550+i*42))
    for j in range(-1,5):
        i=game.moves[j+1]
        pygame.draw.rect(win, colors[j+1], (coordinates[i-1][0]-12, coordinates[i-1][1]-12, 24, 24),3)
    text_middle_right=["Last known"]
    text_middle_right+=["position: "]
    text_middle_right+=[str(game.lastKnownMove)]
    for i in range(3):
        tmb=font.render(text_middle_right[i],1,(255,255,255))
        win.blit(tmb,(1220,250+i*42))
    pygame.display.update()

def f4(win,game,player):
    win.fill((128,128,128))
    picture = pygame.image.load("bm5.jpg")
    picture = pygame.transform.scale(picture, (1200, 730))
    picture_rect = picture.get_rect()
    picture_rect = picture_rect.move((0, 70))
    win.blit(picture, picture_rect)
    text_top="Waiting for all detectives to move"
    text_top_left=game.mrxVehicle
    text_top_right="Your Position: "+ str(game.moves[player])
    font=pygame.font.SysFont("comicsans", 60)
    text_top=font.render(text_top,1,(255,255,255))
    font=pygame.font.SysFont("comicsans", 40)
    win.blit(text_top,(width/2-text_top.get_width()/2-100,5))
    text_top_left=font.render(text_top_left,1,(255,255,255))
    win.blit(text_top_left,(5,45))
    text_top_right=font.render(text_top_right,1,colors[player])
    win.blit(text_top_right,(1100,5))
    text_bottom_right=get_ticket_text(game,player)
    for i in range(3):
        tbr=font.render(text_bottom_right[i],1,(255,255,255))
        win.blit(tbr,(1250,600+i*42))
    for j in range(5):
        i=game.moves[j+1]
        pygame.draw.rect(win, colors[j+1], (coordinates[i-1][0]-12, coordinates[i-1][1]-12, 24, 24),3)
    text_middle_right=["Last known"]
    text_middle_right+=["position: "]
    text_middle_right+=[str(game.lastKnownMove)]
    for i in range(3):
        tmb=font.render(text_middle_right[i],1,(255,255,255))
        win.blit(tmb,(1220,250+i*42))
    pygame.display.update()

def f5(win,game,player):
    while True:
        win.fill((128,128,128))
        picture = pygame.image.load("bm5.jpg")
        picture = pygame.transform.scale(picture, (1200, 730))
        picture_rect = picture.get_rect()
        picture_rect = picture_rect.move((0, 70))
        win.blit(picture, picture_rect)
        text_top="Waiting for all detectives to move"
        text_top_left=game.mrxVehicle
        text_top_right="Your Position: "+ str(game.moves[player])
        font=pygame.font.SysFont("comicsans", 60)
        text_top=font.render(text_top,1,(255,255,255))
        win.blit(text_top,(width/2-text_top.get_width()/2-100,5))
        font=pygame.font.SysFont("comicsans", 40)
        text_top_left=font.render(text_top_left,1,(255,255,255))
        win.blit(text_top_left,(5,45))
        font=pygame.font.SysFont("comicsans", 40)
        text_top_right=font.render(text_top_right,1,colors[player])
        win.blit(text_top_right,(1100,45))
        text_bottom_right=get_ticket_text(game,player)
        for i in range(3):
            tbr=font.render(text_bottom_right[i],1,(255,255,255))
            win.blit(tbr,(1250,600+i*42))
        for j in range(5):
            i=game.moves[j+1]
            pygame.draw.rect(win, colors[j+1], (coordinates[i-1][0]-12, coordinates[i-1][1]-12, 24, 24),3)
        text_middle_right=["Last known"]
        text_middle_right+=["position: "]
        text_middle_right+=[str(game.lastKnownMove)]
        for i in range(3):
            tmb=font.render(text_middle_right[i],1,(255,255,255))
            win.blit(tmb,(1220,250+i*42))
        pygame.display.update()
        textBox = TextBox(30)
        shiftDown = False
        if not game.detectivesWent[player-1]:
            input_string=get_input_textBox(textBox, win)
            if is_valid(input_string,player, game.moves[player], game):
                pygame.display.update()
                return input_string 

def is_valid(string, player, prev_pos, game):
    string=string.lower()
    if player>0:
        if string[0]=="t":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return taxi_move(prev_pos, pos,player, game)
        elif string[0]=="b":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return bus_move(prev_pos, pos,player, game)
        elif string[0]=="u":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return underground_move(prev_pos, pos,player, game)
        else:
            return False
    else:
        if string[0]=="t":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return taxi_move(prev_pos, pos,player, game)
        elif string[0]=="b":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return bus_move(prev_pos, pos,player, game)
        elif string[0]=="u":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return underground_move(prev_pos, pos,player, game)
        elif string[0]=="x":
            pos=string[1:]
            try:
                pos=int(pos)
            except:
                return False
            return (blackticket_move(prev_pos, pos,player, game))
        elif string[0]=="2":
            pos_list=string[1:].split()
            if len(pos_list)==2:
                if game.transports[player][4]==0:
                    return False
                elif(is_valid(pos_list[0],player,prev_pos, game) and is_valid(pos_list[1],player,int(pos_list[0][1:]), game)):
                    return ticket_checker(pos_list[0][0],player, game, pos_list[1][0])
            return False
        else:
            return False

def get_ticket_text(game,player):
    if player>0:
        tickets=game.transports[player]
        ans= ["T: "+str(tickets[0])]
        ans+=["B: "+str(tickets[1])]
        ans+=["U: "+str(tickets[2])]
        return ans
    else:
        tickets=game.transports[player]
        ans= ["T: "+str(tickets[0])]
        ans+=["B: "+str(tickets[1])]
        ans+=["U: "+str(tickets[2])]
        ans+=["X: "+str(tickets[3])]
        ans+=["2: "+str(tickets[4])]
        return ans

"""def redrawWindow(win,game,p,n):
    win.fill((128,128,128))
    if not game.connected():
        font=pygame.font.SysFont("comicsans",80)
        text=font.render("Waiting for "+str(6-game.ready)+" more players to join",1,(255,0,0),True)
        win.blit(text,(width/2-text.get_width()/2,height/2-text.get_height()/2))
    else:
        picture = pygame.image.load("bm3.jpg")
        picture = pygame.transform.scale(picture, (1200, 600))
        picture_rect = picture.get_rect()
        picture_rect = picture_rect.move((0, 100))
        win.blit(picture, picture_rect)
        if game.allDetectivesWent():
            text_top="Waiting for Mr. X to move"
            text_top_left=""
            if p==0:
                textBox = TextBox(30)
                shiftDown = False
                if not game.mrxWent:
                    input_string=get_input_textBox(textBox, win)
                    if is_valid(input_string):
                        game=n.send(input_string)
        else:
            text_top="Waiting for all detectives to move"
            text_top_left="Vehicle"
            if not p==0:
                textBox = TextBox(30)
                shiftDown = False
                if not game.detectivesWent[p-1]:
                    print("not received")
                    input_string=get_input_textBox(textBox, win)
                    if is_valid(input_string):
                        game=n.send(input_string)
                else:
                    print("received")
        font=pygame.font.SysFont("comicsans", 60)
        text_top=font.render(text_top,1,(255,255,255))
        win.blit(text_top,(width/2-text_top.get_width()/2,5))
        text_top_left=font.render(text_top_left,1,(255,255,255))
        win.blit(text_top_left,(5,5))
        
    pygame.display.update()"""