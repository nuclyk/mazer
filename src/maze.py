from cell import Cell
import random
import time


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def break_walls_r(self, i, j):
        current: Cell = self._cells[i][j]
        current.visited = True

        while True:
            to_visit = []
            position = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            if i - 1 >= 0:
                # print(position[0][0], position[0][1])
                cell = self._cells[position[0][0]][position[0][1]]
                if not cell.visited:
                    to_visit.append((position[0][0], position[0][1]))

            if j - 1 >= 0:
                # print(position[1][0], position[1][1])
                cell = self._cells[position[1][0]][position[1][1]]
                if not cell.visited:
                    to_visit.append((position[1][0], position[1][1]))

            if j + 1 < len(self._cells):
                # print(position[2][0], position[2][1])
                cell = self._cells[position[2][0]][position[2][1]]
                if not cell.visited:
                    to_visit.append((position[2][0], position[2][1]))

            if i + 1 < len(self._cells[i]):
                # print(position[3][0], position[3][1])
                cell = self._cells[position[3][0]][position[3][1]]
                if not cell.visited:
                    to_visit.append((position[3][0], position[3][1]))

            # for item in to_visit:
            # print(item)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                print("end")
                return
            else:
                random_number = random.randrange(0, len(to_visit))
                direction = to_visit[random_number]
                column, row = direction
                print(f"direction: {direction}")
                next_cell = self._cells[column][row]

                if column < i and row == j:
                    current.has_left_wall = False
                    next_cell.has_right_wall = False
                elif column == i and row < j:
                    current.has_top_wall = False
                    next_cell.has_bottom_wall = False
                elif column == i and row > j:
                    current.has_bottom_wall = False
                    next_cell.has_top_wall = False
                elif column > i and row == j:
                    current.has_right_wall = False
                    next_cell.has_left_wall = False

                self.break_walls_r(column, row)

        # [i-1, j], [i, j-1], [i, j+1], [i+1, j]
        #

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
