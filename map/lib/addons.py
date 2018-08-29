import pygame


def pointcheck(rect, point):
        'checks if the point is in the rect'
        if (rect[0] < point[0] and rect[0] + rect[2] > point[0] and
                rect[1] < point[1] and rect[1] + rect[3] > point[1]):
            return True
        return False

def circle_pointcheck(circle_point, radious, point):
    x = circle_point[0] - point[0]
    y = circle_point[1] - point[1]

    dis = (x ** 2 + y ** 2) ** 0.5
    if dis < radious:
        return True




        
def rect_collide(self, rect1, rect2):
        'checks if rect two rects overlap.'

        if (self._pointcheck(rect1, (rect2[0], rect2[1])) or
            self.pointcheck(rect1, (rect2[0] + rect2[2], rect2[1] + rect2[3])) or
            self.pointcheck(rect1, (rect2[0] + rect2[2], rect2[1])) or
            self.pointcheck(rect1, (rect2[0], rect2[1] + rect2[3]))):

                return True
        else:
                return False
class collide:
    def __init__(self):
        self.walllist = []
        self.collide = False

    def add(self, rect):
        self.walllist.append(rect)

    def check_all(self):
        'checks all the rects in self.collide against each other.'
        pass

    def check_against(self, rect):
        'checks all the rects in self.collide against inputed rect.'
        for item in self.walllist:
            if (self._pointcheck(item, (rect[0], rect[1])) or
                    self.pointcheck(item, (rect[0] + rect[2], rect[1] + rect[3])) or
                    self.pointcheck(item, (rect[0] + rect[2], rect[1])) or
                    self.pointcheck(item, (rect[0], rect[1] + rect[3]))):

                self.collide = True
                return True
            else:
                self.collide = False
                return False


class timer:
    def __init__(self):
        self.old_time = 0

    def timer(self, interval, time, command):
        
        if time - self.old_time >= interval:
            command()
            self.old_time = time

class Sprite(collide):
    """requiors the use of w, s, d, a on the keyboard"""

    def __init__(self, display, colour, x, y, walls=None):
        collide.__init__(self)
        self.display = display
        self.colour = colour
        self.x = x
        self.y = y
        self.walllist=walls
        self.dx = 5
        self.dy = 5
        self.width = 50
        self.height = 50

    def draw(self, keydict):
        
        pygame.draw.rect(self.display, self.colour,
                         [self.x, self.y, self.width, self.height])

        self.update(keydict)

    def update(self, keydict):

        x_buffer = self.x
        y_buffer = self.y

        if keydict['w'] == True:
            y_buffer -= self.dy

        if keydict['s'] == True:
            y_buffer += self.dy
        if keydict['a'] == True:
            x_buffer -= self.dx
        if keydict['d'] == True:
            x_buffer += self.dx


        x_walls = collide.check_against(self, [self.x, y_buffer, self.width, self.height])
        y_walls = collide.check_against(self, [x_buffer, self.y, self.width, self.height])

        if not x_walls:
            self.y = y_buffer
            
        if not y_walls:
            self.x = x_buffer
            




















