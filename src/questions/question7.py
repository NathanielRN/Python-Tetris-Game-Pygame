# If statements again

def solution7(row: int, column: int, num_rows: int, num_columns: int) -> bool:
    return row < 0 or row >= num_rows or column < 0 or column >= num_columns
