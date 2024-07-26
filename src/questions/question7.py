# If statements again

def solution7(row: int, column: int, num_rows: int, num_columns: int) -> bool:
    """
    This function checks if a given position (row, column) is out of bounds of a grid.
    Steps:
    1. Check if the row is less than 0 or greater than or equal to the number of rows.
    2. Check if the column is less than 0 or greater than or equal to the number of columns.

    It should return True if the position is out of bounds and False if it is within the grid.
    """

    is_out_of_bounds = row >= num_rows # --> Add remaining checks
    return is_out_of_bounds