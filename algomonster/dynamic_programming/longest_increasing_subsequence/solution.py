def longest_sub_len(nums):
    dp = [1] * len(nums)
    longest = 0

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] <= nums[j]:
                continue
            dp[i] = max(dp[i], dp[j] + 1)
        longest = max(longest, dp[i])

    return longest