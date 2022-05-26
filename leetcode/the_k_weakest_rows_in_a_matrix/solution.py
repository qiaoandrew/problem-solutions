def k_weakest_rows(mat, k):

    def binary_search(arr):
        start, end = 0, len(arr) - 1
        first_0 = len(arr)
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == 0:
                first_0 = mid
                end = mid - 1
            else:
                start = mid + 1
        return first_0

    row_strengths = []
    for i in range(len(mat)):
        row_strengths.append((binary_search(mat[i]), i))

    row_strengths.sort()

    indices = []
    for i in range(k):
        indices.append(row_strengths[i][1])
    return indices
