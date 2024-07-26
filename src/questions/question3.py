import pygame
from pygame import Surface

from block import Block

# Using math to draw


def solution3(
    screen: Surface, block: Block, x_offset: int, y_offset: int, x: int, y: int, cell_size: int, grid_cell_multiplier: float
):
    # Create a rectangle for the block
    tile_rect = pygame.Rect(
        0,  # <-- Calculate the x position of the rectangle by adding x_offset to the block's x position multiplied by cell_size
        0,  # <-- Calculate the y position of the rectangle (similar to the x position)
        100,  # <-- Calculate the width of the rectangle by multiplying cell_size by grid_cell_multiplier
        100,  # <-- Calculate the height of the rectangle
    )
    
    # Draw the rectangle on the screen
    pygame.draw.rect(screen, block.color.value, tile_rect)
