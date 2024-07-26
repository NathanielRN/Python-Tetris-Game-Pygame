import pygame

from grid import Grid
from questions.question2 import solution2
from questions.question3 import solution3
from src.block import Block
from src.color import Color
from src.game_state import NUM_OF_NEXT_BLOCKS, GameState

CELL_SIZE = 30

TOP_HEADER_HEIGHT = 200
MAIN_CONTENT_HEIGHT = 620
HEIGHT = TOP_HEADER_HEIGHT + MAIN_CONTENT_HEIGHT

LEFT_COLUMN_WIDTH = 170
MAIN_CONTENT_WIDTH = 320
RIGHT_COLUMN_WIDTH = 170
WIDTH = LEFT_COLUMN_WIDTH + MAIN_CONTENT_WIDTH + RIGHT_COLUMN_WIDTH

RIGHT_COLUMN_START = WIDTH - RIGHT_COLUMN_WIDTH

LEFT_COLUMN_START = 8

GRID_X_START = LEFT_COLUMN_WIDTH + 15
GRID_Y_START = TOP_HEADER_HEIGHT

NEXT_BOX_HEIGHT = 180

GRID_CELL_MULTIPLIER = 0.9


class Drawer(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")

        if it is not None:
            return it

        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass

    def setup(self):

        self.game_font = pygame.font.Font(None, 40)
        self.score_title = self.game_font.render("Score", True, Color.WHITE.value)
        self.next_title = self.game_font.render("Next", True, Color.WHITE.value)
        self.hold_title = self.game_font.render("Hold", True, Color.WHITE.value)
        self.game_title = self.game_font.render(
            "Coding Camp 2024!", True, Color.WHITE.value
        )

        self.score_rect = pygame.Rect(
            RIGHT_COLUMN_START, TOP_HEADER_HEIGHT + 55, RIGHT_COLUMN_WIDTH, 60
        )
        self.next_rect = pygame.Rect(
            RIGHT_COLUMN_START,
            TOP_HEADER_HEIGHT + 215,
            RIGHT_COLUMN_WIDTH,
            NEXT_BOX_HEIGHT * NUM_OF_NEXT_BLOCKS - 200,
        )
        self.hold_rect = pygame.Rect(
            LEFT_COLUMN_START,
            TOP_HEADER_HEIGHT + 215,
            LEFT_COLUMN_WIDTH,
            NEXT_BOX_HEIGHT,
        )

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def draw_base_elements(self):
        self.screen.fill(Color.DARK_BLUE.value)
        self.screen.blit(
            self.score_title, (RIGHT_COLUMN_START, TOP_HEADER_HEIGHT + 20, 50, 50)
        )
        self.screen.blit(
            self.next_title, (RIGHT_COLUMN_START, TOP_HEADER_HEIGHT + 180, 50, 50)
        )
        self.screen.blit(
            self.hold_title,
            (LEFT_COLUMN_START, TOP_HEADER_HEIGHT + NEXT_BOX_HEIGHT, 50, 50),
        )
        self.screen.blit(
            self.game_title,
            (GRID_X_START, TOP_HEADER_HEIGHT / 2, 50, 50),
        )

        pygame.draw.rect(self.screen, Color.LIGHT_BLUE.value, self.score_rect, 0, 10)
        pygame.draw.rect(self.screen, Color.LIGHT_BLUE.value, self.next_rect, 0, 10)
        pygame.draw.rect(self.screen, Color.LIGHT_BLUE.value, self.hold_rect, 0, 10)

    def show_game_over(self):
        game_over_surface = self.game_font.render("GAME OVER", True, Color.WHITE.value)
        self.screen.blit(
            game_over_surface,
            (GRID_X_START + MAIN_CONTENT_WIDTH / 4, GRID_Y_START + MAIN_CONTENT_HEIGHT / 2, 50, 50),
        )

    def draw_block(self, block: Block, x_offset: int, y_offset: int) -> None:
        for tile in block.tiles:
            x, y = tile.column, tile.row
            solution3(self.screen, block, x_offset, y_offset, x, y, CELL_SIZE, GRID_CELL_MULTIPLIER)

    def draw_gs(self, gs: GameState) -> None:
        score_value_surface = self.game_font.render(
            str(gs.score), True, Color.WHITE.value
        )
        self.screen.blit(
            score_value_surface,
            score_value_surface.get_rect(
                centerx=self.score_rect.centerx, centery=self.score_rect.centery
            ),
        )

        self.draw_block(gs.current_block, GRID_X_START, GRID_Y_START)

        if gs.game_over:
            self.show_game_over()
            return

        if gs.held_block:
            self.draw_block(gs.held_block, 50, TOP_HEADER_HEIGHT + NEXT_BOX_HEIGHT + 100)

        for i, block in enumerate(gs.next_blocks):
            self.draw_block(
                block,
                RIGHT_COLUMN_START + 30,
                TOP_HEADER_HEIGHT + 215 + 30 + i * NEXT_BOX_HEIGHT * 0.6,
            )

    def draw_grid(self, grid: Grid) -> None:
        solution2(self.screen, grid, CELL_SIZE, GRID_X_START, GRID_Y_START)
