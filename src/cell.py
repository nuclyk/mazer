from window import Window
from line import Point, Line


class Cell:
    def __init__(self, id, win):
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
        self._win: Window = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.length_x = self._y2 - self._y1
        self.length_y = self._x2 - self._x1
        self.center = Point(self._x1 + self.length_y / 2, self._y1 + self.length_x / 2)

        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y1 + self.length_x)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
            self._win.canvas.create_text(self.center.x, self.center.y, text=self.id)

        if self.has_right_wall:
            p1 = Point(self._x2, self._y2)
            p2 = Point(self._x2, self._y2 - self.length_x)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1 + self.length_y, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            p1 = Point(self._x2, self._y2)
            p2 = Point(self._x2 - self.length_y, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, "gray" if undo else "red")

    def __repr__(self) -> str:
        return f"[CELL {self.id}]"
