def rotate(nums, k):
    k %= len(nums)
    for _ in range(k):
        prev = nums[-1]
        for i in range(len(nums)):
            prev, nums[i] = nums[i], prev
