def find_diagonal_order(matrix):
    if not matrix or not matrix[0]:
        return []

    # Determine number of rows (arrays in matrix)
    # and number of columns (elements in arrays)
    rows, cols = len(matrix), len(matrix[0])

    # Answer array and array to hold elements of each diagonal
    ans, intermediate = [], []

    # Diagonals start at elements of first row and last column
    # Last element of first row and first element of last column intersect
    for diagonal in range(rows + cols - 1):
        intermediate.clear()

        # Determine the row and column indices of the diagonal head
        row, col = 0, 0
        if diagonal < cols:
            row = 0
            col = diagonal
        else:
            col = cols - 1
            row = diagonal - col

        # Loop diagonally through matrix while there are still more values
        while row < rows and col > -1:
            intermediate.append(matrix[row][col])
            row += 1
            col -= 1

        # For odd numbered diagonals, reverse it
        if diagonal % 2 == 0:
            ans.extend(intermediate[::-1])
        else:
            ans.extend(intermediate)

    return ans


print(find_diagonal_order([[1, 2], [3, 4]]))
