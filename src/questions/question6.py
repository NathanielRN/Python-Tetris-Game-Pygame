from typing import List
from tile import Tile

# Creating images from coordinate points

"""
### Example

This is how the LBlock looks like:

[
    Tile(0, 0),  # --> Top left tile
    Tile(0, 1),  # --> Top middle tile
    Tile(0, 2),  # --> Top right tile
    Tile(1, 2),  # --> Bottom right tile (the "leg" of the L)
]

We want the Tile list for each of the Tetris blocks below.
"""

# NOTE: You can delete this when its no longer used.
L_Block_Tile_List =  [
                Tile(0, 0),
                Tile(0, 1),
                Tile(0, 2),
                Tile(1, 2),
            ]

def solution_jblock() -> List[Tile]:
    """
    Returns a list of tiles representing the J block in Tetris.
    The J block is shaped like this:
    [ . . X ]
    [ X X X ]
    """
    return L_Block_Tile_List # Replace with Tile representation for J block



def solution_iblock() -> List[Tile]:
    """
    Returns a list of tiles representing the I block in Tetris.
    The I block is shaped like this:
    [ X X X X ]
    """
    return L_Block_Tile_List # Replace with Tile representation for I block


def solution_oblock() -> List[Tile]:
    """
    Returns a list of tiles representing the O block in Tetris.
    The O block is shaped like this:
    [ X X ]
    [ X X ]
    """
    return L_Block_Tile_List # Replace with Tile representation for O block


def solution_sblock() -> List[Tile]:
    """
    Returns a list of tiles representing the S block in Tetris.
    The S block is shaped like this:
    [ . X X ]
    [ X X . ]
    """
    return L_Block_Tile_List


def solution_tblock() -> List[Tile]:
    """
    Returns a list of tiles representing the T block in Tetris.
    The T block is shaped like this:
    [ X X X ]
    [ . X . ]
    """
    return L_Block_Tile_List


def solution_zblock() -> List[Tile]:
    """
    Returns a list of tiles representing the Z block in Tetris.
    The Z block is shaped like this:
    [ X X . ]
    [ . X X ]
    """
    return L_Block_Tile_List
