from math import inf


def coin_change(coins, amount):
    if amount == 0:
        return 0

    dp = [inf] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[-1] if dp[-1] < inf else -1
