import pygame, pickle, os
import tkinter as tk
from lib.colour import *
from lib.addons import pointcheck
import lib
print(lib.__path__)

class button:
    def __init__(self):
        self.click = False
    def drop_menu(self,screen, rect, text, font, mouse, command, colour1=(0,0,0), colour2=(178, 43, 209)):
        
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


            
            
    def button(self,screen, rect, text, font, mouse, command, colour1=(0,0,0), colour2=(178, 43, 209)):
        
        
        if not pointcheck(rect,mouse):
            
            text_colour = colour2
            
        else:
            pygame.draw.rect(screen, colour2, rect)
            text_colour = colour1
            if mouse[2] == 1:
                command()
        text = font.render(text, True, text_colour)
        
        screen.blit(text, (rect[0], rect[1]+5))


        

class pallet:
    def __init__(self):
        self.pallet = [None,[(100,50,197),False],[(10,0,197),False]]
        
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
    def __init__(self, serface, x, y):
        self.serface = serface
        self.on = True
        self.pallet = [None,[(100,50,197),False]]
        self.tile = 1
        self.edit_x, self.edit_y = 3,3
        self.x, self.y = x, y
        self.width, self.height = 10, 10
        self.level = []
        for x in range(self.width):
            self.level.append([])
            for y in range(self.height):
                self.level[x].append(0)
        

        self.cell_width, self.cell_height = 100, 100
        self.file = None
        self.folder = "C:/Users/verdon/Documents/programming/python projects/pygame/2D rpg/level editor/saves/"
   
    def _selector(self):
        "using the mouse location this outputs what grid square it is over and if the mouse left clicked it"
        for x_cells in range(self.width):
            for y_cells in range(self.height):
                
                if pointcheck([self.x + (x_cells * self.cell_width),
                               self.y + (y_cells * self.cell_height),
                               self.cell_width, self.cell_height], mouse):
            
                    if mouse[2] == 1:
                        return x_cells, y_cells, True
                    
                    else:
                        return x_cells, y_cells, False

        return None
            
        
   
    def _grid_square(self, grider):
        "input a rect square and it returns the grid location\
or input a grid location and it outputs a rect square"
        if len(grider) == 2: # its a grid location
            pass
        elif len(grider) == 4: # its a rect
            pass
        else: # throw error
            print('error in grid._grid_square: it recived the wrong list size')

    def _line(self, start, end, colour = (0,0,0)):
        "a line relitive to the grid"
        pygame.draw.line(self.serface, colour,
                         (self.x + start[0], self.y + start[1]),
                         (self.x + end[0], self.y + end[1]))
    def _rect(self, colour, rect, width = 0):
        "a square relitive to the grid"
        pygame.draw.rect(screen, colour,
                         [rect[0] + self.x, rect[1] + self.y, rect[2], rect[3]],
                         width)
        
    def draw(self):
        
        for y, line in enumerate(self.level):
            for x, tile in enumerate(line):
                if tile is not 0:
                    self._rect(tile[0],[x * self.cell_width, y * self.cell_height,
                                    self.cell_width, self.cell_height])        
        
        for x in range(self.width + 1):
            self._line((x * self.cell_width, 0),
                       (x * self.cell_width, self.height * self.cell_height))
            self._line((0, x * self.cell_height),
                       (self.width * self.cell_width, x * self.cell_height))

    def edit(self, edit):
        ""
        self._rect(black,[edit[0] * self.cell_width, edit[1] * self.cell_height,
                          self.cell_width, self.cell_height],5)
        if edit[2] == True:
            self.add(edit[0],edit[1],self.pallet[self.tile])
            
        
    def update(self):
        if self.on:
            location = self._selector()
            if location is not None:
                self.edit(location)
            
        self.draw()
                         
    def add(self, x, y, tile):
        self.level[y][x] = tile
        
    def increse_size(self, side, number):
        pass
    def insert(self, index, row_column):
        "row_column takes either 'row' or 'column'"
        pass
    def level_save(self):
        if self.file == None:
            self.level_save_as()
        else:
            
            pickle.dump(self.level, open(self.folder + self.file, 'wb'))
            print('save')
    def level_save_as(self):
        def save():
            file = text.get('1.0', '30.0') 
            file = file[:-1]
            self.file = file + '.lev'
            pickle.dump(self.level, open(self.folder + self.file, 'wb'))
            root.destroy()
    
        root = tk.Tk()
        tk.Label(root,text='Save As:').pack()
        text = tk.Text(root, height = 1, width = 30)
        text.pack()
        tk.Button(root, text = 'save', command = lambda: save()).pack()
        
        root.mainloop()
        
        

    def level_load(self):
        def load():
            file = text.get('1.0', '30.0') 
            file = file[:-1]
            self.file = file + '.lev'
            self.level = pickle.load(open(self.folder + self.file, 'rb'))
            root.destroy()

        options = ''
        for file in os.listdir(self.folder):
            options = options + '\n' + file[:-4]
        
        root = tk.Tk()
        tk.Label(root,text='Options: ' + options).pack()
        text = tk.Text(root, height = 1, width = 30)
        text.pack()
        tk.Button(root, text = 'Load', command = lambda: load()).pack()
        root.mainloop()
        
        
        

    def level_new(self):
        def new():
            self.level = []
            for x in range(self.width):
                self.level.append([])
                for y in range(self.height):
                    self.level[x].append(0)
                    root.destroy()
        root = tk.Tk()
        tk.Label(root, text="Are you sure?\nAll unsaved work\nwill be lost.").pack()
        tk.Button(root, text="yes", command=lambda: new()).pack(side='left')
        tk.Button(root, text="no", command=lambda: root.destroy()).pack(side='right')
        root.mainloop()
        self.level = []
        for x in range(self.width):
            self.level.append([])
            for y in range(self.height):
                self.level[x].append(0)

    def level_projectselect(self):
        
        def load():
            folder = text.get('1.0', '30.0') 
            file = file[:-1]
            self.file = file + '.lev'
            self.level = pickle.load(open(self.folder + self.file, 'rb'))
            root.destroy()

        projects = ''
        with open('projects.txt','r') as file:
            projects = file.readlines()
            
        
        root = tk.Tk()
        tk.Label(root,text='Projects: ' + projects).pack()
        text = tk.Text(root, height = 1, width = 30)
        text.pack()
        tk.Button(root, text = 'Load', command = lambda: load()).pack()
        root.mainloop()




    
width, height = 1000, 800
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
    height = height * 0.06
    
pygame.init()
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Level Edit")
image = pygame.image.load("lib/flower_corner_image.png")
pygame.display.set_icon(image)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Courier New", 35)
pallet = pallet()
grid = grid(screen, 0, top_bar.height)

clicky = button()
mouse_oneclick = False

def file_buttons():
    grid.on = False
    pygame.draw.rect(screen,black,[0,0,150,300])
    clicky.button(screen, [0,50,150,50], 'New', font, mouse, lambda: grid.level_new())
    clicky.button(screen, [0,100,150,50], 'Load', font, mouse, lambda: grid.level_load())
    clicky.button(screen, [0,150,150,50], 'Save', font, mouse, lambda: grid.level_save())
    clicky.button(screen, [0,200,150,50], 'SaveAs', font, mouse, lambda: grid.level_save_as())
    clicky.button(screen, [0,250,150,50], 'project', font, mouse, lambda: grid.level_projectselect())


def key():
    speed = 5
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
            grid.on == False
        if grid.on == False:
            grid.on == True
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
    grid.update()
    pygame.draw.rect(screen, black, [0, 0, width, top_bar.height])
    grid.on = True
    clicky.drop_menu(screen, [0,0,150,top_bar.height], 'file', font, mouse, lambda: file_buttons())
    
    
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
    
    
    clock.tick(60)
