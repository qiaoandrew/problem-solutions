def maximal_square(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    largest = 0

    for row in range(rows):
        dp[row][0] = matrix[row][0]
        largest = max(dp[row][0], largest)

    for col in range(cols):
        dp[0][col] = matrix[0][col]
        largest = max(dp[0][col], largest)

    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col] == 0:
                continue
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1],
                               dp[row - 1][col - 1]) + 1
            largest = max(largest, dp[row][col])

    return largest**2
