from typing import Callable

from grid import NUM_COLUMNS, NUM_ROWS

"""
Objective: Use for loops to generate a grid.
"""


def solution2(draw_grid_cell: Callable[[int, int], None]) -> None:
    for cell_row in range(NUM_ROWS):
        for cell_col in range(NUM_COLUMNS):
            draw_grid_cell(cell_row, cell_col)
