from typing import List

from tile import Tile

# Instead of getting the same block every time, get new blocks.


def solution9(next_blocks: List[Tile]):
    return next_blocks.pop(0)
