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
        
class TestMaze(unittest.TestCase):
    
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_small_maze(self):
        m2 = Maze(0, 0, 2, 2, 10, 10)
        self.assertEqual(len(m2._cells), 2)
        self.assertEqual(len(m2._cells[0]), 2)

    def test_non_square_maze(self):
        m3 = Maze(0, 0, 3, 5, 20, 20)
        self.assertEqual(len(m3._cells), 5)
        self.assertEqual(len(m3._cells[0]), 3)
        
    def test_maze_break_entrance_exit(self):
        m = Maze(0, 0, 5, 5, 10, 10)  # 5x5 maze
        entrance = m._cells[0][0]
        exit_cell = m._cells[4][4]

        self.assertFalse(entrance.has_top_wall, "Top-left cell should have no top wall")
        self.assertFalse(exit_cell.has_bottom_wall, "Bottom-right cell should have no bottom wall")
    
        def test_reset_cells_visited(self):
            maze = Maze(0, 0, 5, 5, 10, 10, seed=42)

            # Manually mark every cell visited
            for col in maze._cells:
                for cell in col:
                    cell.visited = True

            # Call the method to reset visited flags
            maze._reset_cells_visited()

            # Check that all cells are now unvisited
            for col in maze._cells:
                for cell in col:
                    self.assertFalse(cell.visited, "Expected cell.visited to be False")
                
if __name__== "__main__":
    unittest.main()
    