import getch				#key input
import screens				#screen interfaces
import menu 				#menu access

SCREEN_W = 30		#global menu screen dimentions
SCREEN_H = 22

class Player:
	def __init__(self, x, y):
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
            return("GOLD: " + str(self.gold) + "\nATTACK: " + str(self.attack))

def env():
	menu.openMenu(p, SCREEN_W, SCREEN_H)

env()
