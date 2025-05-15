import tkinter as tk
from tkinter import Tk, BOTH, Canvas
import time
from point import Point
from line import Line

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close) 
        self.canvas = Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack(fill=BOTH, expand=1)
        
        self.setup_ui()
        
    def setup_ui(self):
        
        label = tk.Label(self.root, text="Hello, Tkinter!")
        label.pack(pady=10)

        button = tk.Button(self.root, text="Close Program", command=self.close)
        button.pack()
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    
    def wait_for_close(self):
        self.is_running = True   
        while self.is_running:
            self.redraw()
            time.sleep(0.01)
            
    def run(self):
        self.root.mainloop()
        
    def close(self):
        self.is_running = False
        #self.root.destroy() 
        
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)    