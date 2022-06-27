def minimum_total(triangle):
    dp = [triangle[-1][c] for c in range(len(triangle[-1]))]

    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r + 1]) - 1):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

    return dp[0]


def minimum_total_dfs(triangle):

    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]

        if r == len(triangle) - 1:
            return triangle[r][c]

        memo[(r, c)] = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
        return memo[(r, c)]

    memo = {}
    return dfs(0, 0)
