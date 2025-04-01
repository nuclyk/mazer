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
        self.center_screen(width, height)

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

    def center_screen(self, window_width, window_height):
        """gets the coordinates of the center of the screen"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(
            "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
        )
