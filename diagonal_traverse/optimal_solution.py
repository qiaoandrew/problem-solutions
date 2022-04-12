def find_diagonal_order(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    order = False

    for s in range(rows + cols):
        temp = []
        for i in range(max(s - cols, 0), min(s, rows)):
            temp.append(matrix[i][s - i - 1])

        if order:
            temp.reverse()
            order = False
        else:
            order = True

        result += temp
    return result