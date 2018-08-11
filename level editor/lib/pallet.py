import pygame
from lib import button
from lib.colour import *


class pallet(button):
    def __init__(self, screen, width, height):

        button.__init__(self)
        self.screen = screen
        self.pallet = [[(255, 255, 255),False],[(255, 0, 0),False],[(0, 255, 0),False], [(0, 0, 255),False]]
        self.pointer = 1 #points to the pallet colour that you want to work with
        self.width, self.height = width, height
        self.font = pygame.font.SysFont("Courier New", 18)

        self.x = self.width * 0.75
        self.y = self.height * 0.6

        self.pallet_width = self.width - self.x
        self.pallet_height = self.height - self.y

        self.resize(width, height)

    def load(self, file):
        pass
    def save(self, name):
        pass

    def forwards(self):
        if self.pointer < (len(self.pallet) - 1):
            self.pointer += 1
        else:
            self.pointer = 0

    def back(self):
        if self.pointer > 0:
            self.pointer -= 1
        else:
            self.pointer = len(self.pallet) - 1


    def add(self, image, collider = None):
        'image can be either rgb or image file'
        self.pallet.append([image,collider])

    def remove(self, index):
        self.pallet.pop(index)


    def print(self):
        for index, item in enumerate(self.pallet):
            print(index, item)

    def draw_curent(self):
        pygame.draw.rect(self.screen, self.pallet[self.pointer][0], [self.x + self.pallet_width * 0.2, self.y + 33, self.pallet_width * 0.6, self.pallet_height * 0.5])

    def update(self, mouse):
        pygame.draw.rect(self.screen, white, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(self.screen, black, [self.x, self.y, self.width, self.height], 5)

        # scrole back
        self.one_click(self.screen, [self.x + 3, self.y + 3, self.pallet_width * 0.5, 30],
                       'back', self.font, mouse, lambda: self.back())
        # scrole forwards
        self.one_click(self.screen, [self.x + 3 + (self.pallet_width * 0.5), self.y + 3, self.pallet_width * 0.5, 30],
                       'next', self.font, mouse, lambda: self.forwards())

        self.draw_curent()





    def resize(self, width, height):
        self.width, self.height = width, height
        self.x = self.width * 0.75
        self.y = self.height * 0.6

        self.pallet_width = self.width - self.x
        self.pallet_height = self.height - self.y