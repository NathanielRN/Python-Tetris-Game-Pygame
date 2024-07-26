from typing import List
from tile import Tile

# Super complex rotation logic.

"""
This question is hard, so we give you the answer. Ask a teacher if you have more
questions!

This is how we COUNTER-CLOCKWISE rotate a 2D array.

Step 1: The original matrix:

*       
* *     
* * *   
* * * * 
* * * * *

Step 2: Take the transpose (row/column are FLIPPED)

* * * * *
  * * * *
    * * *
      * *
        *

Step 3: Flip the image along the vertical axis:

        *       
      * *     
    * * *   
  * * * * 
* * * * *
"""

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
