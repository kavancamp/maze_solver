import unittest
from point import Point
from line import Line
from cell import Cell
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
        
class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point(5, 10)
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, 10)

    def test_repr(self):
        p = Point(1, 2)
        self.assertEqual(repr(p), "Point(x=1, y=2)")

        
class DummyWindow:
    def __init__(self):
        self.draw_calls = []

    def draw_line(self, line, fill_color):
        self.draw_calls.append((line, fill_color))

class TestCell(unittest.TestCase):
    def setUp(self):
        self.win = DummyWindow()
        self.cell = Cell(0, 0, 50, 50, self.win)

    def test_defaults(self):
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)

    def test_draw_move(self):
        neighbor = Cell(50, 0, 100, 50, self.win)
        self.cell.draw_move(neighbor)
        self.assertEqual(len(self.win.draw_calls), 1)
        line, color = self.win.draw_calls[0]
        self.assertEqual(color, "red")
        
if __name__== "__main__":
    unittest.main()
    