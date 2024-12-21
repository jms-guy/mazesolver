import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 65
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        entrance = m1._cells[0][0]
        exit_cell = m1._cells[-1][-1]
        self.assertFalse(entrance.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)



if __name__ == "__main__":
    unittest.main()