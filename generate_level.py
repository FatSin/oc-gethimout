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

"""
def calculate_density(coorx, coory, tile, map):
    if (abs(tile[0] - coorx) < 2 and abs(tile[1] - coory) < 2) and tile[2] == "0":
        nb_neigh = 0
        for othertlist in map:
            for othertile in othertlist:
                if (abs(othertile[0] - tile[0]) < 2 and abs(othertile[1] - tile[1]) < 2) and \
                        (othertile[0] != tile[0] or othertile[1] != tile[1]):
                    if othertile[2] == "0":
                        nb_neigh += 1
    return nb_neigh
"""

def generate(custom_file):
    T = []
    for i in range(0,len_y):
        T_cur = []
        for j in range(0,len_x):
            #T_cur.append("X{1}Y{0}".format(i+1,j+1))
            T_cur.append([j,i,"none"])
        T.append(T_cur)
    #print(T)

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

    #print ('T bord :')
    #print(T_bord)

    #coor_d = random.choice(T_bord)
    #coor_cur = [coor_d[0],coor_d[1], "0"]

    #print('d is in {0},{1}'.format(coor_d[0],coor_d[1] ))

    for tilelist in T:
        for tile in tilelist:
            if tile[0] == coor_d[0] and tile[1] == coor_d[1]:
                tile[2] = "d"

    #Direction for the tile creation, based on where is the start

    dir_horiz, dir_vert = "", ""
    if coor_d[0] < int(len_x/2):
        dir_horiz = "right"
    if coor_d[0] > int(len_x/2):
        dir_horiz = "left"
    if coor_d[1] < int(len_y/2):
        dir_vert = "up"
    if coor_d[1] > int(len_y/2):
        dir_vert = "down"



    min_free = len_x*7
    count_free = 0
    max_never = len_x*2
    count_never = 0
    #directions = ['up', 'down', 'left', 'right']

    create = 1
    move = 1
    force_move = 0

    #directions  = ['up', 'down', 'left', 'right', dir_horiz, dir_horiz, dir_vert, dir_vert]
    #directions = ['up', 'down', 'left', 'right', dir_horiz, dir_vert]
    directions = ['up', 'down', 'left', 'right']

    while create:

        dir = random.choice(directions)
        #print('directions restantes :{0}'.format(directions))
        #print("coordonnées départ")
        #print(coor_d)
        #print(coor_cur)
        x_temp, y_temp = coor_cur[0], coor_cur[1]
        move = 0
        good_dir = 0
        if dir == "up":
            if coor_cur[1] + 1 < len_y:
                y_temp = coor_cur[1] + 1
                print(dir)
                good_dir = 1
            else:
                print('Sort du cadre')
        elif dir == "down":
            if coor_cur[1] - 1 >= 0:
                y_temp = coor_cur[1] - 1
                print(dir)
                good_dir = 1
            else:
                print('Sort du cadre')
        elif dir == "left":
            if coor_cur[0] - 1 >= 0:
                x_temp = coor_cur[0] - 1
                print(dir)
                good_dir = 1
            else:
                print('Sort du cadre')
        elif dir == "right":
            if coor_cur[0] + 1 < len_x:
                x_temp = coor_cur[0] + 1
                print(dir)
                good_dir = 1
            else:
                print('Sort du cadre')
        print("move:{}".format(move))

        # Calculation of density
        # Retrieve the neighbourhood of the destination

        max_neigh = 4

        """
        for tilelist in T:
            for tile in tilelist:
                if (abs(tile[0] - x_temp) < 2 and abs(tile[1] - y_temp) < 2):
                    nb_neigh = 0
                    for othertlist in T:
                        for othertile in othertlist:
                            if (abs(othertile[0] - tile[0]) < 2 and abs(othertile[1] - tile[1]) < 2) and\
                                    (othertile[0] != tile[0] or othertile[1] != tile[1]):
                                if othertile[2] == "0":
                                    nb_neigh += 1
                    print('Coor du voisin: {0},{1}'.format(tile[0], tile[1]))
                    print('Voisins du voisin: {0}'.format(nb_neigh))
                    if nb_neigh > max_neigh:
                        move = 0
                        print("too dense!")
                        break
        """
        if good_dir:
            move = 1
            quarter1, quarter2, quarter3, quarter4 = 0, 0, 0, 0
            if force_move == 0:
                print('cases libres {0}/{1}'.format(count_free, min_free))
                for tilelist in T:
                    for tile in tilelist:
                        if tile[2] == "0":
                            if (tile[0] != x_temp or tile[1] != y_temp):
                                if (0 <= x_temp - tile[0] <=1) and  (-1 <= y_temp - tile[1] <=0):
                                    quarter1 +=1
                                if (-1 <= x_temp - tile[0] <=0) and  (-1 <= y_temp - tile[1] <=0):
                                    quarter2 +=1
                                if (-1 <= x_temp - tile[0] <=0) and  (0 <= y_temp - tile[1] <=1):
                                    quarter3 +=1
                                if (0 <= x_temp - tile[0] <=1) and  (0 <= y_temp - tile[1] <=1):
                                    quarter4 +=1
                            else:
                                count_free -= 1
                if quarter1 >= 3 or quarter2 >= 3 or quarter3 >= 3 or quarter4 >= 3:
                    if [x_temp, y_temp, 'none'] in T_bord:
                        print('On est au bord. Elligible !')
                        if count_free > min_free:
                            # f must not be close to d
                            dist_x = int(x_temp - coor_d[0])
                            dist_y = int(y_temp - coor_d[1])
                            print("distances pour f :{0},{1}".format(dist_x, dist_y))
                            if dist_x >= len_x / 2 or dist_y >= len_y / 2:
                                coor_cur[2] = "f"
                                # replace in T
                                create = 0
                                # move = 1
                            else:
                                move = 0
                                print("ça fait un carré!")
                        else:
                            move = 0
                            print("ça fait un carré!")
                    else:
                        print("On n'est pas au bord. Dommage !")
                        move = 0
                        print("ça fait un carré!")



                        """
                        if (abs(tile[0] - x_temp) < 2 and abs(tile[1] - y_temp) < 2) and tile[2] == "0":
                            nb_neigh = 0
                            for othertlist in T:
                                for othertile in othertlist:
                                    if (abs(othertile[0] - tile[0]) < 2 and abs(othertile[1] - tile[1]) < 2) and \
                                            (othertile[0] != tile[0] or othertile[1] != tile[1]):
                                        if othertile[2] == "0":
                                            nb_neigh += 1
                            print('Coor du voisin: {0},{1}'.format(tile[0], tile[1]))
                            print('Voisins du voisin: {0}'.format(nb_neigh))
                            if nb_neigh > max_neigh:
                                if [x_temp, y_temp, 'none'] in T_bord:
                                    print('On est au bord. Elligible !')
                                    if count_free > min_free:
                                        # f must not be close to d
                                        dist_x = int(x_temp - coor_d[0])
                                        dist_y = int(y_temp - coor_d[1])
                                        print("distances pour f :{0},{1}".format(dist_x, dist_y))
                                        if dist_x >= len_x / 2 or dist_y >= len_y / 2:
                                            coor_cur[2] = "f"
                                            # replace in T
                                            create = 0
                                            #move = 1
                                else:
                                    print("On n'est pas au bord. Dommage !")
                                    move = 0
                                    print("too dense!")
                                break
                                """
            else:
                force_move = 0

        if move:
            #print('coor temp {0},{1}'.format(x_temp, y_temp))
            #print('coor de d {0},{1}'.format(coor_d[0], coor_d[1]))




            #if (x_temp != coor_d[0] or y_temp != coor_d[1]):
            #print('correct move')
            #print('coor temp {0},{1}'.format(x_temp, y_temp))
            coor_cur[0] = x_temp
            coor_cur[1] = y_temp
            #print('nouveau coor_cur {0}'.format(coor_cur))
            #print('coor finales {0},{1}'.format(x_temp, y_temp))
            if coor_cur[2] == "f":
                create = 0

            elif (count_free >= min_free and ([x_temp, y_temp, 'none'] in T_bord)):
                #f must not be close to d
                dist_x = int(abs(coor_cur[0] - coor_d[0]))
                dist_y = int(abs(coor_cur[1] - coor_d[1]))
                print("distances pour f :{0},{1}".format(dist_x, dist_y))
                if dist_x >= len_x/2 or dist_y >= len_y/2:
                    coor_cur[2] = "f"
                    #replace in T
                    create = 0
            elif (x_temp == coor_d[0] and y_temp == coor_d[1]):
                coor_cur[2] = "d"
            else:
                coor_cur[2] = "0"
                #replace in T
                count_free += 1
            for tilelist in T:
                for tile in tilelist:
                    if tile[0] == coor_cur[0] and tile[1] == coor_cur[1]:
                        tile[2] = coor_cur[2]
            #directions = ['up', 'down', 'left', 'right', dir_horiz, dir_horiz, dir_vert, dir_vert]
            #directions = ['up', 'down', 'left', 'right', dir_horiz, dir_vert]
            directions = ['up', 'down', 'left', 'right']
        else:
            #print('incorrect move')
            directions.pop(directions.index(dir))
            if len(directions) == 0:
                directions = [dir_horiz, dir_vert]
                force_move = 1
                #print('Move is forced !')
        #print(T)

    for tilelist in T:
        for tile in tilelist:
            if tile[2] == "none":
                #print('a remplir')
                if count_never < max_never:
                    tchoice = random.choice(["w", "w", "w"])
                    tile[2] = tchoice
                    if tchoice == "n":
                        for othertlist in T:
                            for othertile in othertlist:
                                if (abs(othertile[0] - tile[0]) < 2 and abs(othertile[1] - tile[1]) < 2) and \
                                        (othertile[0] != tile[0] or othertile[1] != tile[1]):
                                    if othertile[2] == "0":
                                        tile[2] = "0"

                        count_never += 1
                else:
                    tile[2] = "w"

    #print('final result :')
    #print(T)
    #print('Le bord :')
    #print(T_bord)

    with open(custom_file, "w") as file:
        for tilelist in T:
            for tile in tilelist:
                file.write(tile[2])
            file.write('\n')
    file.close()
