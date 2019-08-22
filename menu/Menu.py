import Getch
import Screens
import Bag
import Skill
import Equip
import Save

def openMenu(p, w, h):
	ar = 5
	Box = screens.initMenu(w, h, ar)
	while True:
		screens.printMenu(Box)
		c = (getch.getch())
		if c == 'p':
			return
		if c == 'w' or c == 's':
			ar = screens.updateMenu(Box, ar, c)
		if c == '\r':
			if ar == 5:
				map.viewMap()
			elif ar == 8:
				bag.viewBag()
			elif ar == 11:
				skill.viewSkills(p, w, h)
			elif ar == 14:
				equip.mountItems(p, w * 2, h)
			elif ar == 17:
				save.confirmExit(p, w, h)
