from cell import Cell
from line import Line, Point
from window import Window
from maze import Maze


def main():
    win = Window(1024, 768)
    maze = Maze(10, 10, 5, 5, 50, 50, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
