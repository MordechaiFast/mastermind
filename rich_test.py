import sys, tty, termios
import rich

def getchar():
    '''Returns a sinlge character from stdin as it is pressed,
    without waiting for a newline.'''
    fd = sys.stdin.fileno()
    attr = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, attr)

rich.print('enter a color code:')
color = int(getchar())
if color == 1:
    rich.print('[red]:dot:')
