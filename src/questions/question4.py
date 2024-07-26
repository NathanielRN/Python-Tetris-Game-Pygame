from typing import List
from grid import Grid
from tile import Tile

# For loops for validity checks


def solution4(tiles: List[Tile], grid: Grid) -> bool:
    for tile in tiles:
        if Grid.is_out_of_bounds(tile.row, tile.column):
            return False

    for tile in tiles:
        if grid.has_block(tile.row, tile.column):
            return False

    return True
