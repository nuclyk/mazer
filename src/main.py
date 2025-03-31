from cell import Cell
from window import Window
from line import Line, Point


def main():
    win = Window(800, 600)
    cell = Cell(100, 100, 150, 150, win)
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
