"""
Objective: Make the blocks stop leaving the bounds of the grid.

A grid has a restricted number of rows and columns where the blocks should not
pas.

              column=0                column=num_columns
                 ↓                           ↓
       row=0 → [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
               [. . . . . . . . . . . . . . .]
row=num_rows → [. . . . . . . . . . . . . . .]

If the `row` or `column` is outside of the bounds, you should return `True`.
"""


def solution5(row: int, column: int, num_rows: int, num_columns: int) -> bool:
    is_out_of_bounds = row >= num_rows  # <- Change this.
    return is_out_of_bounds
