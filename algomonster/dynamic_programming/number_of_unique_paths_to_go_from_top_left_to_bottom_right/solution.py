def unique_paths(rows, cols):
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for col in range(cols):
        dp[0][col] = 1

    for row in range(rows):
        dp[row][0] = 1

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = dp[row][col - 1] + dp[row - 1][col]

    return dp[-1][-1]
