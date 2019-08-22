# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 20:04:28 by patrisor          #+#    #+#              #
#    Updated: 2019/08/22 03:53:59 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import Maps
import Objects
import Processing
import random

def spawnEnemies(n, w, h):
    ret = []
    oldX = oldY = 0
    for i in range(n):
        x = random.randint(1, w - 1)
        y = random.randint(1, h - 1)
        if x == oldX and y == oldY: continue
        ret.append(Objects.Enemy(x, y))
        oldX = x
        oldY = y
    return ret

def main():
    MAP_WIDTH = 25
    MAP_HEIGHT = 25
    PLAYER = Objects.Player(int(MAP_WIDTH / 2), int(MAP_HEIGHT / 2))
    ITEMS = Objects.Items()
    ENEMIES = spawnEnemies(2, MAP_WIDTH, MAP_HEIGHT)
    MAP = Maps.TestMap(MAP_WIDTH, MAP_HEIGHT, PLAYER, ITEMS, ENEMIES)
    while True:
        # Print Updated Map
        MAP.printMap(PLAYER, ITEMS)
        # Input
        inp = Processing.processInput(PLAYER, MAP, ITEMS)
        # Update Map, based on input and player position
        MAP.updateMap(inp, PLAYER)
    return(0)

if __name__ == "__main__":
    main()
