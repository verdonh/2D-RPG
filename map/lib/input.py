import pygame


class key:
    """use the if self.keydict['key'] == True: to test if a key is down"""

    allkeys = [['p', 112, 'long'],['r_arr', 276, 'long'],
               ['l_arr', 275, 'long'],['u_arr',273, 'long'],
               ['d_arr',274, 'long'],['q',113,'long'],
               ['w',119,'long'],['s',115,'long'],
               ['a',97,'long'],['d',100,'long']]

    def __init__(self, keys=allkeys):
        # w=119,s=115,a=97,d=100,p=112,r_arr=276,
        # l_arr=275, u_arr=273, d_arr=274, q=113
        self.onepress = {}
        self.keys = keys
        self.keylis = ['a', 's', 'w', 'd', 'p', 'r_arr',
                       'l_arr', 'u_arr', 'd_arr']
        self.keydict = {}
        for index in self.keylis:
            self.keydict[index] = False
            self.onepress[index] = False

    def long_keycheck(self, keystates, key):
        '''checks to see what keys have been pressed and updates the keydict'''
        if keystates[key[1]] == 1:
            self.keydict[key[0]] = True
        else:
            self.keydict[key[0]] = False

        

    def one_keycheck(self, keystates, key):
        '''checks to see what keys have been pressed and updates the keydict'''
        if keystates[key[1]] == 1:
            self.keydict[key[0]] = False
            if self.onepress[key[0]] == False:
                self.onepress[key[0]] = True
                self.keydict[key[0]] = True
                
        elif self.onepress[key[0]] == True:
            self.onepress[key[0]] = False
            
    def check(self):
        '''run this each time key states are to be updated'''
        keystates = pygame.key.get_pressed()
        for key in self.keys:
            if key[2] == 'one':
                self.one_keycheck(keystates, key)
            elif key[2] == 'long':
                self.long_keycheck(keystates, key)
            
        

    def keytest(self):
        '''find the key that is pressed and print its number'''
        key = pygame.key.get_pressed()
        
        for index, state in enumerate(key):
            if state != 0:
                print(index)

    def commands(self, state):
        global block_x
        global block_y
        if self.keydict['q'] == True:
            pygame.quit()
        if self.keydict['p'] == True:
            # pause the game
            pass
        if self.keydict['l_arr'] == True:
            if block_x < 10:
                block_x += 1
        if self.keydict['r_arr'] == True:
            if block_x > 0:
                block_x -= 1
            
        if self.keydict['d_arr'] == True:
            
            block_y += 1
        if self.keydict['u_arr'] == True:
            if state < 3:
                state+=1
            else:
                state = 0

        return state
    
    
if __name__ == "__main__":
    
    pygame.init()
    pygame.display.set_mode((100,100))
    key=key()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        key.keytest()
