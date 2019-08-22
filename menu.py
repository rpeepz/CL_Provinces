import getch
import screens
import bag
import skill
import equip
import save

def openMenu(p, w, h):
	ar = 5
	Box = screens.initMenu(w, h, ar)
	while True:
		screens.printMenu(Box)
		c = (getch.getch())
		if c == "112":
			return
		if c == "119" or c == "115":
			ar = screens.updateMenu(Box, ar, c)
		if c == "13":
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
