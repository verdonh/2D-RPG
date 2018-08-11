import pygame
from lib.colour import *
from lib.addons import pointcheck
#print(help(collide))

def button(screen, rect, text, font, mouse, command, colour1=(255,255,255), colour2=(178, 43, 209)):
    
    
    if not pointcheck(rect,mouse):
        
        text_colour = colour2
        pygame.draw.rect(screen, colour1, rect)
    else:
        pygame.draw.rect(screen, colour2, rect)
        text_colour = colour1
        if mouse[2] == 1:
            command()
    text = font.render(text, True, text_colour)
    
    screen.blit(text, (rect[0], rect[1]))
        

class pallet:
    def __init__(self):
        self.pallet = []
        
    def load(self, file):
        pass
    def save(self, name):
        pass

    def add(self, image, collider = None):
        'image can be either rgb or image file'
        self.pallet.append([image,collider])

    def remove(self, index):
        self.pallet.pop(index)

    def print(self):
        for index, item in enumerate(self.pallet):
            print(index, item)

    
class grid:
    #creates a resizable grid that extends past the sides of the window in order to place tiles
    def __init__(self, serface):
        self.pallet = []
        self.level = []
        self.width, self.height = 10, 10
        self.cell_width, self.cell_height = 100, 100
        
    def line(start, end, colour = (0,0,0)):
        pass
        
    def draw(self):
        for x in range(self.width):
            pygame.draw.line(self.serface, (0,0,0), (x * self.cell_width,
    def update(self):
        pass
    def add(self, tile):
        pass
    def increse_size(self, side, number):
        pass
    def insert(self, index, row_column):
        "row_column takes either 'row' or 'column'"
        pass


width, height = 1000, 800
mouse = [0,0,0]

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 35)
pallet = pallet()
grid = grid()


def update():
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, white, [width/4, height/4, width/2, height/2])
    button(screen, [0,0,100,50],"the", font,mouse,lambda: print(9))
    pygame.display.update()
    
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width, height = event.w, event.h
        elif event.type == pygame.MOUSEMOTION:
            mouse[0], mouse[1] = event.pos[0], event.pos[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse[2] = event.button
        else:
            mouse[2] = 0
            

    update()

    clock.tick(60)
