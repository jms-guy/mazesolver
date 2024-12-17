from graphics import *
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

### Populates maze with cells
    def _create_cells(self):
        self._cells = []
    # Creates cells
        for row in range(self.num_rows):
            column = []
            for c in range(self.num_cols):
                c = Cell(self._win)
                column.append(c)
            self._cells.append(column)
    # Draws the cells 
        for column in range(len(self._cells)):
            for row in range(column):
                self._draw_cell(column, row)

### Draws each cell in the maze
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell._x1 = self._x1 + (i * self._cell_size_x)
        cell._y1 = self._y1 + (j * self._cell_size_y)
        cell._x2 = self._x1 + ((i + 1) * self._cell_size_x)
        cell._y2 = self._y1 + ((j + 1) * self._cell_size_y)

        cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
        self._animate()

### Allows us to visualize the maze creation
    def _animate(self):
        self._win.redraw()
        sleep(0.05)