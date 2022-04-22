def spiral_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, -1
    direction = 1
    ans = []

    while rows * cols > 0:
        for _ in range(cols):
            col += direction
            ans.append(matrix[row][col])
        rows -= 1
        for _ in range(rows):
            row += direction
            ans.append(matrix[row][col])
        cols -= 1
        direction *= -1
    return ans


print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
