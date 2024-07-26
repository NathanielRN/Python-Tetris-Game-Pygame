from typing import List
from questions.question11 import solution11
from src.tile import Tile
from src.color import Color


class Block:
    def __init__(self, tiles: List[Tile], color: Color):
        self.tiles = tiles
        self.original_tiles = self.tiles
        self.max_height = max(iter(tile.row for tile in tiles)) + 1
        self.half_height = self.max_height // 2
        self.color = color

    def move_to(self, tiles: List[Tile]):
        self.tiles = tiles

    def get_tiles_from_offset(self, row_offset: int, col_offset: int) -> List[Tile]:
        return [Tile(t.row + row_offset, t.column + col_offset) for t in self.tiles]

    def get_tiles_from_rotation(self):
        rotated_tiles = solution11(self.tiles, self.max_height)

        return rotated_tiles

    def reset(self):
        self.tiles = self.original_tiles
