import pygame
from pygame import Surface

from block import Block

# Using math to draw


def solution3(
    screen: Surface, block: Block, x_offset: int, y_offset: int, x: int, y: int, cell_size: int, grid_cell_multiplier: float
):
    tile_rect = pygame.Rect(
        x_offset + x * cell_size,
        y_offset + y * cell_size,
        cell_size * grid_cell_multiplier,
        cell_size * grid_cell_multiplier,
    )
    pygame.draw.rect(screen, block.color.value, tile_rect)
