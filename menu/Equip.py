import Getch
import Screens

def mountItems(player, w, h):
    ar = 8
    Box = screens.initEquip(player, w, h, ar)
    while True:
        screens.printMenu(Box)
        c = getch.getch()
        if c == '\r':
            return