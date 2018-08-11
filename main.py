import pygame
from lib.addons import collide, pointcheck, timer
from lib.sprite import sprite
from lib.enemy import enemy
from lib.colour import *
#print(help(pygame.draw.circle))
width = 1000
height = 800
time = 0
end = False

# pygame setup
pygame.init()
display = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("dave")
icon = pygame.image.load('images/flower_corner_image.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.MILLI = 18
milasecond_timer = pygame.time.set_timer(pygame.MILLI, 1)

#print(help(pygame.time.set_timer))
class timer:
    def __init__(self):
        self.old_time = 0

    def timer(self, interval, time, command):
        
        if time - self.old_time >= interval:
            command()
            self.old_time = time
            
    
class background(collide):
    def __init__(self,screen, walls=None):
        self.walllist=walls
        self.screen = screen
        self.lives = 40
        self.font = pygame.font.SysFont("Courier New", 35)


    def life(self):
        pygame.draw.rect(self.screen, white, [10,10,60,40])
        text = self.font.render(str(self.lives), True, red)

        self.screen.blit(text, (10, 10))


    def draw(self):
        
        pygame.draw.rect(display, white,[100, 100,100,100])





# initiallizing all the objects. The order is really important for feeding the collide.walllist list through everything

dave = sprite(display, 3, 0.1, 6, width / 2, height / 2)
back = background(display)
pr = timer()
killer = enemy(display, 100, 100)


danger = []

def circle():
    center = (250,250)
    #r = x + y
    pygame.draw.line(display, red, center, (100,200))

def update():
    

    # drawing things
    display.fill(black)
    back.life()
    dave.update()
    killer.update(dave.sword_point, dave.sword_center)
    #pr.timer(100, time, lambda: print(9))
    print(killer.danger)
    pygame.display.update()
    


while not end:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MILLI:
            time += 1
            #print(time)
            
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            display = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dave._a = True
            if event.key == pygame.K_s:
                dave._s = True
            if event.key == pygame.K_d:
                dave._d = True
            if event.key == pygame.K_w:
                dave._w = True

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                dave._a = False
            if event.key == pygame.K_s:
                dave._s = False
            if event.key == pygame.K_d:
                dave._d = False
            if event.key == pygame.K_w:
                dave._w = False



    update()


    

    #print(clock.get_fps())

    clock.tick(60)
