# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Objects.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 23:45:38 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 14:15:44 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Player:

    gold = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.attack = 1
        self.experience = 0
        self.mana = 50

    # TODO: Add 
    def skillTreeToString(self):
        return("GOLD: " + str(self.gold))
