def pascals_triangle(num_rows):
    pascal = []
    for row_num in range(num_rows):
        cur_row = [0] * (row_num + 1)
        cur_row[0], cur_row[-1] = 1, 1
        for col_num in range(1, row_num):
            cur_row[col_num] = pascal[row_num -
                                      1][col_num] + pascal[row_num -
                                                           1][col_num - 1]
        pascal.append(cur_row)
    return pascal


print(pascals_triangle(5))