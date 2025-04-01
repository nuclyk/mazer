from cell import Cell
from line import Line, Point
from window import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(100, 100, 3, 4, 50, 50, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
