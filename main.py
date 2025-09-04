import numpy as np
import pygame
import subprocess
from collections import deque
#import maze
TOOLBAR_HEIGHT = 50

def main():
# === Variables ===
    rows = 100
    cols = 100
    current_color = 2
    width = 1000
    height = 1000
    prev_start = None
    prev_goal = None



# === init ===
    screen = pygame.display.set_mode((width, height + TOOLBAR_HEIGHT))  # přidáme toolbar výšku
    grid = make_grid(rows, cols)
    grid_prev = grid
    print(grid)
    running = True
    clock = pygame.time.Clock()
# ===== Main Loop =====
    while running:
        grid_prev = grid.copy()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ==== Mouse Clicking ====

            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_x, mouse_y = event.pos
                if mouse_y < TOOLBAR_HEIGHT:
                    #White brush
                    if 10 < mouse_x < 50:
                        current_color = 1
                    #Red Brush
                    elif 70 < mouse_x < 110:
                        current_color = 2
                    #Blue Brush
                    elif 130 < mouse_x < 170:
                        current_color = 3
                    #Eraser
                    elif 190 < mouse_x < 230:
                        current_color = 0
                    #Clear
                    elif 250 < mouse_x < 290: 
                        grid = np.zeros((rows, cols))
                    #info button
                    elif 310 < mouse_x < 350:
                        subprocess.Popen(["python", "info.py"])
                else:
                    # Kliknutí v gridu - posuneme y o TOOLBAR_HEIGHT
                    col = int(mouse_x / (width / cols))
                    row = int((mouse_y - TOOLBAR_HEIGHT) / (height / rows))
                    if 0 <= row < rows and 0 <= col < cols:
                        if current_color == 2 and 2 in grid:
                            grid[grid == 2] = 0
                        elif current_color == 3 and 3 in grid:
                            grid[grid == 3] = 0                        
                        grid[row, col] = current_color
            start_pos = np.where(grid == 2)
            goal_pos = np.where(grid == 3)
            #==== pathing ===
            if len(start_pos[0]) > 0 and len(goal_pos[0]) > 0:
                start = (start_pos[0][0], start_pos[1][0])
                goal = (goal_pos[0][0], goal_pos[1][0])

                if grid_changed(grid,grid_prev):
                    grid[grid == 4] = 0
                    prev_start = start
                    prev_goal = goal

                path = bfs_path(grid, start, goal)
                draw_path(screen, path, grid)
            else:
                grid[grid == 4] = 0
                prev_start = None
                prev_goal = None
                path = []


        #==== Drawing UI ====
        draw_toolbar(screen, current_color)
        fill_cells(grid, screen)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    quit()

#Randomize
def randomize(matrix):
    return maze.randomize(matrix)
#checks if grid has been changed
def grid_changed(grid, grid_prev):
    if np.array_equal(grid, grid_prev):
        return False
    return True

#drawing path into the grid
def draw_path(screen, path, grid):
    if len(path) <= 2:
        return
    inner_path = path[1:-1]
    for r, c in inner_path:
        grid[r, c] = 4 # zelená

#Making grind consisting of 0s
def make_grid(rows, cols):
    return np.zeros((rows, cols))

#draws grid
def draw_grid(screen, grid):
    rows, cols = grid.shape
    screen_width, screen_height = screen.get_size()
    usable_height = screen_height - TOOLBAR_HEIGHT  # odečteme toolbar
    cell_width = screen_width / cols
    cell_height = usable_height / rows
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(
                col * cell_width,
                row * cell_height + TOOLBAR_HEIGHT,  # posun dolů o toolbar
                cell_width,
                cell_height
            )
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
    return cell_width, cell_height

#updates colors depending on np array
def fill_cells(grid, screen):
    rows, cols = grid.shape
    screen_width, screen_height = screen.get_size()
    usable_height = screen_height - TOOLBAR_HEIGHT  # odečteme toolbar
    cell_width = screen_width / cols
    cell_height = usable_height / rows

    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(
                col * cell_width,
                row * cell_height + TOOLBAR_HEIGHT,  # posun dolů
                cell_width,
                cell_height
            )

            if grid[row, col] == 1:
                color = (255, 255, 255) #obstacle
            elif grid[row, col] == 2:
                color = (255, 0, 0) #start
            elif grid[row, col] == 3:
                color = (0, 0, 255) #end
            elif grid[row, col] == 4:
                color = (0, 255, 0) #path
            else:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            pygame.display.update(rect)

#draws toolbar
def draw_toolbar(screen, current_color):
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, screen.get_width(), TOOLBAR_HEIGHT))
    
    colors = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]  # jen barvy
    x_positions = [10, 70, 130]
    
    # buttons render
    for i, color in enumerate(colors):
        rect = pygame.Rect(x_positions[i], 10, 40, 30)
        pygame.draw.rect(screen, color, rect)
        if current_color == i + 1:
            pygame.draw.rect(screen, (255, 255, 0), rect, 3)
    
    # ====== buttons =======
    #NOTE: pygame.Rect(X,Y,Z,A) X is allways bigger by 60
    # --- eraser button ---
    eraser_rect = pygame.Rect(190, 10, 40, 30)
    pygame.draw.rect(screen, (200, 200, 200), eraser_rect) 
    
        # --- clear button ---
    clear_rect = pygame.Rect(250, 10, 40, 30)
    pygame.draw.rect(screen, (200, 200, 200), clear_rect)

    # --- Guide Button ---
    guide_rect = pygame.Rect(310, 10, 40, 30)
    pygame.draw.rect(screen, (200, 200, 200), guide_rect)

    # icon of eraser
    font = pygame.font.Font(None, 24)
    text = font.render("E", True, (0, 0, 0))
    text_pos = text.get_rect(center=eraser_rect.center)
    screen.blit(text, text_pos)

    #icon of clear
    font = pygame.font.Font(None, 24)
    text = font.render("C", True, (0, 0, 0))
    text_pos = text.get_rect(center=clear_rect.center)
    screen.blit(text, text_pos)

    #icon of guide
    font = pygame.font.Font(None, 20)
    text = font.render("guide", True, (0, 0, 0))
    text_pos = text.get_rect(center=guide_rect.center)
    screen.blit(text, text_pos)
    
    # highlight of selected button
    if current_color == 0:
        pygame.draw.rect(screen, (255, 255, 0), eraser_rect, 3)

#bfs pathing
def bfs_path(maze: np.ndarray, start: tuple, goal: tuple):
    start = tuple(map(int, np.ravel(start)))
    goal = tuple(map(int, np.ravel(goal)))

    rows, cols = maze.shape
    visited = np.zeros_like(maze, dtype=bool)
    parent = {}
    
    queue = deque([start])
    visited[start] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        
        if (r, c) == goal:
            path = []
            curr = goal
            while curr != start:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            path.reverse()
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols or 4 <= nr < rows and 4 <= nc < cols:
                if not visited[nr, nc] and (maze[nr, nc] == 0 or (nr, nc) == goal) or not visited[nr, nc] and (maze[nr, nc] == 4 or (nr, nc) == goal):
                    visited[nr, nc] = True
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))
    
    return [] 


if __name__ == '__main__':
    pygame.init()
    main()
