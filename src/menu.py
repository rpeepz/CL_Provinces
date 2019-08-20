SCREEN_W = 30
SCREEN_H = 22

def initBox(w, h):
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
	for i in range (5, h - 4, (int)((h - 7) / len(menuitems))):
		for c in range (len(menuitems[z])):
			itemw = (int)((w - len(menuitems[z])) / 2) + c
			m[i][itemw] = menuitems[z][c]
			m[i + 1][itemw] = '─'
			m[i + 1][itemw + 1] = '─'
			m[i + 1][itemw - 1] = '─'
		z += 1
	return m

def printBox(m):
	for i in range(len(m)):
		line = ''.join(m[i])
		if "Main" in line:
			print(line[0] + "\033[1m\033[36m" + line[1 : -1] + "\033[0m" + line[-0])
		elif "Map" in line:
			print(line[0] + "\033[1m\033[36m" + line[1 : -1] + "\033[0m" + line[-0])
		elif "Back" in line:
			print(line[0] + "\033[1m\033[33m" + line[1 : -1] + "\033[0m" + line[-0])
		elif "Skill" in line:
			print(line[0] + "\033[1m\033[32m" + line[1 : -1] + "\033[0m" + line[-0])
		elif "Equip" in line:
			print(line[0] + "\033[1m\033[35m" + line[1 : -1] + "\033[0m" + line[-0])
		elif "Exit" in line:
			print(line[0] + "\033[1m\033[31m" + line[1 : -1] + "\033[0m" + line[-0])
		else:
			print(line)

Box = initBox(SCREEN_W, SCREEN_H)
printBox(Box)
