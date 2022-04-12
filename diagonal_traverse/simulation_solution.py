def find_diagonal_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    ans = []
    row, col = 0, 0
    diagonal = 0
    while diagonal in range(rows + cols - 1):
        print(str(diagonal) + ' (' + str(row) + ', ' + str(col) + ')')
        ans.append(matrix[row][col])
        if diagonal % 2 == 0:
            if row - 1 > -1 and col + 1 < cols:
                row -= 1
                col += 1
            else:
                if diagonal < cols - 1:
                    col += 1
                else:
                    row += 1
                diagonal += 1
        else:
            if col - 1 > -1 and row + 1 < rows:
                row += 1
                col -= 1
            else:
                if diagonal < rows - 1:
                    row += 1
                else:
                    col += 1
                diagonal += 1
    return ans


print(find_diagonal_order([[1, 2], [3, 4]]))
