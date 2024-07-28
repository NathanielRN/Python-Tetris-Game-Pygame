from block import Block
from questions.question7 import (
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
                Tile(*coord)
                for coord in [
                    (0, 0),
                    (0, 1),
                    (0, 2),
                    (1, 2),
                ]
            ],
            Color.LIGHT_BLUE,
        )


class JBlock(Block):
    def __init__(self):
        super().__init__(
            [Tile(*coord) for coord in solution_jblock()],
            Color.ORANGE,
        )


class IBlock(Block):
    def __init__(self):
        super().__init__(
            [Tile(*coord) for coord in solution_iblock()],
            Color.CYAN,
        )


class OBlock(Block):
    def __init__(self):
        super().__init__(
            [Tile(*coord) for coord in solution_oblock()],
            Color.YELLOW,
        )


class SBlock(Block):
    def __init__(self):
        super().__init__(
            [Tile(*coord) for coord in solution_sblock()],
            Color.RED,
        )


class TBlock(Block):
    def __init__(self):
        super().__init__(
            [Tile(*coord) for coord in solution_tblock()],
            Color.PURPLE,
        )


class ZBlock(Block):
    def __init__(self):
        super().__init__(
            [Tile(*coord) for coord in solution_zblock()],
            Color.GREEN,
        )
