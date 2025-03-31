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

    def draw(self):
        length_vertical = self._y2 - self._y1
        length_horizontal = self._x2 - self._x1

        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y1 + length_vertical)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_right_wall:
            p1 = Point(self._x2, self._y2)
            p2 = Point(self._x2, self._y2 - length_vertical)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1 + length_horizontal, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            p1 = Point(self._x2, self._y2)
            p2 = Point(self._x2 - length_horizontal, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
