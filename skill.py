import getch
import screens

def improve(m, player, skill):
	ar = 9
	while True:
		m = screens.printConfirm(len(m[0]), 10, skill, ar)
		c = getch.getch()
		if c == "119" or c == "115":
			ar = screens.updateConfirm(m, c)
		if c == "13":
			if ar == 9:
				return
			if ar == 7:
				player.increase(player, skill)
				ar = screens.updateSkill(m, ar, c, player)
				return

def viewSkills(player, w, h):
	ar = 19 if player.attributes['xp'] < 100 else 7
	while True:
		Box = screens.initSkills(w, h, ar, player)
		screens.printSkills(Box)
		c = getch.getch()
		if c == "119" or c == "115":
			ar = screens.updateSkill(Box, ar, c, player)
		if c == "13":
			if ar == 19:
				return
			if ar == 7:
				improve(Box, player, "Health")
			if ar == 10:
				improve(Box, player, "Mana")
			if ar == 13:
				improve(Box, player, "Strength")
			if ar == 16:
				improve(Box, player, "Defense")
			ar = 19 if player.attributes['xp'] < 100 else 7
