# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Processing.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/21 01:34:12 by patrisor          #+#    #+#              #
#    Updated: 2019/08/21 01:42:41 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import Auxiliary
import Getch
import random

# Quits our game if input is 'q'
def die(i):
    if i == "q":
        print("Goodbye!")
        exit(-1)

# Update User Skill Tree
def itemPickUp(p, c, r):
    if Auxiliary.isCollided(c, 1, r): # GOLD
        p.gold += random.randint(5, 15)
    if Auxiliary.isCollided(c, 2, r): #SWORD
        p.attack += 15

# Takes in a valid-input parameter, and a valid data type you want to comapre it to
# Returns array of these found parameters
def isValid(inp, inputs):
    ret = ''
    for x in inputs:
        if x == inp: ret += str(x)
    return(ret)

# Basic processing of input to see if input is valid
# Checks if key passed was valid to aid with collision
def processInput(p, m, i, valid_inputs = ['w', 'a', 's', 'd', 'p']):
    collisions = Auxiliary.getCollisions(p, m, i)
    while True:
        ret = Getch.get()
        if die(ret[0]) or isValid(ret, valid_inputs) == '':
            print("Invalid Input\r")
            continue
        # NOTE: DO NOT DELETE -> Collision detected if length of keys is greater than 0
        if Auxiliary.isCollided(collisions, 0, ret): continue
        # Update User Skill Tree
        itemPickUp(p, collisions, ret)
        return ret