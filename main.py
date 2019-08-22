# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rpapagna <rpapagna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 20:04:28 by patrisor          #+#    #+#              #
#    Updated: 2019/08/22 04:08:26 by rpapagna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('utils')
import Getch				#key input
import Screens				#screen interfaces
sys.path.append('menu')
import Menu
sys.path.append('src')
import Maps
import Objects
import Processing

def main():
    MAP_WIDTH = 25
    MAP_HEIGHT = 25
    PLAYER = Objects.Player(int(MAP_WIDTH / 2), int(MAP_HEIGHT / 2))
    ITEMS = Objects.Items()
    MAP = Maps.TestMap(MAP_WIDTH, MAP_HEIGHT, PLAYER, ITEMS)
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
