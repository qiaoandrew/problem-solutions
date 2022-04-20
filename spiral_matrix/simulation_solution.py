def spiral_order(matrix):
    # Number of movements that need to be done for the current row and column
    rows, cols = len(matrix), len(matrix[0])
    # Current position of the pointer
    row, col = 0, -1
    # Direction traversal is moving in (1: right, down), (-1: left, up)
    direction = 1
    ans = []

    # Loop while either has values to loop through
    while rows > -1 and cols > -1:
        # Horizontally
        for _ in range(cols):
            col += direction
            ans.append(matrix[row][col])
            print(matrix[row][col])
        rows -= 1
        # Vertically
        for _ in range(rows):
            row += direction
            ans.append(matrix[row][col])
            print(matrix[row][col])
        cols -= 1
        # Change direction
        direction *= -1
    return ans


print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
