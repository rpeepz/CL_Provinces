import getch
import screens

def confirmExit(player, w, h):
	ar = 9
	while True:
		m = screens.printConfirm(w, 10, "exit ", ar)
		c = getch.getch()
		if c == "119" or c == "115":
			ar = screens.updateConfirm(m, c)
		if c == "13":
			if ar == 7:
				print("save and quit successful")
				exit(-1)
			if ar == 9:
				return