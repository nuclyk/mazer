from window import Window
from line import Point, Line


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window) -> None:
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.length_vertical = self._y2 - self._y1
        self.length_horizontal = self._x2 - self._x1
        self.center = Point(
            self._x1 + self.length_horizontal / 2, self._y1 + self.length_vertical / 2
        )

    def draw(self):
        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y1 + self.length_vertical)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_right_wall:
            p1 = Point(self._x2, self._y2)
            p2 = Point(self._x2, self._y2 - self.length_vertical)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1 + self.length_horizontal, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            p1 = Point(self._x2, self._y2)
            p2 = Point(self._x2 - self.length_horizontal, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False) -> None:
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, "gray" if undo else "red")
