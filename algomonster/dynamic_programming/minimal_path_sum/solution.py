def min_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    cur_sum = 0
    for col in range(cols):
        cur_sum += grid[0][col]
        dp[0][col] = cur_sum

    cur_sum = 0
    for row in range(rows):
        cur_sum += grid[row][0]
        dp[row][0] = cur_sum

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = min(dp[row - 1][col],
                               dp[row][col - 1]) + grid[row][col]

    return dp[-1][-1]