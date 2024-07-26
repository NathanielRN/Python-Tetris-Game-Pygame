from typing import List
from tile import Tile

# Creating images from coordinate points


def solution_jblock() -> List[Tile]:
    return [
        Tile(0, 1),
        Tile(1, 1),
        Tile(2, 1),
        Tile(2, 0),
    ]


def solution_iblock() -> List[Tile]:
    return [
        Tile(0, 0),
        Tile(0, 1),
        Tile(0, 2),
        Tile(0, 3),
    ]


def solution_oblock() -> List[Tile]:
    return [
        Tile(0, 0),
        Tile(0, 1),
        Tile(1, 0),
        Tile(1, 1),
    ]


def solution_sblock() -> List[Tile]:
    return [
        Tile(1, 0),
        Tile(1, 1),
        Tile(0, 1),
        Tile(0, 2),
    ]


def solution_tblock() -> List[Tile]:
    return [
        Tile(1, 0),
        Tile(1, 1),
        Tile(0, 1),
        Tile(0, 2),
    ]


def solution_zblock() -> List[Tile]:
    return [
        Tile(0, 0),
        Tile(0, 1),
        Tile(1, 1),
        Tile(1, 2),
    ]
