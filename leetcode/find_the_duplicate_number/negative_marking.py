def find_duplicate(nums):
    for num in nums:
        cur = abs(num)
        if nums[cur] < 0:
            return cur
        nums[cur] *= -1
