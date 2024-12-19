from graphics import *
from cells import Cell
from time import sleep
import random

### Creates the maze itself
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

### Breaks the walls in the maze to create paths
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            ## Initializes adjacent cell values
            cells_to_visit = []
            above_cell = None
            beneath_cell = None
            left_cell = None
            right_cell = None

            ## Determines if adjacent cells exist and need to be visited
            if i > 0:
                if self._cells[i - 1][j]:
                    above_cell = self._cells[i - 1][j]
                    if above_cell.visited == False and above_cell not in cells_to_visit:
                        cells_to_visit.append(above_cell)
            if i < (len(self._cells) - 1):
                if self._cells[i + 1][j]:
                    beneath_cell = self._cells[i + 1][j]
                    if beneath_cell.visited == False and beneath_cell not in cells_to_visit:
                        cells_to_visit.append(beneath_cell)
            if j > 0:
                if self._cells[i][j - 1]:
                    left_cell = self._cells[i][j - 1]
                    if left_cell.visited == False and left_cell not in cells_to_visit:
                        cells_to_visit.append(left_cell)
            if j < (len(self._cells[i]) - 1):
                if self._cells[i][j + 1]:
                    right_cell = self._cells[i][j + 1]
                    if right_cell.visited == False and right_cell not in cells_to_visit:
                        cells_to_visit.append(right_cell)
            
            ## If no adjacent cells meet criteria, draw cell and return
            if len(cells_to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            ## Determines direction to recursively follow
            direction = random.randrange(len(cells_to_visit))
            chosen_direction_cell = cells_to_visit[direction]
            if chosen_direction_cell == above_cell:
                current_cell.has_top_wall = False
                chosen_direction_cell.has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i - 1, j)
                self._break_walls_r(i - 1, j)
            if chosen_direction_cell == beneath_cell:
                current_cell.has_bottom_wall = False
                chosen_direction_cell.has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i + 1, j)
                self._break_walls_r(i + 1, j)
            if chosen_direction_cell == left_cell:
                current_cell.has_left_wall = False
                chosen_direction_cell.has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j - 1)
                self._break_walls_r(i, j - 1)
            if chosen_direction_cell == right_cell:
                current_cell.has_right_wall = False
                chosen_direction_cell.has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j + 1)
                self._break_walls_r(i, j + 1)
                

### Breaks walls for entrance and exit to maze
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entrance_cell.has_top_wall = False
        entrance_cell.draw(entrance_cell._x1, entrance_cell._y1, entrance_cell._x2, entrance_cell._y2)
        exit_cell.has_bottom_wall = False
        exit_cell.draw(exit_cell._x1, exit_cell._y1, exit_cell._x2, exit_cell._y2)


### Populates maze with cells
    def _create_cells(self):
        self._cells = []
    # Creates cells
        for column in range(self.num_cols):
            rows = []
            for c in range(self.num_rows):
                c = Cell(self._win)
                rows.append(c)
            self._cells.append(rows)

    # Draws the cells 
        for column in range(self.num_cols):
            for row in range(self.num_rows):
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
        if self._win:
            self._win.redraw()
            sleep(0.05)