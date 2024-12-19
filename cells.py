from statistics import median
from graphics import *

### Creates graph cells to build the maze with
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

### Draws lines between cells
    def draw_move(self, to_cell, undo=False):
        x_med = median([self._x1, self._x2])
        y_med = median([self._y1, self._y2])
        dest_x_med = median([to_cell._x1, to_cell._x2])
        dest_y_med = median([to_cell._y1, to_cell._y2])

        fill_colour='red'
        if undo:
            fill_colour='gray'       
        self._win.draw_line(Line(Point(x_med, y_med), Point(dest_x_med, dest_y_med)))

### Draws the cells
    def draw(self, x1, y1, x2, y2, fill_colour='white'):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), 'black' if self.has_left_wall else fill_colour)
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), 'black' if self.has_right_wall else fill_colour)
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), 'black' if self.has_top_wall else fill_colour)
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), 'black' if self.has_bottom_wall else fill_colour)
