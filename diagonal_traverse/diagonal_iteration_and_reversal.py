def find_diagonal_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    arr, inter = [], []
    for diagonal in range(rows + cols - 1):
        inter.clear()
        row, col = 0, 0
        if diagonal < cols:
            col = diagonal
        else:
            col = cols - 1
            row = diagonal - cols + 1

        while col > -1 and row < rows:
            inter.append(matrix[row][col])
            col -= 1
            row += 1

        if diagonal % 2 == 0:
            arr.extend(inter[::-1])
        else:
            arr.extend(inter)
    return arr