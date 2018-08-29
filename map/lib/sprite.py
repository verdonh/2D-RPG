import pygame
from lib.colour import *

class sprite:
    def __init__(self, display, push, friction, max_velocity, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.push = push
        self.friction = friction
        self.max_v = max_velocity
        self._a = False
        self._s = False
        self._w = False
        self._d = False
        self._space = False


        self.radious = 40

        self.direction = 'n'
        self.sword_colour = red
        self.sword_length = 150
        self.sword_point = [0,0]
        self.sword_center = [0, 0]
        self.sword_width = 10


    def draw(self):
        pygame.draw.circle(self.display, white, [int(self.x), int(self.y)], self.radious)

    def change_values(self):
        global new_x, new_y

        self.vx += self.ax
        new_x = self.x + self.vx

        self.vy += self.ay
        new_y = self.y + self.vy

        if self.vx > self.max_v:
            self.vx = self.max_v
        if self.vy > self.max_v:
            self.vy = self.max_v
        if self.vx < -self.max_v:
            self.vx = -self.max_v
        if self.vy < -self.max_v:
            self.vy = -self.max_v

        
        if self.vx < self.friction and self.vx > -self.friction and \
           (not self._a) and (not self._d):
            self.vx = 0
            
        if self.vx < 0:
            self.vx += self.friction
        elif self.vx > 0:
            self.vx -= self.friction

        if self.vy < self.friction and self.vy > -self.friction and \
           (not self._w) and (not self._s):
            self.vy = 0
        if self.vy < 0:
            self.vy += self.friction
        elif self.vy > 0:
            self.vy -= self.friction


        
        return new_x, new_y

    def _sword_calc(self):
        point =0
        if self.direction == 'nw':
            point = (((self.sword_length ** 2) / 2) ** 0.5)
            self.sword_point = [point + self.x, point + self.y]

        elif self.direction == 'se':
            point = (((self.sword_length ** 2) / 2) ** 0.5)
            self.sword_point = [-point + self.x, -point + self.y]

        elif self.direction == 'ne':
            point = (((self.sword_length ** 2) / 2) ** 0.5)
            self.sword_point = [-point + self.x, point + self.y]

        elif self.direction == 'sw':
            point = (((self.sword_length ** 2) / 2) ** 0.5)
            self.sword_point = [point + self.x, -point + self.y]

        elif self.direction == 'n':
            point = self.sword_length
            self.sword_point = [self.x, point + self.y]

        elif self.direction == 's':
            point = self.sword_length
            self.sword_point = [self.x, -point + self.y]

        elif self.direction == 'w':
            point = self.sword_length
            self.sword_point = [point + self.x, self.y]

        elif self.direction == 'e':
            point = self.sword_length
            self.sword_point = [-point + self.x, self.y]

        self.sword_point = [int(self.sword_point[0]), int(self.sword_point[1])]

        self.sword_center = self.sword_point 
        print(self.sword_point)


    def draw_sword(self):
        self._sword_calc()
        pygame.draw.line(self.display, self.sword_colour, (self.x, self.y), self.sword_point, self.sword_width)
        pygame.draw.circle(self.display, self.sword_colour, self.sword_point, int(self.sword_width/3))

    def sword_directionswap(self):

        direction_list = ['n','nw','w','sw','s','se','e','ne']
        for item, direction in enumerate(direction_list):
            if self.direction == direction:
                print('t',item)
                if item <= 3:
                    self.direction = direction[item + 3]
                else:
                    self.direction = direction[item - 4]
    def _attack(self):
        self.sword_directionswap()



    def sword(self):
        self.draw_sword()


    def update(self):
        
        # these reset acceleration to 0 when a button is not pressed
        if not (self._a and self._d):
            self.ax = 0

        if not (self._w and self._s):
            self.ay = 0

        # change acceleration when somthing is pressed
        if self._a:
            self.ax = -self.push
            self.direction = 'w'
            
        if self._d:
            self.ax = self.push
            self.direction = 'e'
            
        if self._w:
            self.ay = -self.push
            self.direction = 'n'

        if self._s:
            self.ay = self.push
            self.direction = 's'

        if self._a and self._w:
            self.direction = 'nw'

        if self._w and self._d:
            self.direction = 'ne'

        if self._s and self._d:
            self.direction = 'se'

        if self._s and self._a:
            self.direction = 'sw'

        if self._space:
            self._attack()




            #print(self.vx, self.vy)
        self.x, self.y = self.change_values()

        self.sword()
        self.draw()


#class sword(sprite):
 #   def __init__(self, display, push, friction, max_velocity, x, y):
  #      super.__init__(display, push, friction, max_velocity, x, y)






