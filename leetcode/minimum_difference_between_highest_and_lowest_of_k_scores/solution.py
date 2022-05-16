def minimum_differences(nums, k):
    if k <= 1:
        return 0
    nums.sort()
    min_difference = float('inf')
    for i in range(0, len(nums) - k + 1):
        min_difference = min(min_difference, nums[i + k - 1] - nums[i])
    return min_difference
