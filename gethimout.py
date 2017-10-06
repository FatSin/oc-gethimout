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
	#print("Voici le labyrinthe sous forme de liste:",level)
	#print("Voici la 4e ligne:",level[3])
	return level

def display_level(window,level):
        #window = pg.display.set_mode((640,480), RESIZABLE)
        
        
        wall = pg.image.load("wall.png").convert()
        macgyver = pg.image.load("macgyver.png").convert_alpha()
        guardian = pg.image.load("guardian.png").convert_alpha()
        needle = pg.image.load("needle.png").convert_alpha()
        ether = pg.image.load("ether.png").convert_alpha()
        tube = pg.image.load("tube.png").convert_alpha()
        #Redimensioning of the images, to adapt to the window size
        wall = pg.transform.scale(wall,(int(650/15),int(480/15)))
        macgyver = pg.transform.scale(macgyver,(int(650/15),int(480/15)))
        guardian = pg.transform.scale(guardian,(int(650/15),int(480/15)))
        needle = pg.transform.scale(needle,(int(650/15),int(480/15)))
        ether = pg.transform.scale(ether,(int(650/15),int(480/15)))
        tube = pg.transform.scale(tube,(int(650/15),int(480/15)))
        #Static positioning of the labyrinth and the characters
        num_line = 0
        empty_cells = [] #List of empty cells
        for line in level :
                num_col=0
                y=num_line*480/15
                for cell in line :
                        x = num_col*640/15
                        if cell=="w":
                                window.blit(wall,(x,y))  
                        if cell=="d":
                                window.blit(macgyver,(x,y))
                                position_macgyver = macgyver.get_rect()
                                position_macgyver.center = (x,y)
                        if cell=="f":
                                window.blit(guardian,(x,y))
                        elif cell=="0":
                                empty_cells.append([x,y])                                
                        num_col += 1
                num_line += 1
        #position_macgyver = macgyver.get_rect() -> macgyver not centered here
        #Random positioning of the obects
        position1 = random.randint(0,len(empty_cells))
        position2 = random.randint(0,len(empty_cells))
        position3 = random.randint(0,len(empty_cells))
        #print(position1,position2,position3)
        #print(empty_cells)
        #print(len(empty_cells))
        window.blit(needle,empty_cells[position1])
        window.blit(ether,empty_cells[position2])
        window.blit(tube,empty_cells[position3])
        pg.display.flip()
        elements = [macgyver,position_macgyver]
        return elements
        
current_level = create_level()

current_window = pg.display.set_mode((640,480), RESIZABLE)

#display_level(current_level)

class Character():
        def __init__(self, window, elements_level):
                self.elements_level = elements_level
                #self.position = position
                self.window = window

        
        def move_char(self, direction):
                #position = self.elements_level[1]
                if direction == "up":
                        #position = position.move(0,int(480/15))
                        self.elements_level[1] = self.elements_level[1].move(0,-int(480/15))
                        print(self.elements_level[1])
                if direction == "down":
                        #position = position.move(0,-int(480/15))
                        self.elements_level[1] = self.elements_level[1].move(0,int(480/15))
                        #print(position)                        
                        print(self.elements_level[1])
                if direction == "left":
                        #position = position.move(-int(640/15),0)
                        self.elements_level[1] = self.elements_level[1].move(-int(480/15),0)
                        #print(position) 
                        print(self.elements_level[1])
                if direction == "right":
                        #position = position.move(int(640/15),0)
                        self.elements_level[1] = self.elements_level[1].move(int(480/15),0)
                        #print(position) 
                        print(self.elements_level[1])
                self.window.blit(self.elements_level[0],self.elements_level[1])
                pg.display.flip()
                

MacGyver = Character(current_window, display_level(current_window, current_level))

def game_loop():
        
        keep_open = 1
        while keep_open :
                for event in pg.event.get(): 
                        if event.type == QUIT :
                                keep_open = 0
                        elif event.type == KEYDOWN:
                                if event.key == K_UP:
                                        MacGyver.move_char("up")
                                if event.key == K_DOWN:
                                        MacGyver.move_char("down")
                                if event.key == K_LEFT:
                                        MacGyver.move_char("left")
                                if event.key == K_RIGHT:
                                        MacGyver.move_char("right")
                                        
                        pg.display.flip()
                                

game_loop()

