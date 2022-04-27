def pascals_triangle(num_rows):
    ans = []
    for row_num in range(num_rows):
        row = [None] * (row_num + 1)
        row[0], row[-1] = 1, 1
        for col_num in range(1, len(row) - 1):
            row[col_num] = ans[row_num - 1][col_num] + ans[row_num -
                                                           1][col_num - 1]
        ans.append(row)
    return ans


print(pascals_triangle(4))