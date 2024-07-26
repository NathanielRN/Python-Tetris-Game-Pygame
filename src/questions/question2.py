import pygame
from pygame import Surface

from color import Color
from grid import NUM_COLUMNS, NUM_ROWS, Grid

# For loops

def solution2(screen: Surface, g: Grid, cell_size: int, grid_x_start: int, grid_y_start: int):
    for row_i in range(NUM_ROWS):
        for col_i in range(NUM_COLUMNS):
            cell_color: Color = g.grid[row_i][col_i]
            cell_rect = pygame.Rect(
                col_i * cell_size + grid_x_start,
                row_i * cell_size + grid_y_start,
                cell_size - 1,
                cell_size - 1,
            )
            pygame.draw.rect(screen, cell_color.value, cell_rect)
