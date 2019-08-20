# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 20:04:28 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 14:22:16 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import Map
import Objects
import Auxiliary
import sys,tty,termios
import random

# UPGRADED INPUT()
class _Getch:       
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    return k

# Quits our game if input is 'q'
def die(i):
    if i == "q":
        print("Goodbye!")
        exit(-1)

# TODO
#def itemPickUp():

'''PROCESSING'''
# Takes in a valid-input parameter, and a valid data type you want to comapre it to
# Returns array of these found parameters
def isValid(inp, inputs):
    ret = ''
    for x in inputs:
        if x == inp: ret += str(x)
    return(ret)

# Basic processing of input to see if input is valid
# Checks if key passed was valid to aid with collision
def processInput():
    # NOTE: If you want the ability to add more items, then add another function call to this list, and
    # update the third parameter to the item you are looking for
    keys = [Auxiliary.check_collision(PLAYER, MAP.map, 1), Auxiliary.check_collision(PLAYER, MAP.map, 3)]
    while True: 
        ret = get()
        if die(ret[0]) or isValid(ret, valid_inputs) == '': 
            print("Invalid Input\r") 
            continue 
        # Collision detected if length of keys is greater than 0
        if Auxiliary.isCollided(keys, 0, ret): 
            print("Wall in the way")
            continue
        # Update User Skill Tree 
        # 3: equals to coins
        if Auxiliary.isCollided(keys, 1, ret):
            PLAYER.gold += random.randint(5, 15)
        return ret

# MAIN
valid_inputs = ['w', 'a', 's', 'd', 'p']
MAP_WIDTH = 25
MAP_HEIGHT = 25
PLAYER = Objects.Player(int(MAP_WIDTH / 2), int(MAP_HEIGHT / 2))
# TODO: Convert to class
ITEMS = [[3]] + [[s for s in range(4, 14, 1)]] + [[p for p in range(14, 24, 1)]]
MAP = Map.Map(MAP_WIDTH, MAP_HEIGHT, PLAYER, ITEMS)
while True:
    # Print Updated Map
    MAP.printMap(PLAYER)
    # Input
    inp = processInput()
    # Update Map, based on input and player position
    MAP.updateMap(inp, PLAYER)
exit(0)
