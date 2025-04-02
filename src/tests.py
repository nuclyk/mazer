import unittest
from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    # def test_maze_break_entrance_and_exit(self):
    #     num_cols = 5
    #     num_rows = 5
    #     m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
    #     self.assertEqual(m1._cells[0][0].has_top_wall, False)
    #     self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

    def test_reseting_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        m1.break_walls_r(0, 0)
        m1._reset_cells_visited()
        for i in range(len(m1._cells)):
            for cell in m1._cells[i]:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
