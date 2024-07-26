from typing import List
from grid import Grid
from tile import Tile

# Check if the proposed new block tiles positions are valid.


def solution4(tiles: List[Tile], grid: Grid) -> bool:
    for tile in tiles:
        if True: # <-- Use Grid static method to determine if tile is out of bounds
            return False

    for tile in tiles:
        if True: # <-- Use grid instance method to determine if tile is out of bounds
            return False

    return True
