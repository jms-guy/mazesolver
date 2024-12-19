from graphics import *
from maze import *
from cells import *


def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win, 1)
    win.wait_for_close()


main()