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
    #program loop/quit handle
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(60)
        fill_grid(grid, screen)
    pygame.quit()



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