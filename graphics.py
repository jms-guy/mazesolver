from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            self.win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, background='gray75')
        self.canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
        print('Window closed...')

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_colour='black'):
        line.draw(self.canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2)