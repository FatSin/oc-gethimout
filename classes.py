#!/usr/bin/python3
# -*- coding: Utf-8 -*

""""
This file describes all the classes from gethimout.py
"""

import random

import pygame as pg
from pygame.locals import *

from constants import *

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
        self.position4 = random.randint(0, len(self.elements_level[2]) - 1)
        self.position5 = random.randint(0, len(self.elements_level[2]) - 1)
        self.position6 = random.randint(0, len(self.elements_level[2]) - 1)

        self.got_needle = 0
        self.got_ether = 0
        self.got_tube = 0
        self.got_gift = 0
        self.got_5, self.got_6 = 0, 0

        self.state = "alive"
        self.lives = 3
        self.score = 0

        self.needle = pg.image.load(image_needle).convert_alpha()
        self.ether = pg.image.load(image_ether).convert_alpha()
        self.tube = pg.image.load(image_tube).convert_alpha()
        self.needle = pg.transform.scale(self.needle, (int((WIDTH + 10) / SIDE), int(HEIGHT / SIDE)))
        self.ether = pg.transform.scale(self.ether, (int((WIDTH + 10) / SIDE), int(HEIGHT / SIDE)))
        self.tube = pg.transform.scale(self.tube, (int((WIDTH + 10) / SIDE), int(HEIGHT / SIDE)))

        self.heart = pg.image.load(image_heart).convert_alpha()
        self.heart = pg.transform.scale(self.heart, (int(WIDTH / 9), int(HEIGHT / 8)))
        self.skull = pg.image.load(image_skull).convert_alpha()
        self.skull = pg.transform.scale(self.skull, (int(WIDTH / 9), int(HEIGHT / 8)))
        self.money = pg.image.load(image_money).convert_alpha()
        self.money = pg.transform.scale(self.money, (int(WIDTH / 9), int(HEIGHT / 8)))
        self.gift = pg.image.load(image_gift).convert_alpha()
        self.gift = pg.transform.scale(self.gift, (int((WIDTH + 10) / SIDE), int(HEIGHT / SIDE)))

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
		
    #def display_moves(self, person, obj1, obj2, obj3, obj4, diff):
    def display_moves(self, person, diff, numlevel):
        """ Displays the new position of the main character, and the objects."""



        list_coor = list(self.elements_level[1].topleft)

        if (diff == 1 and numlevel > 3) or (diff == 2 and 1 < numlevel < 4):
            max_got = 4
        elif diff == 2 and numlevel > 4:
            max_got = 5
        else:
            max_got = 3




        if list_coor != self.elements_level[2][self.position1] and self.got_needle == 0:
            self.window.blit(self.needle, self.elements_level[2][self.position1])
        else:
            self.got_needle = 1
        if list_coor != self.elements_level[2][self.position2] and self.got_ether == 0:
            self.window.blit(self.ether, self.elements_level[2][self.position2])
        else:
            self.got_ether = 1
        if list_coor != self.elements_level[2][self.position3] and self.got_tube == 0:
            self.window.blit(self.tube, self.elements_level[2][self.position3])
        else:
            self.got_tube = 1


        if max_got == 4:
            if list_coor != self.elements_level[2][self.position5] and self.got_5 == 0:
                self.window.blit(self.ether, self.elements_level[2][self.position5])
            else:
                self.got_5 = 1

        if max_got == 5:
            if list_coor != self.elements_level[2][self.position6] and self.got_6 == 0:
                self.window.blit(self.tube, self.elements_level[2][self.position6])
            else:
                self.got_6 = 1

        if diff > 0:

            if list_coor != self.elements_level[2][self.position4] and self.got_gift == 0:
                self.window.blit(self.gift, self.elements_level[2][self.position4])
            else:
                if self.got_gift == 0:
                    ind = random.randint(0,2)
                    if ind == 0:
                        self.window.blit(self.heart, (WIDTH/2, HEIGHT/2))
                        if self.lives < 3:
                            self.lives+=1
                    elif ind == 1:
                        self.window.blit(self.skull, (WIDTH/2, HEIGHT/2))
                        self.lives-=1
                        if self.lives < 0:
                            self.state = "dead"
                    elif ind == 2:
                        self.window.blit(self.money, (WIDTH/2, HEIGHT/2))
                        self.score += 100
                self.got_gift = 1
                #else:
                #    self.got_gift = 1

        if list_coor == self.elements_level[3]:
            if (self.got_needle + self.got_ether + self.got_tube + self.got_5 + self.got_6) >= max_got:
                #print("Hourrrrrra !")
                self.state = "won"
            else:
                #print("You looooooose!")
                self.state = "dead"




        """
        if list_coor == self.elements_level[3]:
            if self.got_needle == 1 and self.got_ether == 1 and self.got_tube == 1:
                #print("Hourrrrrra !")
                self.state = "won"
            else:
                #print("You looooooose!")
                self.state = "dead"
        #print(self.state)
        """
        self.window.blit(person, list_coor)



        #print("position de macgyver",list_coor)
        #print("position du guardien",self.elements_level[3])
        #print(self.got_needle,self.got_ether,self.got_tube)
        pg.display.flip()


'''
class Minion:
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