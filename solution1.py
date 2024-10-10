def print_square_shell(n):
    # Create a matrix (2D list) with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Set variables for the boundaries of the matrix
    start_row = 0  # The first row we will fill
    end_row = n - 1  # The last row we will fill
    start_col = 0  # The first column we will fill
    end_col = n - 1  # The last column we will fill
    current_number = 0  # This is the number we'll put into the matrix

    # Keep filling the matrix as long as there are rows and columns left
    while start_row <= end_row and start_col <= end_col:
        # Fill the top row (left to right)
        for col in range(start_col, end_col + 1):
            matrix[start_row][col] = f"{current_number:02d}"  # Format the number to be 2 digits
            current_number += 1
        start_row += 1  # Move the top boundary down

        # Fill the right column (top to bottom)
        for row in range(start_row, end_row + 1):
            matrix[row][end_col] = f"{current_number:02d}"
            current_number += 1
        end_col -= 1  # Move the right boundary left

        # Fill the bottom row (right to left), if there are rows left
        if start_row <= end_row:
            for col in range(end_col, start_col - 1, -1):
                matrix[end_row][col] = f"{current_number:02d}"
                current_number += 1
            end_row -= 1  # Move the bottom boundary up

        # Fill the left column (bottom to top), if there are columns left
        if start_col <= end_col:
            for row in range(end_row, start_row - 1, -1):
                matrix[row][start_col] = f"{current_number:02d}"
                current_number += 1
            start_col += 1  # Move the left boundary right

    # Print the matrix row by row
    for row in matrix:
        print(" ".join(row))

# Example usage: This will print a 5x5 shell matrix
print_square_shell(5)
