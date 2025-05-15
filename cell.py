from line import Line
from point import Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win=None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self):
        if self._win is None:
            return
        # Draw top wall
        if self.has_top_wall:
            top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top)

        # Draw bottom wall
        if self.has_bottom_wall:
            bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom)

        # Draw left wall
        if self.has_left_wall:
            left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left)

        # Draw right wall
        if self.has_right_wall:
            right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right)
            
    def draw_move(self, to_cell, undo=False):
        #change color to show backtracking
        fill_color = "gray" if undo else "red" 

        # Calculate centers of current cell and destination cell
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1
        
        # Create a line from this cell's center to the other
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
                