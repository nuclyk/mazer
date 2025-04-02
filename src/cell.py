from window import Window
from line import Point, Line


class Cell:
    def __init__(self, id, win=None):
        self.id = id
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.length_x = None
        self.length_y = None
        self.center = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.length_x = self._y2 - self._y1
        self.length_y = self._x2 - self._x1
        self.center = Point(self._x1 + self.length_y / 2, self._y1 + self.length_x / 2)

        line = Line(
            Point(self._x1, self._y1), Point(self._x1, self._y1 + self.length_x)
        )
        if self.has_left_wall:
            self._win.draw_line(line, "black")
            # draw a text with cell id for debugging
            # self._win.canvas.create_text(self.center.x, self.center.y, text=self.id)
        else:
            self._win.draw_line(line, "white")

        line = Line(
            Point(self._x2, self._y2), Point(self._x2, self._y2 - self.length_x)
        )
        if self.has_right_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")

        line = Line(
            Point(self._x1, self._y1), Point(self._x1 + self.length_y, self._y1)
        )
        if self.has_top_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")

        line = Line(
            Point(self._x2, self._y2), Point(self._x2 - self.length_y, self._y2)
        )
        if self.has_bottom_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, "gray" if undo else "red")

    def __repr__(self) -> str:
        return f"[CELL {self.id}]"
