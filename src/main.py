from window import Window
from maze import Maze


def main():
    win = Window(1024, 768)
    maze = Maze(10, 10, 30, 30, 5, 5, win, 19)
    maze.break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
