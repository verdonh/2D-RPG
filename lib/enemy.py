import pygame
from lib.addons import pointcheck, circle_pointcheck



class enemy:
    def __init__(self, screen, x, y):
        self.alive = True
        self.screen = screen
        self.hit = False
        self.x, self.y = x, y
        self.radious = 30
        self.danger = ['circle', [self.x, self.y], self.radious]

    def update(self, point1, point2):
        if not self.hit:
            pygame.draw.circle(self.screen, (150,200,50), [self.x, self.y], self.radious)
        if circle_pointcheck([self.x, self.y], self.radious, point1) or circle_pointcheck([self.x, self.y], self.radious, point2):
            self.hit = True

        self.danger = ['circle', [self.x, self.y], self.radious]


