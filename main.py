import numpy as np
import pygame


#main loop
def main():
    rows = 10
    cols = 10

    screen = pygame.display.set_mode((500, 500))  # window size in pixels
    grid = make_grid(rows, cols)
    grid[5,6] = 2
    print(grid)
    running = True
    clock = pygame.time.Clock()
    cell_width, cell_height = draw_grid(screen, grid)
    current_color = 2
    #program loop/quit handle
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = int(mouse_x / cell_width)
                row = int(mouse_y / cell_height)
                grid[row, col] = current_color
        pygame.display.flip()
        clock.tick(60)
        fill_grid(grid, screen)
    pygame.quit()
    quit()

#define grid as np array
def make_grid(rows, width):
    return np.zeros((rows, width))

#make a grid
def draw_grid(screen, grid):
    rows, cols = grid.shape
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width / cols
    cell_height = screen_height / rows
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(
                col * cell_width,
                row * cell_height,
                cell_width,
                cell_height
            )
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
    return(cell_width, cell_height)

def fill_grid(grid, screen):
    rows, cols = grid.shape
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width / cols
    cell_height = screen_height / rows

    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(
                col * cell_width,
                row * cell_height,
                cell_width,
                cell_height
            )

            # fill cell by grid value
            if grid[row, col] == 1:
                color = (255, 255, 255)
            elif grid[row, col] == 2:
                color = (255, 0, 0)  
            elif grid[row, col] == 3:
                color = (0, 0, 255) 
            else:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            pygame.display.update(rect)


if __name__ == '__main__':
    pygame.init()
    main()