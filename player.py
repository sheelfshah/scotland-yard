import pygame

# ammend full file later
def get_coordinates(pos):
    return (pos*50,pos*50)  

def valid_move(initPos,finPos):
    return True     

class Player():
    def __init__(self,color,role,pos):
        self.color=color
        self.role=role
        self.pos=pos
        self.coordinates=get_coordinates(pos)
        self.rect=(self.coordinates[0],self.coordinates[1],25,25)

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self,pos):
        if valid_move(self.pos,pos):
            self.pos=pos
            self.coordinates=get_coordinates(pos)
            self.update()
            return True
        return False

    def update(self):
        self.rect=(self.coordinates[0],self.coordinates[1],25,25)
