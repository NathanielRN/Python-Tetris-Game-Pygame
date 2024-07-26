from block import Block
from src.tile import Tile
from src.color import Color


class LBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(0, 0),
                Tile(0, 1),
                Tile(0, 2),
                Tile(1, 2),
            ],
            Color.WHITE,
        )


class JBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(0, 1),
                Tile(1, 1),
                Tile(2, 1),
                Tile(2, 0),
            ],
            Color.ORANGE,
        )


class IBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(0, 0),
                Tile(0, 1),
                Tile(0, 2),
                Tile(0, 3),
            ],
            Color.CYAN,
        )


class OBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(0, 0),
                Tile(0, 1),
                Tile(1, 0),
                Tile(1, 1),
            ],
            Color.YELLOW,
        )


class SBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(1, 0),
                Tile(1, 1),
                Tile(0, 1),
                Tile(0, 2),
            ],
            Color.RED,
        )


class TBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(1, 0),
                Tile(1, 1),
                Tile(0, 1),
                Tile(0, 2),
            ],
            Color.PURPLE,
        )


class ZBlock(Block):
    def __init__(self):
        super().__init__(
            [
                Tile(0, 0),
                Tile(0, 1),
                Tile(1, 1),
                Tile(1, 2),
            ],
            Color.GREEN,
        )
