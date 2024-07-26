from typing import List

from blocks import LBlock
from tile import Tile

# Instead of getting the same block every time, get new blocks.
"""
HINT: In Python, list.pop() removes and returns the last item from a list. For example, if you have a list ['a', 'b', 'c'] and you call pop(), it will remove 'c' and give it back to you. If you want to remove an item at a specific position, you can pass an index to pop(), like pop(0) to remove the first item.
"""
def solution9(next_blocks: List[Tile]):
    return LBlock() # Replace by getting blocks from next_blocks
