from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.visited = False # ← Track maze traversal
        
    def draw(self):
        if self._win is None:
            return

        def maybe_draw(condition, start, end):
            color = "black" if condition else "white"
            line = Line(start, end)
            self._win.draw_line(line, color)

        # Draw each wall depending on existence
        maybe_draw(self.has_top_wall,    Point(self._x1, self._y1), Point(self._x2, self._y1))
        maybe_draw(self.has_bottom_wall, Point(self._x1, self._y2), Point(self._x2, self._y2))
        maybe_draw(self.has_left_wall,   Point(self._x1, self._y1), Point(self._x1, self._y2))
        maybe_draw(self.has_right_wall,  Point(self._x2, self._y1), Point(self._x2, self._y2))

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        color = "gray" if undo else "red"

        # Compute center points
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(line, color)
