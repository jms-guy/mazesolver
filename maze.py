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
        self._reset_cells_visited()

### Solves the maze
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if current_cell == self._cells[-1][-1]:
            return True
        
        ## Left
        if i > 0 and current_cell.has_left_wall == False and not self._cells[i - 1][j].visited:
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i - 1][j], True)
        ## Right
        if i + 1 < self.num_cols and current_cell.has_right_wall == False and not self._cells[i + 1][j].visited:
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i + 1][j], True)
        ## Up
        if j > 0 and current_cell.has_top_wall == False and not self._cells[i][j - 1].visited:
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j-1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j - 1], True)
        ## Down
        if j + 1 < self.num_rows and current_cell.has_bottom_wall == False and not self._cells[i][j + 1].visited:
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j+1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j + 1], True)
        

### Breaks the walls in the maze to create paths
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            cells_to_visit = []

            ## Determines if adjacent cells exist and need to be visited
            if i > 0 and not self._cells[i - 1][j].visited:
                cells_to_visit.append(("left", i-1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                cells_to_visit.append(("right", i+1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                cells_to_visit.append(("above", i, j-1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                cells_to_visit.append(("beneath", i, j+1))
            
            ## If no adjacent cells meet criteria, draw cell and return
            if len(cells_to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            ## Determines direction to recursively follow
            direction = random.randrange(len(cells_to_visit))
            chosen = cells_to_visit[direction]
            if chosen[0] == "left":
                current_cell.has_left_wall = False
                self._cells[chosen[1]][chosen[2]].has_right_wall = False

            if chosen[0] == "right":
                current_cell.has_right_wall = False
                self._cells[chosen[1]][chosen[2]].has_left_wall = False

            if chosen[0] == "above":
                current_cell.has_top_wall = False
                self._cells[chosen[1]][chosen[2]].has_bottom_wall = False

            if chosen[0] == "beneath":
                current_cell.has_bottom_wall = False
                self._cells[chosen[1]][chosen[2]].has_top_wall = False

            self._break_walls_r(chosen[1], chosen[2])
                
### Resets cell.visited property for maze traversal
    def _reset_cells_visited(self):
        for i in self._cells:
            for cells in i:
                cells.visited = False


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