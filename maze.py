from cell import Cell
import time
import random
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x =  cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        
        self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)
            
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit() #breaks top-left and bottom-right walls
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        
    def _create_cells(self): 
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(None) 
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        # Create the cell if it doesn't exist
        if self._cells[i][j] is None:
            x1 = self._x1 + i * self.cell_size_x
            y1 = self._y1 + j * self.cell_size_y
            x2 = x1 + self.cell_size_x
            y2 = y1 + self.cell_size_y
            self._cells[i][j] = Cell(x1, y1, x2, y2, self._win)

        if self._win is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0,0)
        
        exit_cell = self._cells[self.num_cols - 1][self.num_rows -1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        
        while True:
            directions = []
            
            # Check all 4 neighbors and add unvisited ones to directions list
            if i > 0 and not self._cells[i - 1][j].visited:
                directions.append(("left", i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                directions.append(("right", i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                directions.append(("up", i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                directions.append(("down", i, j + 1))
            if not directions:
                # No more unvisited neighbors — backtrack
                self._draw_cell(i, j)
                return    
            # Pick a random direction to move to
            direction, ni, nj = random.choice(directions)
            neighbor = self._cells[ni][nj]

            # Knock down the walls between current and neighbor
            if direction == "left":
                current.has_left_wall = False
                neighbor.has_right_wall = False
            elif direction == "right":
                current.has_right_wall = False
                neighbor.has_left_wall = False
            elif direction == "up":
                current.has_top_wall = False
                neighbor.has_bottom_wall = False
            elif direction == "down":
                current.has_bottom_wall = False
                neighbor.has_top_wall = False

            self._draw_cell(i, j)
            self._draw_cell(ni, nj)

            # Recurse to the neighbor
            self._break_walls_r(ni, nj)
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    
    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        
        # Check if we are at the goal (bottom-right)
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        directions = [
        ("left",  i - 1, j),
        ("right", i + 1, j),
        ("up",    i, j - 1),
        ("down",  i, j + 1)
    ]
        for direction, ni, nj in directions:
            if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
                neighbor = self._cells[ni][nj]
                if not neighbor.visited:
                    # Check for a wall between current and neighbor
                    if direction == "left" and not current.has_left_wall:
                        current.draw_move(neighbor)
                        if self._solve_r(ni, nj):
                            return True
                        current.draw_move(neighbor, undo=True)

                    elif direction == "right" and not current.has_right_wall:
                        current.draw_move(neighbor)
                        if self._solve_r(ni, nj):
                            return True
                        current.draw_move(neighbor, undo=True)

                    elif direction == "up" and not current.has_top_wall:
                        current.draw_move(neighbor)
                        if self._solve_r(ni, nj):
                            return True
                        current.draw_move(neighbor, undo=True)

                    elif direction == "down" and not current.has_bottom_wall:
                        current.draw_move(neighbor)
                        if self._solve_r(ni, nj):
                            return True
                        current.draw_move(neighbor, undo=True)

        return False  # No path worked from this cell