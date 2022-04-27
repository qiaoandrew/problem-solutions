def find_diagonal_order(matrix):
    index_sums = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cur_index_sum = i + j
            if cur_index_sum in index_sums:
                index_sums[cur_index_sum].append(matrix[i][j])
            else:
                index_sums[cur_index_sum] = [matrix[i][j]]
    arr = []
    for i in index_sums.keys():
        if i % 2 == 0:
            arr.extend(index_sums[i][::-1])
        else:
            arr.extend(index_sums[i])
    return arr