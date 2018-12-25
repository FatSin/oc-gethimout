#!/usr/bin/python3
# -*- coding: Utf-8 -*

""""
This file describes all the classes from gethimout.py
"""

import random

import pygame as pg
from pygame.locals import *

class Character():
    """Creation of main character (Macgyver), and animation of the character and

    the objects to pick."""

    def __init__(self, window, elements_level):
        """Automatic creation of an instance of the Character class;"""
        self.elements_level = elements_level
        #self.position = position
        self.window = window
        self.window.blit(self.elements_level[0], self.elements_level[1].topleft)

        self.position1 = random.randint(0, len(self.elements_level[2]) - 1)
        self.position2 = random.randint(0, len(self.elements_level[2]) - 1)
        self.position3 = random.randint(0, len(self.elements_level[2]) - 1)

        self.got_needle = 0
        self.got_ether = 0
        self.got_tube = 0

        self.state = "alive"
        self.lives = 3
        self.score = 0

    def move_char(self, direction):
        """Manages the animation of the main character. The inputs are the arrow

        buttons pressed on the keyboard."""

        list_coor = list(self.elements_level[1].topleft)
        x = list_coor[0]
        y = list_coor[1]

        if direction == "up" and ([x, y - int(480/15)] in self.elements_level[2] or \
                                  [x, y - int(480/15)] == self.elements_level[3]):
            #position = position.move(0,int(480/15))
            self.elements_level[1] = self.elements_level[1].move(0, -int(480/15))
            print(self.elements_level[1])
        elif direction == "down" and ([x, y + int(480/15)] in self.elements_level[2] or \
                                      [x, y + int(480/15)] == self.elements_level[3]):
            #position = position.move(0,-int(480/15))
            self.elements_level[1] = self.elements_level[1].move(0, int(480/15))
            #print(position)
            print(self.elements_level[1])
        elif direction == "left" and ([x - int(640/15), y] in self.elements_level[2] or \
                                      [x - int(640/15), y] == self.elements_level[3]):
            #position = position.move(-int(640/15),0)
            self.elements_level[1] = self.elements_level[1].move(-int(640/15), 0)
            #print(position)
            print(self.elements_level[1])
        elif direction == "right" and ([x + int(640/15), y] in self.elements_level[2] or \
                                       [x + int(640/15), y] == self.elements_level[3]):
            #position = position.move(int(640/15),0)
            self.elements_level[1] = self.elements_level[1].move(int(640/15), 0)
            #print(position)
            print(self.elements_level[1])
        #self.window.blit(self.elements_level[0],self.elements_level[1])
		
    def display_moves(self, person, obj1, obj2, obj3):
        """ Displays the new position of the main character, and the objects."""

        list_coor = list(self.elements_level[1].topleft)

        if list_coor != self.elements_level[2][self.position1] and self.got_needle == 0:
            self.window.blit(obj1, self.elements_level[2][self.position1])
        else:
            self.got_needle = 1
        if list_coor != self.elements_level[2][self.position2] and self.got_ether == 0:
            self.window.blit(obj2, self.elements_level[2][self.position2])
        else:
            self.got_ether = 1
        if list_coor != self.elements_level[2][self.position3] and self.got_tube == 0:
            self.window.blit(obj3, self.elements_level[2][self.position3])
        else:
            self.got_tube = 1

        if list_coor == self.elements_level[3]:
            if self.got_needle == 1 and self.got_ether == 1 and self.got_tube == 1:
                #print("Hourrrrrra !")
                self.state = "won"
            else:
                #print("You looooooose!")
                self.state = "dead"
        #print(self.state)
        self.window.blit(person, list_coor)



        #print("position de macgyver",list_coor)
        #print("position du guardien",self.elements_level[3])
        #print(self.got_needle,self.got_ether,self.got_tube)
        pg.display.flip()

'''
class Guardian:
    def __init__(self, image, coor):
        """Automatic creation of an instance of the Character class;"""
        self.elements_level = elements_level
        # self.position = position
        self.image = image
        self.x = coor[0]
        self.y = coor[1]
        self.radius = int((LENGTHX/4) +1)
        #self.window.blit(self.elements_level[0], self.elements_level[1].topleft)
    def move(self):
        """ Displays the new position of the main character, and the objects."""

        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)
        #print("coordonnées départ")
        #print(coor_d)
        #print(coor_cur)
        x, y = self.x, self.y
        
        move = 0
        if direction == "up" and ([x, y - int(480/15)] in self.elements_level[2] or \
                                  [x, y - int(480/15)] == self.elements_level[3]):
            #position = position.move(0,int(480/15))
            self.y = self.elements_level[1].move(0, -int(480/15))
            #print(self.elements_level[1])
        elif direction == "down" and ([x, y + int(480/15)] in self.elements_level[2] or \
                                      [x, y + int(480/15)] == self.elements_level[3]):
            #position = position.move(0,-int(480/15))
            self.y = self.elements_level[1].move(0, int(480/15))
            #print(position)
            #print(self.elements_level[1])
        elif direction == "left" and ([x - int(640/15), y] in self.elements_level[2] or \
                                      [x - int(640/15), y] == self.elements_level[3]):
            #position = position.move(-int(640/15),0)
            self.x = self.elements_level[1].move(-int(640/15), 0)
            #print(position)
            #print(self.elements_level[1])
        elif direction == "right" and ([x + int(640/15), y] in self.elements_level[2] or \
                                       [x + int(640/15), y] == self.elements_level[3]):
            #position = position.move(int(640/15),0)
            self.elements_level[1] = self.elements_level[1].move(int(640/15), 0)
            #print(position)
            print(self.elements_level[1])

        list_coor = list(self.elements_level[1].topleft)

        if list_coor != self.elements_level[2][self.position1] and self.got_needle == 0:
            self.window.blit(obj1, self.elements_level[2][self.position1])
        else:
            self.got_needle = 1
        if list_coor != self.elements_level[2][self.position2] and self.got_ether == 0:
            self.window.blit(obj2, self.elements_level[2][self.position2])
        else:
            self.got_ether = 1
        if list_coor != self.elements_level[2][self.position3] and self.got_tube == 0:
            self.window.blit(obj3, self.elements_level[2][self.position3])
        else:
            self.got_tube = 1

        if list_coor == self.elements_level[3]:
            if self.got_needle == 1 and self.got_ether == 1 and self.got_tube == 1:
                #print("Hourrrrrra !")
                self.state = "won"
            else:
                #print("You looooooose!")
                self.state = "dead"
        #print(self.state)
        self.window.blit(self.image, list_coor)

'''