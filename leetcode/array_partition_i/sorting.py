def array_pair_sum(nums):
    nums.sort()
    pair_sum = 0
    for i in range(0, len(nums), 2):
        pair_sum += nums[i]
    return pair_sum
