import pygame, os, pickle
import tkinter as tk
from lib.addons import pointcheck
from lib.colour import *


class grid:
    #creates a resizable grid that extends past the sides of the window in order to place tiles
    def __init__(self, serface, x, y):
        self.serface = serface
        self.on = True

        self.tile = [(255,0,0),False]
        self.edit_x, self.edit_y = 3,3
        self.x, self.y = x, y
        self.width, self.height = 10, 10
        self.draw_grid = True
        self.level = []
        for x in range(self.height):
            self.level.append([])
            for y in range(self.width):
                self.level[x].append(0)
        

        self.cell_width, self.cell_height = 100, 100
        self.file = None
        self.folder = "C:/Users/verdon/Documents/programming/python projects/pygame/2D rpg/level editor/saves/"
   
    def _selector(self, mouse):
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
        pygame.draw.rect(self.serface, colour,
                         [rect[0] + self.x, rect[1] + self.y, rect[2], rect[3]],
                         width)
        
    def draw(self):
        
        for y, line in enumerate(self.level):
            for x, tile in enumerate(line):
                if tile is not 0:
                    self._rect(tile[0],[x * self.cell_width, y * self.cell_height,
                                    self.cell_width, self.cell_height])        
        if self.draw_grid:
            for x in range(self.height + 1):
                self._line((0, x * self.cell_height),
                           (self.width * self.cell_width, x * self.cell_height))
            for y in range(self.width + 1):
                self._line((y * self.cell_width, 0),
                           (y * self.cell_width, self.height * self.cell_height))


    def edit(self, edit):
        self._rect(black,[edit[0] * self.cell_width, edit[1] * self.cell_height,
                          self.cell_width, self.cell_height], 5)
        if edit[2]:
            self.add(edit[0], edit[1], self.tile)

    def update(self, mouse, tile):
        self.tile = tile
        self.draw()
        if self.on:
            location = self._selector(mouse)
            if location is not None:
                self.edit(location)

    def add(self, x, y, tile):
        self.level[y][x] = tile
        
    def increse_size(self, side, number):
        if side == 'n':
            pass
        if side == 's':
            self.height += number
            self.level.append([])
            for i in range(len(self.level[0])):
                self.level[len(self.level) - 1].append(0)



        if side == 'e':
            self.width += number
            for i in range(len(self.level)):
                self.level[i].append(0)

        if side == 'w':
            pass

    def grid_view(self):
        if self.draw_grid:
            self.draw_grid = False
        else:
            self.draw_grid = True




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
