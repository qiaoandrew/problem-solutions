def find_diagonal_order(mat):
    # Hash table to match sum of indices to elements with that sum
    index_sum_map = {}

    # Loop through matrix and save values to hash table
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i + j in index_sum_map:
                index_sum_map[i + j].append(mat[i][j])
            else:
                index_sum_map[i + j] = [mat[i][j]]

    ans = []
    # Add hash table entries to answer array
    # Even sum of indices will be reversed due to snake pattern
    for item in index_sum_map.items():
        if item[0] % 2 == 0:
            [ans.append(num) for num in item[1][::-1]]
        else:
            [ans.append(num) for num in item[1]]
    return ans


print(find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
