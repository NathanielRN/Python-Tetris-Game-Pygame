from typing import List
from tile import Tile

"""
Objective: Take the diagonal flip (transpose) of the tiles to fix the tile
rotation.

This is how we COUNTER-CLOCKWISE rotate a 2D array.

Step 1: The original matrix:

*       
* *     
* * *   
* * * * 
* * * * *

Step 2: Take the transpose by SWITCHING the rows and columns. (You do this one!)

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


def solution11(input_tiles: List[Tile]) -> List[Tile]:
    return [Tile(t.column, t.row) for t in input_tiles]
