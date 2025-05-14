
class Point:
    def __init__(self, x, y):
        self.x = x # horizontal (pixels from the left)
        self.y = y  # vertical (pixels from the top)
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"     
        