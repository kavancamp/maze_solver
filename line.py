from point import Point

class Line:
    def __init__(self, start, end):
        self.start = start  # instance of Point
        self.end = end      # instance of Point

    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"