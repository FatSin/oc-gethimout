#!/usr/bin/python3
# -*- coding: Utf-8 -*

""""
This file describes how levels are generated and saved into .txt files
"""

import random

from constants import *

#len_x = int(WIDTH/SIDE)
#len_y = int(HEIGHT/SIDE)




len_x = LENGTHX
len_y = LENGTHY

def generate(custom_file):
    T = []
    for i in range(0,len_y):
        T_cur = []
        for j in range(0,len_x):
            #T_cur.append("X{1}Y{0}".format(i+1,j+1))
            T_cur.append([j,i,"none"])
        T.append(T_cur)
    print(T)

    T_bord = []

    for tilelist in T:
        T_bord.append(tilelist[0])
        #T_bord.append(tilelist[len_x-1])

    coor_d = random.choice(T_bord)
    coor_cur = [coor_d[0],coor_d[1], "0"]

    for tilelist in T:
        #T_bord.append(tilelist[0])
        T_bord.append(tilelist[len_x-1])
    for tile in T[0]:
        T_bord.append(tile)
    for tile in T[len_y-1]:
        T_bord.append(tile)

    print ('T bord :')
    print(T_bord)

    #coor_d = random.choice(T_bord)
    #coor_cur = [coor_d[0],coor_d[1], "0"]

    print('d is in {0},{1}'.format(coor_d[0],coor_d[1] ))

    for tilelist in T:
        for tile in tilelist:
            if tile[0] == coor_d[0] and tile[1] == coor_d[1]:
                tile[2] = "d"

    min_free = len_x*3
    count_free = 0
    max_never = len_x*2
    count_never = 0
    directions = ['up', 'down', 'left', 'right']

    create = 1
    move = 1


    while create:
        dir = random.choice(directions)
        print("coordonnées départ")
        print(coor_d)
        print(coor_cur)
        x_temp, y_temp = coor_cur[0], coor_cur[1]
        move = 0
        if dir == "up":
            if coor_cur[1] + 1 < len_y:
                y_temp = coor_cur[1] + 1
                print(dir)
                move = 1
        elif dir == "down":
            if coor_cur[1] - 1 > 0:
                y_temp = coor_cur[1] - 1
                print(dir)
                move = 1
        elif dir == "left":
            if coor_cur[0] - 1 > 0:
                x_temp = coor_cur[0] - 1
                print(dir)
                move = 1
        elif dir == "right":
            if coor_cur[0] + 1 < len_x:
                x_temp = coor_cur[0] + 1
                print(dir)
                move = 1
        print("move:{}".format(move))
        if move:
            print('coor temp {0},{1}'.format(x_temp, y_temp))
            print('coor de d {0},{1}'.format(coor_d[0], coor_d[1]))
            print('cases libres {0}/{1}'.format(count_free, min_free))
            if (x_temp != coor_d[0] or y_temp != coor_d[1]):
                print('correct move')
                #print('coor temp {0},{1}'.format(x_temp, y_temp))
                coor_cur[0] = x_temp
                coor_cur[1] = y_temp
                print('coor finales {0},{1}'.format(x_temp, y_temp))
                if count_free > min_free and coor_cur in T_bord:
                    #f must not be close to d
                    dist_x = int(coor_cur[0] - coor_d[0])
                    dist_y = int(coor_cur[1] - coor_d[1])
                    print("distances pour f :{0},{1}".format(dist_x, dist_y))
                    if dist_x >= len_x/2 or dist_y >= len_y/2:
                        coor_cur[2] = "f"
                        #replace in T
                        create = 0
                else:
                    coor_cur[2] = "0"
                    #replace in T
                    count_free += 1
                for tilelist in T:
                    for tile in tilelist:
                        if tile[0] == coor_cur[0] and tile[1] == coor_cur[1]:
                            tile[2] = coor_cur[2]
        else:
            print('incorrect move')
    print(T)

    for tilelist in T:
        for tile in tilelist:
            if tile[2] == "none":
                #print('a remplir')
                if count_never < max_never:
                    tile[2] = random.choice(["n", "w", "w"])
                    count_never += 1
                else:
                    tile[2] = "w"

    print('final result :')
    print(T)

    with open(custom_file, "w") as file:
        for tilelist in T:
            for tile in tilelist:
                file.write(tile[2])
            file.write('\n')
    file.close()
