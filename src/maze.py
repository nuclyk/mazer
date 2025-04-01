from cell import Cell
from window import Window
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for column in range(self._num_cols):
            self._cells.append([])
            for row in range(self._num_rows):
                cell = Cell(f"{column}{row}", self._win)
                self._cells[column].append(cell)

        self._break_entrance_and_exit()

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        top_left_x = self._x1 + (i * self._cell_size_x)
        top_left_y = self._y1 + (j * self._cell_size_y)
        self._cells[i][j].draw(
            top_left_x,
            top_left_y,
            top_left_x + self._cell_size_x,
            top_left_y + self._cell_size_y,
        )
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if self._win is None:
            return
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._win.redraw()
