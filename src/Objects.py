# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Objects.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 23:45:38 by patrisor          #+#    #+#              #
#    Updated: 2019/08/21 01:59:22 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Player:

    def __init__(self, x, y):
        self.id = 2
        self.x = x
        self.y = y
        self.health = 100
        self.attack = 1
        self.experience = 0
        self.mana = 50
        self.gold = 0

    # TODO: Add 
    def skillTreeToString(self):
        return("GOLD: " + str(self.gold) + "\nATTACK: " + str(self.attack))

class Enemy:

    def __init__(self, x, y):
        self.id = 20
        self.x = x
        self.y = y
        self.health = 10
        self.attack = 10

class Items:

    def __init__(self):
        #self.inventory = [[3]] + [[s for s in range(4, 14, 1)]] + [[p for p in range(14, 24, 1)]]
        self.KNIFE = 4
        self.COINS = 3
