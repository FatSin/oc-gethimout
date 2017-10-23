#!/usr/bin/python3
# -*- coding: Utf-8 -*

""""
"Get Him Out !" game :

Help Macgyver escape from the labyrinth by collecting 3 items to put the Guardian to sleep.
"""

import pygame as pg
from pygame.locals import *

from classes import *
from constants import *

pg.init()

def create_level():
    """Generation of a labyrinth from a static txt file

    in the format of a multi-dimensional list."""
    level = []
    with open(LEVEL_FILE) as file:
        for line in file:
            lines = []
            for cell in line:
                if cell != '\n':
                    lines.append(cell)
            level.append(lines)
    #print("Here is the labyrinth as a list:",level)
    #print("Here is the 4rth row:", level[3])
    return level


def display_level(window, level):
    """2D-display of the previously generated labyrinth."""

    background = pg.image.load(image_background).convert()
    background = pg.transform.scale(background, (WIDTH, HEIGHT))
    window.blit(background, (0, 0))
    wall = pg.image.load(image_wall).convert()
    start = pg.image.load(image_start).convert_alpha()
    guardian = pg.image.load(image_guardian).convert_alpha()
    mac = pg.image.load(image_macgyver).convert_alpha()
    #Redimensioning of the images, to adapt to the window size
    wall = pg.transform.scale(wall, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
    start = pg.transform.scale(start, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
    guardian = pg.transform.scale(guardian, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
    mac = pg.transform.scale(mac, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
    #Static positioning of the labyrinth and the characters
    num_line = 0
    empty_cells = [] #List of empty cells
    position_guardian = []
    for line in level:
        num_col = 0
        y = num_line * int(HEIGHT/SIDE)
        for cell in line:
            x = num_col * int(WIDTH/15)
            if cell == "w":
                window.blit(wall, (x, y))
            if cell == "d":
                window.blit(start, (x, y))
                position_macgyver = mac.get_rect()
                position_macgyver.center = (x + int((WIDTH/(SIDE*2))), y + int((HEIGHT/(SIDE * 2))))
            if cell == "f":
                window.blit(guardian, (x, y))
                position_guardian = [x, y]
            if cell == "n":
                pass
            elif cell == "0":
                empty_cells.append([x, y])
            num_col += 1
        num_line += 1
    elements = [mac, position_macgyver, empty_cells, position_guardian]
    return elements

current_level = create_level()

current_window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)



MacGyver = Character(current_window, display_level(current_window, current_level))

macg = pg.image.load(image_macgyver).convert_alpha()
needle = pg.image.load(image_needle).convert_alpha()
ether = pg.image.load(image_ether).convert_alpha()
tube = pg.image.load(image_tube).convert_alpha()
youwin = pg.image.load(image_youwin).convert()
youlose = pg.image.load(image_youlose).convert()

macg = pg.transform.scale(macg, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))
needle = pg.transform.scale(needle, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
ether = pg.transform.scale(ether, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
tube = pg.transform.scale(tube, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
youwin = pg.transform.scale(youwin, (WIDTH, HEIGHT))
youlose = pg.transform.scale(youlose, (WIDTH, HEIGHT))

menu = pg.image.load(image_menu).convert()
menu = pg.transform.scale(menu, (WIDTH, HEIGHT))

#Here is the game loop :

keep_open = 1
keep_menu = 1
MacGyver.display_moves(macg, needle, ether, tube)
MacGyver.state = "alive"

current_window.blit(menu, (0, 0))
pg.display.flip()

#Loop for the menu
while keep_menu:
    pg.time.Clock().tick(30)
    for event in pg.event.get():
        if event.type == QUIT:
            keep_menu = 0
            keep_open = 0
        if event.type == KEYDOWN:
            if event.key == K_F1:
                keep_menu = 0

if keep_open:
    display_level(current_window, current_level)
    MacGyver.display_moves(macg, needle, ether, tube)

#Actual game loop
while keep_open:
    pg.time.Clock().tick(30)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == QUIT:
            keep_open = 0
        if MacGyver.state == "alive":
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
                MacGyver.display_moves(macg, needle, ether, tube)
        elif MacGyver.state == "dead":
            current_window.blit(youlose, (0, 0))
            pg.display.flip()
        elif MacGyver.state == "won":
            current_window.blit(youwin, (0, 0))
            pg.display.flip()
