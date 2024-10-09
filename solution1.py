def print_square_shell(n):
    # Create an empty matrix (2D list) filled with zeros.
    matrix = [[0] * n for _ in range(n)]
    
    # Initialize starting variables
    start_row, end_row = 0, n - 1  # These variables track the current row bounds
    start_col, end_col = 0, n - 1  # These variables track the current column bounds
    current_num = 0  # This variable will keep track of the current number to fill the matrix

    # Use a loop to fill the matrix in a spiral pattern
    while start_row <= end_row and start_col <= end_col:
        # Fill the top row (from left to right)
        for col in range(start_col, end_col + 1):
            matrix[start_row][col] = f"{current_num:02d}"  # Fill numbers and format with two digits
            current_num += 1
        start_row += 1  # Move to the next row

        # Fill the right column (from top to bottom)
        for row in range(start_row, end_row + 1):
            matrix[row][end_col] = f"{current_num:02d}"
            current_num += 1
        end_col -= 1  # Move to the previous column

        # Fill the bottom row (from right to left), only if rows are left
        if start_row <= end_row:
            for col in range(end_col, start_col - 1, -1):
                matrix[end_row][col] = f"{current_num:02d}"
                current_num += 1
            end_row -= 1  # Move to the previous row

        # Fill the left column (from bottom to top), only if columns are left
        if start_col <= end_col:
            for row in range(end_row, start_row - 1, -1):
                matrix[row][start_col] = f"{current_num:02d}"
                current_num += 1
            start_col += 1  # Move to the next column

    # Print the matrix
    for row in matrix:
        print(" ".join(row))

# Example usage:
print_square_shell(5)  # This will print the shell matrix for size 5
