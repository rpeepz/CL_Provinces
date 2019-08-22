import sys
sys.path.append('utils')
import Getch				#key input
import Screens				#screen interfaces
sys.path.append('menu')
import Menu 				#menu access

SCREEN_W = 30		#global menu screen dimentions
SCREEN_H = 22

class Player:
	def __init__(self, level, xp, hp, mana, stren, defn):
		self.attributes = {
		'level': level,
		'xp': xp,
		'Health': hp,
		'Mana': mana,
		'Strength': stren,
		'Defense': defn,
		}
		self.weapon = ["None", 0]
		self.armor = ["Chest Plate", 6]

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

def env():
	p = Player(1, 100, 50, 20, 6, 0)
	Menu.openMenu(p, SCREEN_W, SCREEN_H)

env()