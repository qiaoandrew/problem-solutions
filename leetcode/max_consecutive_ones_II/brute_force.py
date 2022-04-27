def find_max_consecutive_ones(nums):
    max_consecutive = 0
    for left in range(len(nums)):
        num_zeroes = 0
        for right in range(left, len(nums)):
            if nums[right] == 0:
                num_zeroes += 1
            if num_zeroes <= 1:
                max_consecutive = max(max_consecutive, right - left + 1)
    return max_consecutive
