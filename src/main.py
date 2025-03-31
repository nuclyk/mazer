from tkinter import Tk, BOTH, Canvas
from line import Line, Point


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Mazer")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)


def main():
    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(500, 50)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
