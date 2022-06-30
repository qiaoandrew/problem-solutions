def get_row(row_index):
    prev_row = [1]
    for i in range(1, row_index + 1):
        cur_row = [1] * (i + 1)
        for j in range(1, i):
            cur_row[j] = prev_row[j - 1] + prev_row[j]
        prev_row = cur_row
    return prev_row


print(get_row(3))