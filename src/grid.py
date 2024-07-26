from src.color import Color

NUM_ROWS = 20
NUM_COLUMNS = 10
EMPTY_CELL = Color.DARK_GREY


class Grid:
    def __init__(self):
        self.grid = [[EMPTY_CELL for _ in range(NUM_COLUMNS)] for __ in range(NUM_ROWS)]

    @staticmethod
    def is_out_of_bounds(row: int, column: int):
        return row < 0 or row >= NUM_ROWS or column < 0 or column >= NUM_COLUMNS

    def has_block(self, row: int, column: int) -> None:
        return self.grid[row][column] != EMPTY_CELL

    def is_row_full(self, row) -> bool:
        for column in range(NUM_COLUMNS):
            if self.grid[row][column] == EMPTY_CELL:
                return False
        return True

    def clear_row(self, row: int) -> None:
        for column in range(NUM_COLUMNS):
            self.grid[row][column] = EMPTY_CELL

    def move_row_down(self, row: int, num_rows: int) -> None:
        for column in range(NUM_COLUMNS):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = EMPTY_CELL

    def clear_full_rows(self) -> int:
        full_rows = 0

        for row in range(NUM_ROWS - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                full_rows += 1
            elif full_rows > 0:
                self.move_row_down(row, full_rows)

        return full_rows

    def reset(self):
        for row in range(NUM_ROWS):
            for column in range(NUM_COLUMNS):
                self.grid[row][column] = EMPTY_CELL
