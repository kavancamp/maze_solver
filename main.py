from window import Window
from maze import Maze

def main():
    print("Welcome to Maze Solver!")

if __name__ == "__main__":
    win = Window(500, 500)
    
    # # Create a cell and draw it
    # cell1 = Cell(150, 100, 200, 150, win)
    # cell1.draw()

    # # Create another cell with some walls removed
    # cell2 = Cell(160, 100, 210, 150, app)
    # cell2.has_left_wall = False
    # cell2.has_bottom_wall = False
    # cell2.draw()

    # # Another one with only the top wall
    # cell3 = Cell(220, 100, 270, 150, app)
    # cell3.has_bottom_wall = False
    # cell3.has_left_wall = False
    # cell3.has_right_wall = False
    # cell3.draw()
    
    # cell1.draw_move(cell2)       # forward (red)
    # cell2.draw_move(cell3)       # forward (red)
    # cell3.draw_move(cell2, True) # backtrack (gray)
    maze = Maze(50, 50, 10, 10, 40, 40, win=win) #seed=0) #instantiate the Maze:
    solved = maze.solve()
    print("Maze Solved", solved)
    win.wait_for_close()

    main()  