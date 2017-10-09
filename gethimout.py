import random
import pygame as pg
from pygame.locals import *

def create_level():
	level=[]
	with open("level1.txt") as f:
		for line in f:
			lines=[]
			for cell in line:
				if cell != '\n':
					lines.append(cell)
			level.append(lines)
	#print("Here is the labyrinth as a list:",level)
	#print("Here is the 4rth row:",level[3])
	return level

def display_level(window,level):
        background = pg.image.load("background.jpg").convert()
        background = pg.Surface(window.get_size())
        window.blit(background,(0,0))
        
        wall = pg.image.load("wall.png").convert()
        start = pg.image.load("start.png").convert_alpha()
        guardian = pg.image.load("guardian.png").convert_alpha()
        macgyver = pg.image.load("macgyver.png").convert_alpha()

        #Redimensioning of the images, to adapt to the window size        
        wall = pg.transform.scale(wall,(int(650/15),int(480/15)))
        start = pg.transform.scale(start,(int(650/15),int(480/15)))
        guardian = pg.transform.scale(guardian,(int(650/15),int(480/15)))
        macgyver = pg.transform.scale(macgyver,(int(650/15),int(480/15)))
        
        #Static positioning of the labyrinth and the characters
        num_line = 0
        empty_cells = [] #List of empty cells
        position_guardian = []
        for line in level :
                num_col=0
                y=num_line*int(480/15)
                for cell in line :
                        x = num_col*int(640/15)
                        if cell=="w":
                                window.blit(wall,(x,y))  
                        if cell=="d":
                                window.blit(start,(x,y))
                                position_macgyver = macgyver.get_rect()
                                position_macgyver.center = (x+int((640/30)),y+int((480/30)))
                        if cell=="f":
                                window.blit(guardian,(x,y))
                                position_guardian = [x,y]
                        if cell=="n":
                                pass
                        elif cell=="0":
                                empty_cells.append([x,y])                                
                        num_col += 1
                num_line += 1

        pg.display.flip()
        elements = [macgyver,position_macgyver, empty_cells, position_guardian]
        return elements
        
current_level = create_level()

current_window = pg.display.set_mode((640,480), RESIZABLE)



#display_level(current_level)

class Character():
        def __init__(self, window, elements_level):
                self.elements_level = elements_level
                #self.position = position
                self.window = window
                self.window.blit(self.elements_level[0],self.elements_level[1].topleft)
                pg.display.flip()

                self.position1 = random.randint(0,len(self.elements_level[2]))
                self.position2 = random.randint(0,len(self.elements_level[2]))
                self.position3 = random.randint(0,len(self.elements_level[2]))

                #self.list_coor=list(self.elements_level[1].topleft) # -> répétition, à transformer
               
                self.got_needle = 0
                self.got_ether = 0
                self.got_tube = 0

                self.state = "alive"
                               
        def move_char(self, direction):

                list_coor=list(self.elements_level[1].topleft)
                x = list_coor[0]
                y = list_coor[1]
                                
                if direction == "up" and ([x,y-int(480/15)] in self.elements_level[2] or [x,y-int(480/15)] == self.elements_level[3] ) :
                        #position = position.move(0,int(480/15))
                        self.elements_level[1] = self.elements_level[1].move(0,-int(480/15))
                        print(self.elements_level[1])
                elif direction == "down" and ([x,y+int(480/15)] in self.elements_level[2] or [x,y+int(480/15)] == self.elements_level[3] ) :
                        #position = position.move(0,-int(480/15))
                        self.elements_level[1] = self.elements_level[1].move(0,int(480/15))
                        #print(position)                        
                        print(self.elements_level[1])
                elif direction == "left" and ([x-int(640/15),y] in self.elements_level[2] or [x-int(640/15),y] == self.elements_level[3] ) :
                        #position = position.move(-int(640/15),0)
                        self.elements_level[1] = self.elements_level[1].move(-int(640/15),0)
                        #print(position) 
                        print(self.elements_level[1])
                elif direction == "right" and (([x+int(640/15),y] in self.elements_level[2]) or ([x+int(640/15),y] == self.elements_level[3]) ) :
                        #position = position.move(int(640/15),0)
                        self.elements_level[1] = self.elements_level[1].move(int(640/15),0)
                        #print(position) 
                        print(self.elements_level[1])
                #self.window.blit(self.elements_level[0],self.elements_level[1])

        def display_moves(self,macgyver, needle, ether, tube, init):
                list_coor=list(self.elements_level[1].topleft)
                
                if list_coor != self.elements_level[2][self.position1] and self.got_needle==0 :
                        self.window.blit(needle,self.elements_level[2][self.position1])
                else:
                        self.got_needle = 1
                        
                if list_coor != self.elements_level[2][self.position2] and self.got_ether==0:
                        self.window.blit(ether,self.elements_level[2][self.position2])
                else:
                        self.got_ether = 1
                        
                if list_coor != self.elements_level[2][self.position3] and self.got_tube==0:
                        self.window.blit(tube,self.elements_level[2][self.position3])
                else:
                        self.got_tube = 1

                if list_coor == self.elements_level[3]:
                        
                        if self.got_needle == 1 and self.got_ether==1 and self.got_tube==1:
                                #print("Hourrrrrra !")
                                self.state="won"
                        else:
                                #print("You looooooose!")
                                self.state="dead"
                #print(self.state)                      
                self.window.blit(macgyver,list_coor)

                #print("position de macgyver",list_coor)
                #print("position du guardien",self.elements_level[3])
                #print(self.got_needle,self.got_ether,self.got_tube)
                pg.display.flip()
                

MacGyver = Character(current_window, display_level(current_window, current_level))

macgyver = pg.image.load("macgyver.png").convert_alpha()
needle = pg.image.load("needle.png").convert_alpha()
ether = pg.image.load("ether.png").convert_alpha()
tube = pg.image.load("tube.png").convert_alpha()
youwin = pg.image.load("youwin.png").convert_alpha()
youlose = pg.image.load("youlose.jpg").convert_alpha()

macgyver = pg.transform.scale(macgyver,(int(650/15),int(480/15)))
needle = pg.transform.scale(needle,(int(650/15),int(480/15)))
ether = pg.transform.scale(ether,(int(650/15),int(480/15)))
tube = pg.transform.scale(tube,(int(650/15),int(480/15)))
youwin = pg.transform.scale(youwin,(640,480))
youlose = pg.transform.scale(youlose,(640,480))


#Here is the game loop :
        
keep_open = 1
MacGyver.display_moves(macgyver, needle, ether, tube,1)

while keep_open :
        for event in pg.event.get(): 
                if event.type == QUIT :
                        keep_open = 0
                if MacGyver.state=="alive" :        
                        if event.type == KEYDOWN:                        
                                if event.key == K_UP:
                                        MacGyver.move_char("up")
                                if event.key == K_DOWN:
                                        MacGyver.move_char("down")
                                if event.key == K_LEFT:
                                        MacGyver.move_char("left")
                                if event.key == K_RIGHT:
                                        MacGyver.move_char("right")
                                        
                                display_level(current_window, current_level)
                                MacGyver.display_moves(macgyver, needle, ether, tube, 0)
                elif MacGyver.state=="dead":
                        current_window.blit(youlose,(0,0))
                        pg.display.flip()
                elif MacGyver.state=="won":
                        current_window.blit(youwin,(0,0))
                        pg.display.flip()
