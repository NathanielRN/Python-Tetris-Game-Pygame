import pygame
from pygame import Surface

from color import Color
from grid import NUM_COLUMNS, NUM_ROWS, Grid

# Interact with for loops to draw the Tetris grid!

def solution2(screen: Surface, g: Grid, cell_size: int, grid_x_start: int, grid_y_start: int):
    # Loop through each row in the grid
    for row_number in range(NUM_ROWS): 
        # Loop through each column in the grid
        for col_number in range(NUM_COLUMNS):
            # Get the color of the current cell
            # For example: g.grid[0][0] will get the color of the (0, 0) grid space
            cell_color = Color.WHITE  # <-- Fill this in following example above
            ### Create a rectangle for the current cell
            # To find the x position: multiply the column number by the cell size and add the starting x position of the grid
            # To find the y position: multiply the row number by the cell size and add the starting y position of the grid
            cell_rect = pygame.Rect(
                0, # <-- x position
                0, # <-- y position
                cell_size - 1,
                cell_size - 1,
            )
            # Draw the rectangle on the screen
            pygame.draw.rect(screen, cell_color.value, cell_rect)
