from typing import List
from tile import Tile

# Super complex rotation logic.


def solution11(input_tiles: List[Tile], max_height: int):
    min_row = min(iter(tile.row for tile in input_tiles))
    min_col = min(iter(tile.column for tile in input_tiles))
    normalized_tiles = [Tile(t.row - min_row, t.column - min_col) for t in input_tiles]
    transposed_tiles = [Tile(t.column, t.row) for t in normalized_tiles]
    rotated_tiles = [Tile(max_height - t.row, t.column) for t in transposed_tiles]
    denormalized_tiles = [
        Tile(t.row + min_row, t.column + min_col) for t in rotated_tiles
    ]
    return denormalized_tiles
