import getch
import bag
import skill
import equip
import save

SCREEN_W = 30
SCREEN_H = 22

class Player:
	def __init__(self, level, xp, hp, mana, attk, defn):
		self.level = level
		self.xp = xp
		self.hp = hp
		self.mana = mana
		self.attk = attk
		self.defn = defn

def initBox(w, h, ar):
	m = [[" "] * (w) for i in range(h)]
	m[0][0] = '┌'
	m[0][w - 1] = '┐'
	m[h - 1][0] = '└'
	m[h - 1][w - 1] = '┘'
	for i in range(1, w - 1):
		m[0][i] = '─'
		m[h- 1][i] = '─'
	for i in range(1, h - 1):
		m[i][0] = '│'
		m[i][w - 1] = '│'
	title = "Main Menu"
	for c in range(len(title)):
		j = (int)((w - len(title)) / 2) + c
		m[1][j] = title[c]
		m[2][j] = '─'
		m[2][j + 2] = '─'
		m[2][j - 2] = '─'
	menuitems = ["View Map",
				 "Backpack",
				 "Skill",
				 "Equip",
				 "Exit Game"]
	z = 0
	m[ar][5] = '>'
	for i in range (5, h - 4, (int)((h - 7) / len(menuitems))):
		for c in range (len(menuitems[z])):
			itemw = (int)((w - len(menuitems[z])) / 2) + c
			m[i][itemw] = menuitems[z][c]
			m[i + 1][itemw] = '─'
			m[i + 1][itemw + 1] = '─'
			m[i + 1][itemw - 1] = '─'
		z += 1
	return m

def updateBox(m, ar, c):
	for i in range(len(m)):
		if '>' in m[i]:
			if (i == 5 and c == "119") or (i == 17 and c == "115"):
				return ar
			else:
				m[i][5] = ' '
				i = i - 3 if c == "119" else i + 3
				m[i][5] = '>'
				return i

def printBox(m):
	for i in range(len(m)):
		line = ''.join(m[i])
		if "Main" in line:
			print(line[0 : 6] + "\033[1m\033[36m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Map" in line:
			print(line[0 : 6] + "\033[1m\033[36m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Back" in line:
			print(line[0 : 6] + "\033[1m\033[33m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Skill" in line:
			print(line[0 : 6] + "\033[1m\033[32m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Equip" in line:
			print(line[0 : 6] + "\033[1m\033[35m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Exit" in line:
			print(line[0 : 6] + "\033[1m\033[31m" + line[6 : -1] + "\033[0m" + line[-0])
		else:
			print(line)

ar = 5
Box = initBox(SCREEN_W, SCREEN_H, ar)
p = Player(4, 105, 75, 50, 10, 0)
while True:
	printBox(Box)
	c = (getch.getch())
	if c == "113":
		exit(-1)
	if c == "119" or c == "115":
		ar = updateBox(Box, ar, c)
	if c == "13":
		if ar == 5:
			map.viewMap()
		elif ar == 8:
			bag.viewBag()
		elif ar == 11:
			skill.viewSkills(p)
		elif ar == 14:
			equip.mountItems()
		elif ar == 18:
			save.confirm()