# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Map.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 00:06:24 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 14:34:01 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

class Map:

    def __init__(self, w, h, p, i):
        ret = [([1] * w)] + ([([1] + ([0] * (w - 2)) + [1]) for _ in range(h - 2)]) + [([1] * w)]
        # Places character
        ret[p.x][p.y] = 2
        # Randomizes Coin drops
        for r in range(25):
            ret[random.randint(1, w - 2)][random.randint(1, h - 2)] = i[0][0]
        self.map = ret

    def controls(self):
        return "WALK: W, A, S, and D\nPAUSE: P\n\n"

    # TODO: update
    def printMap(self, p):
        #FOR TESTING
        '''
        print('\n')
        for r in range(len(self.map)):
            print(' '.join(str(e) for e in self.map[r]))
        '''
        out = ""
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if r == 0:
                    if c == 0: out += "┌"
                    elif c == len(self.map[r]) - 1: out += "┐"
                    else: out += "──"
                if r > 0 and r < len(self.map) - 1:
                    if self.map[r][c] == 1: out += "│"
                    elif self.map[r][c] == 2: out += "🕺"
                    elif self.map[r][c] == 3: out += "💰"
                    else: out += "  "
                if r == len(self.map) - 1:
                    if c == 0: out += "└"
                    elif c == len(self.map[r]) - 1: out += "┘"
                    else: out += "──"
            out += "\n"
        print(out + "CONTROLS:\n" + self.controls() + "SKILLS:\n" + p.skillTreeToString() + "\n\n\n\n")

    # Function SAVES the old address of the player position, then updates it with player pos
    def updateMap(self, i, p):
        self.map[p.x][p.y] = 0
        if i == 'a' or i == 'd': p.y += (1 if i == 'd' else -1)
        if i == 'w' or i == 's': p.x += (1 if i == 's' else -1)
        self.map[p.x][p.y] = 2
        return 0
