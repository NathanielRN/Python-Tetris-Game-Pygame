from typing import List, Tuple

"""
Objective: Build blocks of different shapes using x,y coordinates.

Using (x,y) coordinates, we can fill it tiles to build blocks.

                    x
           0     1     2     3
    0    (0,0) (1,0) (2,0) (3,0)
y   1    (0,1) (1,1) (2,1) (3,1)
    2    (0,2) (1,2) (2,2) (3,2)
    3    (0,3) (1,3) (2,3) (3,3)
"""

Coordinates = List[Tuple[int, int]]


def solution_jblock() -> Coordinates:
    """
    Write the coordinates for the J block in Tetris.

                        x
               0     1     2     3
        0          (1,0)
    y   1          (1,1)
        2    (0,2) (1,2)
        3
    """
    return [(0, 0), (1, 0), (2, 0), (2, 1)]


def solution_iblock() -> Coordinates:
    """
    Write the coordinates for the I block in Tetris.

                        x
               0     1     2     3
        0    (0,0)
    y   1    (0,1)
        2    (0,2)
        3    (0,3)
    """
    return [(0, 0), (0, 1), (0, 2), (0, 3)]


def solution_oblock() -> Coordinates:
    """
    Write the coordinates for the o block in Tetris.

                        x
               0     1     2     3
        0    (0,0) (1,0)
    y   1    (0,1) (1,1)
        2
        3
    """
    return [(0, 0), (1, 0), (0, 1), (1, 1)]


def solution_sblock() -> Coordinates:
    """
    Write the coordinates for the s block in Tetris.
                    x
               0     1     2     3
        0          (1,0) (2,0)
    y   1    (0,1) (1,1)
        2
        3
    """
    return [(0, 1), (1, 1), (1, 0), (2, 0)]


def solution_tblock() -> Coordinates:
    """
    Write the coordinates for the o block in Tetris.
                    x
               0     1     2     3
        0          (1,0)
    y   1    (0,1) (1,1) (2,1)
        2
        3
    """
    return [(1, 0), (0, 1), (1, 1), (2, 1)]


def solution_zblock() -> Coordinates:
    """
    Write the coordinates for the z block in Tetris.
                    x
               0     1     2     3
        0    (0,0) (1,0)
    y   1          (1,1) (2,1)
        2
        3
    """
    return [(0, 0), (1, 0), (1, 1), (2, 1)]
