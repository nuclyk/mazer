from window import Window
from maze import Maze


def main():
    win = Window(1024, 768)
    maze = Maze(10, 10, 15, 15, 50, 50, win)
    maze.break_walls_r(0, 0)
    win.wait_for_close()


if __name__ == "__main__":
    main()
