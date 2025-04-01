from cell import Cell
from window import Window
from line import Line, Point


def main():
    win = Window(800, 600)
    cell = Cell(100, 100, 150, 150, win)
    cell2 = Cell(150, 100, 200, 150, win)
    cell.has_right_wall = False
    cell2.has_left_wall = False
    cell.draw()
    cell2.draw()
    cell.draw_move(cell2, undo=True)
    win.wait_for_close()


if __name__ == "__main__":
    main()
