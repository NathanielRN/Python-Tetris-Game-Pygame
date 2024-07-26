from block import Block
from questions.question6 import (
    solution_iblock,
    solution_jblock,
    solution_oblock,
    solution_sblock,
    solution_tblock,
    solution_zblock,
)
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
            solution_jblock(),
            Color.ORANGE,
        )


class IBlock(Block):
    def __init__(self):
        super().__init__(
            solution_iblock(),
            Color.CYAN,
        )


class OBlock(Block):
    def __init__(self):
        super().__init__(
            solution_oblock(),
            Color.YELLOW,
        )


class SBlock(Block):
    def __init__(self):
        super().__init__(
            solution_sblock(),
            Color.RED,
        )


class TBlock(Block):
    def __init__(self):
        super().__init__(
            solution_tblock(),
            Color.PURPLE,
        )


class ZBlock(Block):
    def __init__(self):
        super().__init__(
            solution_zblock(),
            Color.GREEN,
        )
