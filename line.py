from point import Point
from tkinter import Canvas

class Line:
    def __init__(self, start, end):
        self.start = start  # instance of Point
        self.end = end      # instance of Point
        
    def draw(self, canvas, fill_color="black"): 
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill=fill_color,
            width=2
        )
    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"
    
