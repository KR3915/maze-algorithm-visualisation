import numpy as np
import pygame


#main loop
def main():
    rows = 10
    cols = 10
    screen = pygame.display.set_mode((500, 500))  # window size in pixels
    grid = make_grid(rows, cols)

#define grid as np array
def make_grid(rows, width):
    grid = np.zeros((rows, width))
    print(grid)


if __name__ == '__main__':
    pygame.init()
    main()
    running = True
    #program loop/quit handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False