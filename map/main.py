import pygame
import pickle
import lib.input as inp
from lib.colour import *

width = 800
height = 500

end = False

class level:
    def __init__(self, display, map_file, x, y, cell_width, cell_height):
        self.display = display

        self.level = self.open_level(map_file)
        self.x, self.y = x, y
        self.cell_width, self.cell_height =cell_width, cell_height
        self.speed = 3

        self.w = False
        self.s = False
        self.d = False
        self.a = False


    def open_level(self, file):
        return pickle.load(open(file,'rb'))

    def _rect(self, colour, rect):
        pygame.draw.rect(self.display, colour, rect)

    def new_level(self, map_file, x, y):
        self.level = openlevel(map_file)
        self.x, self.y = x, y

    def update(self):
        for y in range(len(self.level)):
            for x in range(len(self.level)):
                self._rect(self.level[y][x][0],
                           [self.x + (x * self.cell_height),
                            self.y + (y * self.cell_width),
                            self.cell_width, self.cell_height])

        self.keys()

    def keys(self):
        if self.w:
            self.y += self.speed
        if self.s:
            self.y -= self.speed
        if self.d:
            self.x -= self.speed
        if self.a:
            self.x += self.speed
        

    def test(self):
        pass
        

class character:
    def __init__(self, display, start_pos, scale, file):
        
        
        self.x, self.y = start_pos[0], start_pos[1]
        
 
        self.display = display
        self.scale = scale * 16

        self.file = file

        self.image_lis = []

        for name in ['back1.png', 'back2.png','frount-left1.png',
                     'frount-left2.png','frount-right1.png', 'frount-right2.png']:
            
            image = pygame.image.load('images/' + self.file + '/' + name)
            image = pygame.transform.scale(image, (self.scale ,self.scale))
            self.image_lis.append(image)

        self.image = self.image_lis[4]

        self.block = int(self.scale / 16)

        self.width, self.height = self.block * 6, self.block * 13

        self.xhold, self.yhold = 0, 0
        self.rect = []
        self._real_pos_calc(self.x, self.y)

        self.w = False
        self.s = False
        self.d = False
        self.a = False


        

    def draw(self, image, x, y):
        self._real_pos_calc(x, y)
        self.display.blit(image, (self.xhold, self.yhold))

    def _real_pos_calc(self, x, y):
        self.xhold, self.yhold = x - self.block * 8, y - self.block * 8
        self.rect = [x - self.block * 3, y - self.block * 6, self.width, self.height]
        
    def _show_bounds(self):
      
        pygame.draw.rect(self.display, (100,1,10), self.rect)
        
    def update(self):
        self.keys()
        self.draw(self.image, self.x, self.y)
        

    def keys(self):
        if self.w:
            self.image = self.image_lis[0]

        if self.s:
            self.image = self.image_lis[4]

        if self.d:
            self.image = self.image_lis[4]

        if self.a:
            self.image = self.image_lis[3]

        
        

    
# pygame setup
pygame.init()
display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Test")
icon = pygame.image.load('images/flower_corner_image.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
scary = character(display,(width * 0.5, height * 0.5), 10, 'scary dude')
dungon = level(display, 'maps/test.lev', 0, 0, 100, 100)


def background():
    pygame.draw.rect(display, (0,200,10),scary.rect)


def keys():
    pass


def update(events):
    display.fill(white)
    
    dungon.update()
    #background()

    scary.update()
    
    

    
    pygame.display.update()


while not end:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dungon.w = True
                scary.w = True
            if event.key == pygame.K_s:
                dungon.s = True
                scary.s = True
            if event.key == pygame.K_d:
                dungon.d = True
                scary.d = True
            if event.key == pygame.K_a:
                dungon.a = True
                scary.a = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                dungon.w = False
                scary.w = False
            if event.key == pygame.K_s:
                dungon.s = False
                scary.s = False
            if event.key == pygame.K_d:
                dungon.d = False
                scary.d = False
            if event.key == pygame.K_a:
                dungon.a = False
                scary.a = False

    keys()
    update(events)
    
    clock.tick(30)








    
