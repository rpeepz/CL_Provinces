import getch
SCREEN_W = 30
SCREEN_H = 22
player_level = 4
player_xp = 105
player_hp = 75
player_mana = 50
player_attk = 10
player_def = 0

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
	title = "Skills"
	for c in range(len(title)):
		j = (int)((w - len(title)) / 2) + c
		m[1][j] = title[c]
		m[2][j] = '─'
		m[2][j + 2] = '─'
		m[2][j - 2] = '─'
	xp = "EXP        level  " + str(player_level)
	for c in range(len(xp)):
		j = (int)((w - len(xp)) / 2) + c
		m[3][j] = xp[c]
	for c in range(5, 24):
		if c == 5:
			m[4][c] = '['
		elif c == 23:
			m[4][c] = ']'
		else:
			i = int(((c - 5) / 17) * 100)
			if player_xp >= 100:
				m[4][c] = '▓'
			elif i <= player_xp:
				m[4][c] = '░'
			else:
				m[4][c] = ' '
		if player_xp >= 100:
			upgrade = "upgrades available : " + str(int(player_xp / 100))
			for i in range(len(upgrade)):
				m[5][i + 4] = upgrade[i]
	menuitems = ["",
				"Health  : " + str(player_hp).rjust(4),
				"Mana    : " + str(player_mana).rjust(4),
				"Attack  : " + str(player_attk).rjust(4),
                "Defense : " + str(player_def).rjust(4),
				"Exit Menu"]
	z = 0
	m[ar][5] = '>'
	for i in range (4, h - 1, 3):
		for c in range(len(menuitems[z])):
			itemw = c + 8
			m[i][itemw] = menuitems[z][c]
		z += 1
	return m

def updateBox(m, ar, c):
	for i in range(len(m)):
		if '>' in m[i]:
			if (i == 7 and c == "119") or (i == 19 and c == "115") or (player_xp < 100):
				return ar
			else:
				m[i][5] = ' '
				i = i - 3 if c == "119" else i + 3
				m[i][5] = '>'
				return i

def printConfirm(w, h, skill, ar):
	text = "confirm ?"
	m = [[" "] * (w) for i in range(h + 1)]
	s = int((w/2) - (w/4))
	f = w - int(w/4)
	m[0][s - 1] = '┌'
	m[0][f] = '┐'
	m[h][s - 1] = '└'
	m[h][f] = '┘'
	for i in range(1, h):
		m[i][s - 1] = '│'
		m[i][f] = '│'
	for i in range(s, f):
		m[0][i] = '─'
		m[2][i] = '─'
		m[h][i] = '─'
	for i in range(len(skill)):
		m[1][int((w - len(skill)) / 2) + i] = skill[i]
	for i in range(len(text)):
		m[4][int((w - len(text)) / 2) + i] = text[i]
		m[5][int((w - len(text)) / 2) + i] = '─'
	m[7][s + s] = 'Y'
	m[9][s + s] = 'N'
	m[ar][s + s - 4] = '>'
	for i in range(len(m)):
		line = ''.join(m[i])
		print(line)
	return m

def improve(player, skill):
	ar = 9
	while True:
		m = printConfirm(SCREEN_W, 10, skill, ar)
		c = getch.getch()
		if c == "119" or c == "115":
			for i in range(len(m)):
				if '>' in m[i]:
					if (i == 7 and c == "119") or (i == 9 and c == "115"):
						ar = i
						break
					else:
						m[i][int(SCREEN_W / 3)] = ' '
						i = i - 2 if c == "119" else i + 2
						m[i][int(SCREEN_W / 3)] = '>'
						ar = i
						break
		if c == "13":
			if ar == 9:
				return
			if ar == 7:
				player.xp -= 100
				player.hp += 100
				return

def printBox(m):
	box = "\r"
	for i in range(len(m)):
		line = ''.join(m[i])
		if "Skill" in line:
			box = box + (line[0 : 6] + "\033[1m\033[32m" + line[6 : -1] + "\033[0m" + line[-0] + '\n')
		else:
			box = box + line + '\n'
	print (box, end = '')

def viewSkills(player):
	if player_xp < 100:
		ar = 19
	else:
		ar = 7
	Box = initBox(SCREEN_W, SCREEN_H, ar)
	print("this will be the skill tree menu")
	print('')
	print('')
	print("you can add points earned from levling")
	print("to your attributes and skills")
	print('')
	print('')
	print("here you will also be able to view current exp")
	print("and total of stats such as hp and attack")
	while True:
		printBox(Box)
		c = getch.getch()
		if c == "113":
			exit(-1)
		if c == "119" or c == "115":
			ar = updateBox(Box, ar, c)
		if c == "13":
			if ar == 19:
				return
			if ar == 7:
				improve(player, "Health")
			if ar == 10:
				improve(player, "Mana")
			if ar == 13:
				improve(player, "Attack")
			if ar == 16:
				improve(player, "Defense")