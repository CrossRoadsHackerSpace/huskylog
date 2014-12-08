import curses
import time

screen = curses.initscr()
dims = screen.getmaxyx()

screen.addstr(int(dims[0]/2), int(dims[1]/2-6), "Hello World")
screen.refresh()
screen.getch()

curses.endwin()
