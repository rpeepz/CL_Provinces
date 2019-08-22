import sys,tty,termios
class _Getch:       
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def getch():
    inkey = _Getch()
    while(1):
            k=inkey()
            if k!='':break
    if str(ord(k)) == "27": exit(-1)
    return str(ord(k))