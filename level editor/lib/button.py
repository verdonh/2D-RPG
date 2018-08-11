import pygame
from lib.colour import *
from lib.addons import pointcheck
gray1 = (150,150,150)
class button:
    def __init__(self):
        self.click = False
        self.reset = False
    def drop_menu(self,screen, rect, text, font, mouse, command, colour1=(0,0,0), colour2=gray1):
        
        if not pointcheck(rect,mouse):
            
            text_colour = colour2
            
        else:
            pygame.draw.rect(screen, colour2, rect)
            text_colour = colour1
            if mouse[2] == 1:
                mouse[2] == 0
                if self.click == True:
                    self.click = False
                else:
                    self.click = True
        
        if self.click == True:
            command()
            
        text = font.render(text, True, text_colour)
        
        screen.blit(text, (rect[0], rect[1]+5))


            
            
    def button(self,screen, rect, text, font, mouse, command, colour1=(0,0,0), colour2=gray1):
        
        
        if not pointcheck(rect,mouse):
            
            text_colour = colour2
            
        else:
            pygame.draw.rect(screen, colour2, rect)
            text_colour = colour1
            if mouse[2] == 1:
                command()
        text = font.render(text, True, text_colour)
        
        screen.blit(text, (rect[0], rect[1]+5))

    def one_click(self, screen, rect, text, font, mouse, command, colour1=(0, 0, 0), colour2=gray1):
        pygame.draw.rect(screen,colour1,rect)
        if not pointcheck(rect, mouse):

            text_colour = colour2

        else:
            pygame.draw.rect(screen, colour2, rect)
            text_colour = colour1
            if mouse[2] == 1 and self.reset:

                if self.click == True:
                    self.click = False
                else:
                    self.click = True
                    self.reset = False

        if mouse[2] == 0:
            self.reset = True

        if self.click == True:
            command()
        self.click = False
        text = font.render(text, True, text_colour)

        screen.blit(text, (rect[0], rect[1] + 5))




        
