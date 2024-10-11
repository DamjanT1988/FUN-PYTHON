def print_square_shell(n):
    ### Create a 2D list (matrix) filled with zeros
    # create a matrix with n rows and n columns, with the value 0
    matrix = [[0] * n for _ in range(n)]
    
    ### Set up variables to control the boundaries of the matrix
    start_row = 0  # The first row to fill
    end_row = n - 1  # The last row to fill
    start_col = 0  # The first column to fill
    end_col = n - 1  # The last column to fill
    current_number = 0  # The number we will insert into the matrix, starting from 0

    ### Loop while there are still rows and columns to fill
    while start_row <= end_row and start_col <= end_col:
        
        # Fill the top row, going left to right
        # Loop from the first column to the last column in the current top row
        for col in range(start_col, end_col + 1):
            matrix[start_row][col] = f"{current_number:02d}"  # Add the current number (formatted as 2 digits)
            current_number += 1  # Increment the number for the next cell
        start_row += 1  # Move the top boundary down since we filled the top row

        # Fill the right column, going top to bottom
        # Loop from the first row to the last row in the current right column
        for row in range(start_row, end_row + 1):
            matrix[row][end_col] = f"{current_number:02d}"  # Add the current number
            current_number += 1  # Increment the number
        end_col -= 1  # Move the right boundary left since we filled the right column

        # Fill the bottom row, going right to left (only if there are rows left)
        if start_row <= end_row:  # Make sure there's still a row to fill
            for col in range(end_col, start_col - 1, -1):  # Loop backwards from the last column to the first column
                matrix[end_row][col] = f"{current_number:02d}"  # Add the current number
                current_number += 1  # Increment the number
            end_row -= 1  # Move the bottom boundary up since we filled the bottom row

        # Fill the left column, going bottom to top (only if there are columns left)
        if start_col <= end_col:  # Make sure there's still a column to fill
            for row in range(end_row, start_row - 1, -1):  # Loop backwards from the last row to the first row
                matrix[row][start_col] = f"{current_number:02d}"  # Add the current number
                current_number += 1  # Increment the number
            start_col += 1  # Move the left boundary right since we filled the left column

    ###print the matrix row by row
    # 'join' will combine all numbers in each row into a single string separated by spaces
    for row in matrix:
        print(" ".join(row))

#rints 5x5 matrix in a spiral pattern
print_square_shell(5)
