import getch
import screens

def confirmExit(player, w, h):
	ar = 9
	while True:
		m = screens.printConfirm(w, 10, "exit ", ar)
		c = getch.getch()
		if c == 'w' or c == 's':
			ar = screens.updateConfirm(m, c)
		if c == '\r':
			if ar == 7:
				print("save and quit successful")
				exit(-1)
			if ar == 9:
				return