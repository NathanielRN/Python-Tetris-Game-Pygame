import copy
from typing import List
from grid import Grid
from blocks import *
import random
import pygame

from questions.question10 import solution10
from questions.question4 import solution4
from questions.question9 import solution9


NUM_OF_NEXT_BLOCKS = 3
BLOCKS = [
    IBlock(),
    JBlock(),
    LBlock(),
    OBlock(),
    SBlock(),
    TBlock(),
    ZBlock(),
]


def get_random_block() -> Block:
    return copy.deepcopy(random.choice(BLOCKS))


class GameState:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.reset()

        self.clear_sound = pygame.mixer.Sound("src/Sounds/clear.ogg")

    def reset(self) -> None:
        self.grid.reset()
        self.set_current_block(get_random_block())
        self.game_over = False
        self.next_blocks = [get_random_block() for _ in range(NUM_OF_NEXT_BLOCKS)]
        self.score = 0
        self.held_block = None

    def update_score_for_moving_down(self) -> None:
        self.score += solution10()

    def update_score_for_lines_cleared(self, lines_cleared: int) -> None:
        self.score += lines_cleared * 100

    def is_valid_tiles(self, tiles: List[Tile]) -> bool:
        return solution4(tiles, self.grid)

    def move_current_block(self, row_offset: int, col_offset: int) -> bool:
        ncp = self.current_block.get_tiles_from_offset(row_offset, col_offset)
        if self.is_valid_tiles(ncp):
            self.current_block.move_to(ncp)
            return True

        return False

    def move_left(self) -> None:
        _ = self.move_current_block(0, -1)

    def move_right(self) -> None:
        _ = self.move_current_block(0, 1)

    def move_down(self) -> bool:
        did_move = self.move_current_block(1, 0)

        if not did_move:
            self.lock_current_block()
        else:
            self.update_score_for_moving_down()

        return did_move

    def rotate(self) -> None:
        tiles = self.current_block.get_tiles_from_rotation()
        if self.is_valid_tiles(tiles):
            self.current_block.move_to(tiles)

    def hold(self) -> None:
        tmp = self.held_block
        self.held_block = self.current_block
        self.held_block.reset()
        if tmp:
            self.swap_current_block(tmp)
        else:
            self.set_current_block(self.next_blocks.pop(0))
            self.next_blocks.append(get_random_block())

    def swap_current_block(self, new_current: Block) -> None:
        self.set_current_block(new_current)

        if not self.is_valid_tiles(self.current_block.tiles):
            self.game_over = True

    def set_current_block(self, new_block: Block) -> None:
        self.current_block = new_block
        self.current_block.reset()
        self.current_block.move_to(self.current_block.get_tiles_from_offset(0, 4))

    def lock_current_block(self) -> None:
        next_block = solution9(self.next_blocks)
        for tile in self.current_block.tiles:
            row, column = tile.row, tile.column
            self.grid.grid[row][column] = self.current_block.color
        self.swap_current_block(next_block)
        if self.game_over:
            return

        self.next_blocks.append(get_random_block())

        rows_cleared = self.grid.clear_full_rows()

        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score_for_lines_cleared(rows_cleared)
