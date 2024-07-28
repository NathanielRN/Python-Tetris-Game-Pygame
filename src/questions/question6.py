from typing import List
from color import Color

"""
Objective: Stop blocks from passing through already filled cells.
"""


def solution6(grid: List[List[int]], row: int, column: int, empty_cell: Color) -> bool:
    return grid[row][column] != empty_cell
