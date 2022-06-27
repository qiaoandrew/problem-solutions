from functools import lru_cache


def can_partition(nums):
    target = sum(nums) // 2
    if sum(nums) % 2 != 0 or max(nums) > target:
        return False
    used = [False] * len(nums)

    @lru_cache(None)
    def dfs(cur_sum):
        if cur_sum == target:
            return True

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            if dfs(cur_sum + nums[i]):
                return True
            used[i] = False

        return False

    return dfs(0)


def can_partition_2(nums):
    if len(nums) < 2:
        return False

    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]
