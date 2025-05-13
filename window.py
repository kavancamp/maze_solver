from tkinter import tk, BOTH, Canvas

class Window:
    def __innit__(self, width, height, title="Maze Solver"):
        self.root = tk.Tk()
        self.width = width
        self.height = height 
        self.root.title = title(title)
        self.is_running = False
        
        canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        canvas.pack(anchor=tk.CENTER, expand=True)
    
    
    def run(self):
        self.root.mainloop()