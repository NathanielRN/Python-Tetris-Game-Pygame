from typing import List

from tile import Tile

"""
Objective: Get new blocks to drop in the grid.

You are given a list of the "next blocks", so you want to take the first element
AND remove it from the list. `list.pop()` would be very helpful!

e.g.

a = [1, 2, 3]

a.pop()

# a = [1, 2]
"""


def solution10(next_blocks: List[Tile]):
    return next_blocks.pop(0)  # Replace by getting blocks from next_blocks
