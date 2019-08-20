# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 20:04:28 by patrisor          #+#    #+#              #
#    Updated: 2019/08/19 23:01:36 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''AUXILIARY FUNCTIONS'''
# COLLISION DETECTION
'''
if (rect1.x < rect2.x + rect2.width &&
   rect1.x + rect1.width > rect2.x &&
   rect1.y < rect2.y + rect2.height &&
   rect1.y + rect1.height > rect2.y) {
    // collision detected!
}
m[p.x + 1][p.y]: Checks for wall under you; if there is boundary, return 's'
m[p.x - 1][p.y]: Checks for wall above you; if there is boundary, return 'w'
m[p.x][p.y + 1]: Checks for wall to the right; if there is boundary, return 'd'
m[p.x][p.y - 1]: Checks for wall to the left; if there is boundary, return 'a'
'''
# RETURN List of where it can't go
def collided(p, m):
    ret = []
    if m[p.x][p.y + 1] == 1 or m[p.x][p.y - 1] == 1:
        ret.append(('d' if m[p.x][p.y + 1] == 1 else 'a'))
    if m[p.x + 1][p.y] == 1 or m[p.x - 1][p.y] == 1:
        ret.append(('s' if m[p.x + 1][p.y] == 1 else 'w'))
    return ret

'''PLAYER'''
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

'''MAP'''
# TODO: update
def printMap(m):
    for r in range(len(m)):
        print(' '.join(str(e) for e in m[r]))
    '''
    out = ""
    for r in range(len(m)):
        for c in range(len(m[r])):
            if r == 0:
                out += "-"
            if r > 0 and r < len(m) - 1:
                if m[r][c] == 1:
                    out += "|"
                elif m[r][c] == 2:
                    out += "P"
                else:
                    out += " "
            if r == len(m) - 1:
                out += "-"
        out += "\n"
    print(out)
    '''

# Function wipes the old address of the player position, then updates it
def updateMap(m, i, p):
    m[p.x][p.y] = 0
    if i == 'a' or i == 'd':
        p.y += (1 if i == 'd' else -1)
    if i == 'w' or i == 's':
        p.x += (1 if i == 's' else -1)
    m[p.x][p.y] = 2
    return 0

def initMap(w, h, p):
    ret = [([1] * w)] + ([([1] + ([0] * (w - 2)) + [1]) for _ in range(h - 2)]) + [([1] * w)]
    ret[p.x][p.y] = 2
    return ret

'''INPUT'''
def die(i):
    if i == "q":
        print("Goodbye!")
        exit(-1)

def controls():
    return "WALK: W, A, S, and D\n"

def processInput(invalid_keys):
    ret = ""
    while True:
        ret = raw_input(controls())
        if (len(ret) != 1):
            print("Invalid Input")
            continue
        ret = ret.lower()
        if die(ret) or ret != 'w' and ret != 'a' and ret != 's' and ret != 'd':
            print("Invalid Input")
            continue
        for i in invalid_keys:
            if i == ret:
                return -1
        return ret

MAP_WIDTH = 25
MAP_HEIGHT = 25
PLAYER = Player(MAP_WIDTH / 2, MAP_HEIGHT / 2)
MAP = initMap(MAP_WIDTH, MAP_HEIGHT, PLAYER)
invalid_keys = []
while True:
    printMap(MAP)
    inp = processInput(invalid_keys)
    if inp == -1:
        print("You cannot go there")
        continue
    updateMap(MAP, inp, PLAYER)
    # TODO: Conditions
    invalid_keys = collided(PLAYER, MAP)
    print("Cannot Go: " + ' '.join(invalid_keys))
