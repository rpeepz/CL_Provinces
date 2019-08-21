import getch
from skill import printConfirm
SCREEN_W = 30
SCREEN_H = 22

def confirmExit():
	ar = 9
	while True:
		m = printConfirm(SCREEN_W, 10, "exit ", ar)
		c = getch.getch()
		if c == "119" or c == "115":
			for i in range(len(m)):
				if '>' in m[i]:
					if (i == 7 and c == "119") or (i == 9 and c == "115"):
						ar = i
					else:
						m[i][int(SCREEN_W / 3)] = ' '
						i = i - 2 if c == "119" else i + 2
						m[i][int(SCREEN_W / 3)] = '>'
						ar = i
						break
		if c == "13":
			if ar == 7:
				exit(-1)
			if ar == 9:
				return