def get_row(row_index):
    row = [1] * (row_index + 1)
    for i in range(row_index):
        for j in range(i, 0, -1):
            row[j] = row[j] + row[j - 1]
    return row


print(get_row(6))