from typing import List
from questions.question11 import solution11
from src.tile import Tile
from src.color import Color


class Block:
    def __init__(self, tiles: List[Tile], color: Color):
        self.tiles = tiles
        self.original_tiles = self.tiles
        self.color = color

    def move_to(self, tiles: List[Tile]) -> None:
        self.tiles = tiles

    def get_tiles_from_offset(self, row_offset: int, col_offset: int) -> List[Tile]:
        return [Tile(t.row + row_offset, t.column + col_offset) for t in self.tiles]

    def get_tiles_from_rotation(self) -> List[Tile]:
        min_row = min(iter(tile.row for tile in self.tiles))
        min_col = min(iter(tile.column for tile in self.tiles))
        normalized_tiles = [
            Tile(t.row - min_row, t.column - min_col) for t in self.tiles
        ]
        transposed_tiles = solution11(normalized_tiles)
        block_height = max(iter(tile.row for tile in transposed_tiles))
        vertically_flipped_tiles = [
            Tile(block_height - t.row, t.column) for t in transposed_tiles
        ]
        denormalized_tiles = [
            Tile(t.row + min_row, t.column + min_col) for t in vertically_flipped_tiles
        ]

        return denormalized_tiles

    def reset(self) -> None:
        self.tiles = self.original_tiles
