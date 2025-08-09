import numpy as np
import pygame

TOOLBAR_HEIGHT = 50

def main():
    rows = 10
    cols = 10
    current_color = 2
    width = 500
    height = 500

    screen = pygame.display.set_mode((width, height + TOOLBAR_HEIGHT))  # přidáme toolbar výšku
    grid = make_grid(rows, cols)
    print(grid)
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if mouse_y < TOOLBAR_HEIGHT:
                    # mouse click on the toolbar icon changes current color variable
                    if 10 < mouse_x < 50:
                        current_color = 1
                    elif 70 < mouse_x < 110:
                        current_color = 2
                    elif 130 < mouse_x < 170:
                        current_color = 3
                    elif 190 < mouse_x < 230:  # guma
                        current_color = 0
                    elif 250 < mouse_x < 290:  # guma
                        grid = np.zeros((rows, cols))
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

        
        draw_toolbar(screen, current_color)
        fill_grid(grid, screen)
        draw_grid(screen, grid)

        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    quit()

def make_grid(rows, cols):
    return np.zeros((rows, cols))

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

def fill_grid(grid, screen):
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

def draw_toolbar(screen, current_color):
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, screen.get_width(), TOOLBAR_HEIGHT))
    
    colors = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]  # jen barvy
    x_positions = [10, 70, 130]
    
    # vykreslení barevných tlačítek
    for i, color in enumerate(colors):
        rect = pygame.Rect(x_positions[i], 10, 40, 30)
        pygame.draw.rect(screen, color, rect)
        if current_color == i + 1:
            pygame.draw.rect(screen, (255, 255, 0), rect, 3)
    ###################
    ######buttons######
    ###################
    #NOTE: pygame.Rect(X,Y,Z,A) X is allways bigger by 60
    # --- eraser button ---
    eraser_rect = pygame.Rect(190, 10, 40, 30)
    pygame.draw.rect(screen, (200, 200, 200), eraser_rect) 
    
        # --- clear button ---
    clear_rect = pygame.Rect(250, 10, 40, 30)
    pygame.draw.rect(screen, (200, 200, 200), clear_rect)

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

    # zvýraznění gumy, pokud je vybraná (current_color == 0)
    if current_color == 0:
        pygame.draw.rect(screen, (255, 255, 0), eraser_rect, 3)
if __name__ == '__main__':
    pygame.init()
    main()
