def sort_array_by_parity(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] % 2 == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums
