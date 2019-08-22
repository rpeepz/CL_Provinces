# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Getch.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/21 01:36:27 by patrisor          #+#    #+#              #
#    Updated: 2019/08/21 01:37:51 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys,tty,termios

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally: termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    return k
