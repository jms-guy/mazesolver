from graphics import *


def main():
    win = Window(800, 600)
    example = Cell(Point(300, 300), Point(500, 500))
    example.draw(win)
    example2 = Cell(Point(50, 50), Point(75, 100))
    example2.has_right_wall = False
    example2.has_top_wall = False
    example2.draw(win)
    win.wait_for_close()


main()