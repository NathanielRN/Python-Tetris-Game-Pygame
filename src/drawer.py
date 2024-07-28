import pygame

from grid import Grid
from questions.question1 import solution1
from questions.question2 import solution2
from questions.question3 import solution3
from src.block import Block
from src.color import Color
from src.game_state import GameState

# Padding

HORIZONTAL_PAD = 8
VERTICAL_PAD = 20
CELL_SIZE = 30
GRID_CELL_MULTIPLIER = 0.9

# Heights

TOP_HEADER_HEIGHT = 200

GRID_HEIGHT = 620
SCORE_BOX_HEIGHT = 50

H2_TITLE_HEIGHT = 20

HEIGHT = TOP_HEADER_HEIGHT + GRID_HEIGHT

# Widths

SIDE_COLUMN_WIDTH = 170
GRID_WIDTH = 320

WIDTH = SIDE_COLUMN_WIDTH + GRID_WIDTH + SIDE_COLUMN_WIDTH + HORIZONTAL_PAD

# Sides

HOLD_BLOCK_BOX_SIDE = SIDE_COLUMN_WIDTH - HORIZONTAL_PAD

# Vertical Offsets

GRID_ROW_START = TOP_HEADER_HEIGHT
LEFT_COLUMN_START = HORIZONTAL_PAD

SCORE_TITLE_ROW_START = TOP_HEADER_HEIGHT + VERTICAL_PAD
SCORE_BOX_ROW_START = SCORE_TITLE_ROW_START + H2_TITLE_HEIGHT + VERTICAL_PAD

NEXT_TITLE_ROW_START = SCORE_BOX_ROW_START + SCORE_BOX_HEIGHT + VERTICAL_PAD
NEXT_BOX_ROW_START = NEXT_TITLE_ROW_START + H2_TITLE_HEIGHT + VERTICAL_PAD

# Horizontal Offsets

RIGHT_COLUMN_START = WIDTH - SIDE_COLUMN_WIDTH - HORIZONTAL_PAD
GRID_COLUMN_START = SIDE_COLUMN_WIDTH + HORIZONTAL_PAD


class DrawerSingleton(object):
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")

        if it is not None:
            return it

        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwargs)
        return it

    def init(self, *args, **kwargs):
        pass

    def startup_screen(self):
        self.screen.blit(
            self.title_font.render(
                "Welcome! Solve question1 to start :)", True, Color.WHITE.value
            ),
            (
                RIGHT_COLUMN_START,
                HEIGHT / 2,
                SIDE_COLUMN_WIDTH,
                H2_TITLE_HEIGHT,
            ),
        )

    def setup(self):
        self.title_font = pygame.font.Font(None, 80)
        self.game_title = self.title_font.render(solution1(), True, Color.WHITE.value)
        self.game_font = pygame.font.Font(None, 40)
        self.score_title = self.game_font.render("Score", True, Color.WHITE.value)
        self.next_title = self.game_font.render("Next", True, Color.WHITE.value)
        self.hold_title = self.game_font.render("Hold", True, Color.WHITE.value)

        self.score_rect = pygame.Rect(
            RIGHT_COLUMN_START,
            SCORE_BOX_ROW_START,
            SIDE_COLUMN_WIDTH,
            SCORE_BOX_HEIGHT,
        )
        self.next_rect = pygame.Rect(
            RIGHT_COLUMN_START,
            NEXT_BOX_ROW_START,
            SIDE_COLUMN_WIDTH,
            HEIGHT - NEXT_BOX_ROW_START - VERTICAL_PAD,
        )
        self.hold_rect = pygame.Rect(
            LEFT_COLUMN_START,
            SCORE_BOX_ROW_START,
            HOLD_BLOCK_BOX_SIDE,
            HOLD_BLOCK_BOX_SIDE,
        )

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.screen.fill(Color.DARK_BLUE.value)
        self.screen.blit(
            self.score_title,
            (
                RIGHT_COLUMN_START,
                SCORE_TITLE_ROW_START,
                SIDE_COLUMN_WIDTH,
                H2_TITLE_HEIGHT,
            ),
        )
        self.screen.blit(
            self.next_title,
            (
                RIGHT_COLUMN_START,
                NEXT_TITLE_ROW_START,
                SIDE_COLUMN_WIDTH,
                H2_TITLE_HEIGHT,
            ),
        )
        self.screen.blit(
            self.hold_title,
            (
                LEFT_COLUMN_START,
                SCORE_TITLE_ROW_START,
                SIDE_COLUMN_WIDTH,
                H2_TITLE_HEIGHT,
            ),
        )
        self.screen.blit(
            self.game_title,
            self.game_title.get_rect(centerx=WIDTH / 2, centery=TOP_HEADER_HEIGHT / 2),
        )
        game_over_font = pygame.font.Font(None, 60)
        self.game_over_surface = game_over_font.render(
            "GAME OVER", True, Color.WHITE.value
        )
        self.game_over_surface_rect = self.game_over_surface.get_rect(
            center=(WIDTH / 2, TOP_HEADER_HEIGHT + GRID_HEIGHT / 2)
        )

    def show_game_over(self):
        self.screen.blit(
            self.game_over_surface,
            self.game_over_surface_rect,
        )

    def hide_game_over(self):
        pygame.draw.rect(
            self.screen, Color.DARK_BLUE.value, self.game_over_surface_rect, 0
        )

    def draw_block(self, block: Block, x_offset: float, y_offset: float) -> None:
        for tile in block.tiles:
            x, y = tile.column, tile.row
            tile_rect = pygame.Rect(
                x_offset + solution3(x, CELL_SIZE),
                y_offset + solution3(y, CELL_SIZE),
                CELL_SIZE * GRID_CELL_MULTIPLIER,
                CELL_SIZE * GRID_CELL_MULTIPLIER,
            )

            pygame.draw.rect(self.screen, block.color.value, tile_rect)

    def draw_dynamic_elements(self, grid: Grid, gs: GameState) -> None:
        if gs.game_over:
            self.draw_block(gs.current_block, GRID_COLUMN_START, GRID_ROW_START)
            self.show_game_over()
            return

        self.hide_game_over()

        def draw_grid_cell(row: int, col: int):
            cell_color = grid.cells[row][col]
            cell_rect = pygame.Rect(
                col * CELL_SIZE + GRID_COLUMN_START,
                row * CELL_SIZE + GRID_ROW_START,
                CELL_SIZE * GRID_CELL_MULTIPLIER,
                CELL_SIZE * GRID_CELL_MULTIPLIER,
            )
            pygame.draw.rect(self.screen, cell_color.value, cell_rect)

        solution2(draw_grid_cell)

        pygame.draw.rect(self.screen, Color.DARK_GREY.value, self.score_rect, 0, 10)
        pygame.draw.rect(self.screen, Color.DARK_GREY.value, self.next_rect, 0, 10)
        pygame.draw.rect(self.screen, Color.DARK_GREY.value, self.hold_rect, 0, 10)

        score_value_surface = self.game_font.render(
            str(gs.score), True, Color.WHITE.value
        )
        self.screen.blit(
            score_value_surface,
            score_value_surface.get_rect(
                center=(self.score_rect.centerx, self.score_rect.centery)
            ),
        )

        self.draw_block(gs.current_block, GRID_COLUMN_START, GRID_ROW_START)

        if gs.held_block:
            self.draw_block(
                gs.held_block,
                LEFT_COLUMN_START + HOLD_BLOCK_BOX_SIDE / 5,
                SCORE_BOX_ROW_START + 1.5 * VERTICAL_PAD,
            )

        for i, block in enumerate(gs.next_blocks):
            self.draw_block(
                block,
                RIGHT_COLUMN_START + HOLD_BLOCK_BOX_SIDE / 5,
                NEXT_BOX_ROW_START
                + 1.25 * VERTICAL_PAD
                + i * (HOLD_BLOCK_BOX_SIDE * 0.8),
            )
