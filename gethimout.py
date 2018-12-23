#!/usr/bin/python3
# -*- coding: Utf-8 -*

""""
"Get Him Out !" game :

Help Macgyver escape from the labyrinth by collecting 3 items to put the Guardian to sleep.
"""
import time

import pygame as pg
from pygame.locals import *

from classes import *
from constants import *
from generate_level import *

pg.init()

def create_level(txtfile):
    """Generation of a labyrinth from a static txt file

    in the format of a multi-dimensional list."""
    level = []
    with open(txtfile) as file:
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
                empty_cells.append([x, y])
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

#current_level = create_level(LEVEL1_FILE)

current_window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)



#MacGyver = Character(current_window, display_level(current_window, current_level))

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


heart = pg.image.load(image_heart).convert_alpha()
heart = pg.transform.scale(heart, (int((WIDTH + 10)/SIDE), int(HEIGHT/SIDE)))
skull = pg.image.load(image_skull).convert_alpha()
skull = pg.transform.scale(skull, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))
money = pg.image.load(image_money).convert_alpha()
money = pg.transform.scale(money, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))
gift = pg.image.load(image_gift).convert_alpha()
gift = pg.transform.scale(gift, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))

#Load menu image
menu = pg.image.load(image_menu).convert()
menu = pg.transform.scale(menu, (WIDTH, HEIGHT))
#Load options image
options = pg.image.load(image_options).convert()
options = pg.transform.scale(options, (WIDTH, HEIGHT))
#Load score image
scores = pg.image.load(image_scores).convert()
scores = pg.transform.scale(scores, (WIDTH, HEIGHT))
#Load build image
build = pg.image.load(image_build).convert()
build = pg.transform.scale(build, (WIDTH, HEIGHT))
#Load start image
expl = pg.image.load(image_expl).convert()
expl = pg.transform.scale(expl, (WIDTH, HEIGHT))
#Load character thumbnails
mac = pg.image.load(image_macgyver).convert_alpha()
leela = pg.image.load(image_leela).convert_alpha()
homer = pg.image.load(image_homer).convert_alpha()
mac = pg.transform.scale(mac, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))
leela = pg.transform.scale(leela, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))
homer = pg.transform.scale(homer, (int((WIDTH + 10)/ SIDE), int(HEIGHT/SIDE)))
#Load difficulty image
easy = pg.image.load(image_easy).convert()
easy = pg.transform.scale(easy, (int((WIDTH + 10)/SIDE *2), int(HEIGHT/SIDE *2)))
medium = pg.image.load(image_medium).convert()
medium = pg.transform.scale(medium, (int((WIDTH + 10)/ SIDE *2), int(HEIGHT/SIDE *2)))
hard = pg.image.load(image_hard).convert()
hard = pg.transform.scale(hard, (int((WIDTH + 10)/ SIDE *2), int(HEIGHT/SIDE *2)))



#Here is the game loop :

keep_open = 1
keep_menu = 1
keep_options, keep_scores, keep_build, keep_expl = 0, 0, 0, 0
##MacGyver.display_moves(macg, needle, ether, tube)
#MacGyver.display_moves(macg, needle, ether, tube)
#MacGyver.state = "alive"

current_window.blit(menu, (0, 0))
#pg.display.flip()

print(keep_menu)
print(keep_open)
print(keep_options)
print(keep_scores)
print(keep_build)

#Loop for the menu
while keep_menu:
    pg.time.Clock().tick(30)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == QUIT:
            keep_menu = 0
            keep_open = 0
            print('quit from ')
        if event.type == KEYDOWN:
            if event.key == K_F5:
                keep_menu = 0
                keep_open = 0
                print('quit')
            # Start a new game
            elif event.key == K_F1:
                keep_options = 1
                #keep_menu = 0
                char_index, diff_index = 0, 0

                current_window.blit(options, (0, 0))
                current_window.blit(mac, ((WIDTH/2)-SIDE, HEIGHT/3))
                current_window.blit(easy, ((WIDTH / 2)-SIDE, HEIGHT / 2))
                pg.display.flip()
                pg.event.clear()
                while keep_options:
                    pg.time.Clock().tick(30)
                    characters = [mac, leela, homer]
                    difficulty = [easy, medium, hard]

                    for event in pg.event.get():

                        if event.type == QUIT:
                            keep_options = 0
                            keep_menu = 0
                            keep_open = 0
                            print('quit from start')
                        if event.type == KEYDOWN:
                            if event.key == K_F5:
                                keep_options = 0
                                current_window.blit(menu, (0, 0))
                                pg.display.flip()
                                print('back to menu')

                            #Change character
                            elif event.key == K_c:
                                char_index += 1
                                if char_index == 3:
                                    char_index = 0
                                current_window.blit(options, (0, 0))
                                current_window.blit(characters[char_index], (WIDTH/2, HEIGHT/3))
                                current_window.blit(difficulty[diff_index], (WIDTH / 2, int(HEIGHT / 1.7)))
                                pg.display.flip()
                                print('change char: {0}'.format(char_index))
                                pg.event.clear()

                            # Change difficulty
                            elif event.key == K_d:
                                diff_index += 1
                                if diff_index == 3:
                                    diff_index = 0
                                current_window.blit(options, (0, 0))
                                current_window.blit(characters[char_index], (WIDTH / 2, HEIGHT / 3))
                                current_window.blit(difficulty[diff_index], (WIDTH/2, int(HEIGHT/1.7)))
                                pg.display.flip()
                                print('change difficulty: {0}'.format(diff_index))
                                pg.event.clear()


                            #Get explanations to start the game
                            elif event.key == K_F1:
                                keep_expl = 1
                                keep_options = 0
                                current_window.blit(expl, (0, 0))
                                pg.display.flip()
                                pg.event.clear()
                                opt = [characters[char_index], difficulty[diff_index]]
                                print('options confirmed')

                                while keep_expl:
                                    pg.time.Clock().tick(30)
                                    for event in pg.event.get():
                                        if event.type == QUIT:

                                            keep_menu = 0
                                            keep_open = 0
                                            keep_expl = 0
                                            print('quit from explanations')

                                        if event.type == KEYDOWN:
                                            if event.key == K_F1:
                                                keep_expl = 0
                                                keep_options = 0
                                                keep_menu = 0


                            print(keep_menu)
                            print(keep_open)
                            print(keep_options)
                            print(keep_scores)
                            print(keep_build)

            elif event.key == K_F2:
                keep_scores = 1
                current_window.blit(scores, (0, 0))
                pg.display.flip()
                pg.event.clear()
                while keep_scores:
                    pg.time.Clock().tick(30)
                    for event in pg.event.get():
                        if event.type == QUIT:
                            keep_scores = 0
                            keep_menu = 0
                            keep_open = 0
                            print('quit from start')

                        elif event.key == K_F5:
                            keep_scores = 0
                            current_window.blit(menu, (0, 0))
                            pg.display.flip()
                            print('back to menu')
                        print(keep_menu)
                        print(keep_open)
                        print(keep_start)
                        print(keep_scores)
                        print(keep_build)
            elif event.key == K_F3:
                keep_build = 1
                keep_menu = 0
                current_window.blit(build, (0, 0))
                pg.display.flip()
                pg.event.clear()
                while keep_build:
                    pg.time.Clock().tick(30)
                    for event in pg.event.get():
                        if event.type == QUIT:
                            keep_build = 0
                            keep_menu = 0
                            keep_open = 0
                            print('quit from start')

                        elif event.key == K_F5:
                            keep_build = 0
                            current_window.blit(menu, (0, 0))
                            pg.display.flip()
                            print('back to menu')
                        print(keep_menu)
                        print(keep_open)
                        print(keep_start)
                        print(keep_scores)
                        print(keep_build)

"""
print('Option chosen')
print(keep_menu)
print(keep_open)
print(keep_start)
print(keep_scores)
print(keep_build)

if keep_start:
    keep_start = 1
    current_window.blit(options, (0, 0))
    pg.display.flip()

while keep_start:
    pg.time.Clock().tick(30)
    for event in pg.event.get():
        if event.type == QUIT:
            keep_start = 0
            keep_menu = 0
            keep_open = 0
            print('quit from start')

        elif event.type == KEYDOWN:
            if event.key == K_F5:
                keep_start = 0
                current_window.blit(menu, (0, 0))
                pg.display.flip()
                print('back to menu')

print(keep_menu)
print(keep_open)
print(keep_start)
print(keep_scores)
print(keep_build)
"""

#Level and character initialization
#levels = ["random_level.txt", LEVEL1_FILE, LEVEL2_FILE, LEVEL3_FILE, LEVEL4_FILE, LEVEL5_FILE]
levels = []

for num in range(0,LEVEL_NUMBER):
    filename = 'random_level{0}.txt'.format(num+1)
    generate(filename)
    levels.append(filename)

for level in levels:
    current_level = create_level(level)
    MacGyver = Character(current_window, display_level(current_window, current_level))
    MacGyver.display_moves(macg, needle, ether, tube)
    MacGyver.state = "alive"


    if keep_open:
        display_level(current_window, current_level)
        MacGyver.display_moves(opt[0], needle, ether, tube)
        lifex = SIDE
        for life in range(0, MacGyver.lives):
            current_window.blit(heart, (lifex, SIDE))
            lifex += SIDE * 2
        current_window.blit(money, (7 * WIDTH / 8, SIDE))
        keep_levels = 1

    #Actual game loop
    while keep_levels:
        pg.time.Clock().tick(30)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == QUIT:
                keep_levels = 0
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
                    MacGyver.display_moves(opt[0], needle, ether, tube)
                    lifex = SIDE
                    for life in range(0, MacGyver.lives):
                        current_window.blit(heart, (lifex, SIDE))
                        lifex += SIDE*2
                    current_window.blit(money, (7*WIDTH/8, SIDE))
                    pg.display.flip()
            elif MacGyver.state == "dead":
                current_window.blit(youlose, (0, 0))
                pg.display.flip()
                time.sleep(3)
                keep_open = 0
                keep_levels = 0
                break
            elif MacGyver.state == "won":
                current_window.blit(youwin, (0, 0))
                pg.display.flip()
                time.sleep(3)
                keep_levels = 0
