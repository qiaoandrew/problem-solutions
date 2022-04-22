def find_diagonal_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0
    diagonal = 0
    arr = []
    while diagonal in range(rows + cols - 1):
        arr.append(matrix[row][col])
        if diagonal % 2 == 0:
            if col + 1 < cols and row - 1 >= 0:
                row -= 1
                col += 1
            else:
                if col + 1 >= cols:
                    row += 1
                else:
                    col += 1
                diagonal += 1
        else:
            if row + 1 < rows and col - 1 >= 0:
                col -= 1
                row += 1
            else:
                if row + 1 >= rows:
                    col += 1
                else:
                    row += 1
                diagonal += 1
    return arr


print(find_diagonal_order([[1, 2], [3, 4]]))
