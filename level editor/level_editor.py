import pygame
from lib import button, grid, pallet
from lib.addons import pointcheck
from lib.colour import *


    
width, height = 800, 500
mouse = [0,0,0]
class keydown:
    w = False
    s = False
    a = False
    d = False
    q = False
    e = False
    c = False
    up = False
    down = False
    right = False
    left = False
    z = False
    x = False
    c = False

class top_bar:
    height = 800 * 0.06
    
pygame.init()
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Level Edit")
image = pygame.image.load("lib/flower_corner_image.png")
pygame.display.set_icon(image)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Courier New", 35)
pallet = pallet(screen, width, height)
grid = grid(screen, 0, top_bar.height)

file_clicker = button()
edit_clicker = button()
clicky = button()
mouse_oneclick = False

def grid_on(rect):
    if pointcheck(rect, mouse):
        grid.on = False


def file_buttons():

    grid.on = False
    pygame.draw.rect(screen,black,[0,48,150,250])
    clicky.button(screen, [0,50,150,50], 'New', font, mouse, lambda: grid.level_new())
    clicky.button(screen, [0,100,150,50], 'Load', font, mouse, lambda: grid.level_load())
    clicky.button(screen, [0,150,150,50], 'Save', font, mouse, lambda: grid.level_save())
    clicky.button(screen, [0,200,150,50], 'SaveAs', font, mouse, lambda: grid.level_save_as())
    clicky.button(screen, [0,250,150,50], 'project', font, mouse, lambda: grid.level_projectselect())

def edit_buttons():

    grid.on = False
    pygame.draw.rect(screen, black, [150, 48, 150, 100])
    clicky.button(screen, [150, 50, 150, 50], 'column', font, mouse, lambda: print('hold'))
    clicky.button(screen, [150, 100, 150, 50], 'row', font, mouse, lambda: print('hold'))


def key():
    speed = 8
    if keydown.w == True:
        grid.y += speed
    if keydown.s == True:
        grid.y -= speed
    if keydown.a == True:
        grid.x += speed
    if keydown.d == True:
        grid.x -= speed
    if keydown.q:
        grid.cell_height += 5
        grid.cell_width += 5
    if keydown.e:
        buffer = grid.cell_height
        
        buffer -= 5
        if buffer > -5:
            grid.cell_height = buffer
            grid.cell_width = buffer
    if keydown.c:
        if grid.on == True:
            grid.on = False
        if grid.on == False:
            grid.on = True
    if keydown.up == True:
        try:
            grid.edit_y -= 1
        except:
            print("too far")
    if keydown.down == True:
        try:
            grid.edit_y += 1
        except:
            print("too far")
    
def update():
    
    screen.fill(white)
    grid.update(mouse, pallet.pallet[pallet.pointer])

    pallet.update(mouse)
    pygame.draw.rect(screen, black, [0, 0, width, top_bar.height])
    grid.on = True
    grid_on([pallet.x, pallet.y, pallet.pallet_width, pallet.pallet_height])
    file_clicker.drop_menu(screen, [0,0,150,top_bar.height], 'file', font, mouse, lambda: file_buttons())
    edit_clicker.drop_menu(screen, [150, 0, 150, top_bar.height], 'insert', font, mouse, lambda: edit_buttons())
    
    
    pygame.display.update()
    
    
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width, height = event.w, event.h
            pallet.resize(width, height)
            
            
        elif event.type == pygame.MOUSEMOTION:
            mouse[0], mouse[1] = event.pos[0], event.pos[1]
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse[2] = event.button

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button != 0:
                mouse[2] = 0

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                keydown.w = True
            if event.key == pygame.K_s:
                keydown.s = True
            if event.key == pygame.K_a:
                keydown.a = True
            if event.key == pygame.K_d:
                keydown.d = True
            if event.key == pygame.K_q:
                keydown.q = True
            if event.key == pygame.K_e:
                keydown.e = True
            if event.key == pygame.K_c:
                keydown.c = True
            if event.key == pygame.K_8:
                keydown.up = True
            if event.key == pygame.K_2:
                keydown.down = True
            if event.key == pygame.K_4:
                keydown.right = True
            if event.key == pygame.K_6:
                keydown.left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keydown.w = False 
            if event.key == pygame.K_s:
                keydown.s = False
            if event.key == pygame.K_a:
                keydown.a = False
            if event.key == pygame.K_d:
                keydown.d = False
            if event.key == pygame.K_q:
                keydown.q = False
            if event.key == pygame.K_e:
                keydown.e = False
            
        else:
            pass
            
    
    key()
    update()
    
    # reset one time use keys
    # mouse one time perameters
    if mouse[1] <= top_bar.height:
        mouse[2] = 0
    keydown.up = False
    keydown.down = False
    keydown.right = False
    keydown.left = False
    keydown.c = False
    
    
    clock.tick(30)
