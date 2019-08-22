# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Objects.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 23:45:38 by patrisor          #+#    #+#              #
#    Updated: 2019/08/22 04:46:17 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Player:
    def __init__(self, x, y):
        self.id = 2
        self.x = x
        self.y = y
        self.attributes = {
        'level': 1,
        'xp': 0,
        'Health': 50,
        'Mana': 20,
        'Strength': 6,
        'Defense': 0,
        }
        self.weapon = ["None", 0]
        self.armor = ["Chest Plate", 6]
        self.gold = 0

    # Increases stats (p = Player; k = skill you want affected)
    def increase(self, p, k):
        x = int(p.attributes['level'] / 5)
        y = int(p.attributes['level'] % 5)
        z = int(p.attributes['level'] * .825884)
        if y < 2:
                y += 1
        else:
                y = 3
        if k == "Health":
                p.attributes[k] = p.attributes[k] + z + (((2 * (10 * x)) + 5  + 15) * y)
                p.attributes[k] = p.attributes[k] - p.attributes[k] % (p.attributes['level'] * 3 + p.attributes['level']) * 5
                p.attributes[k] = p.attributes[k] - p.attributes[k] % 5
        elif k == "Mana":
                p.attributes[k] = p.attributes[k] + z + (((((x + 1) * 5) * 2) - 1) + y)
                p.attributes[k] = p.attributes[k] - p.attributes[k] % 5
        else:
                val = int(((z + x + y) * 10) / 10)
                val = p.attributes[k] % y + val
                p.attributes[k] += int((val / 2) + 1)
        p.attributes['xp'] -= 100
        p.attributes['Health'] += 5
        p.attributes['Strength'] += 1
        p.attributes['Defense'] += 1
        p.attributes['level'] += 1

        # TODO: Add
    def skillTreeToString(self):
        ret = "HEALTH: " + str(self.attributes["Health"])
        ret += "\nATTACK: " + str(self.attributes["Strength"])
        ret += "\nGOLD: " + str(self.gold)
        return(ret)

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
