def find_max_consecutive_ones(nums):
    left, right = 0, 0
    num_zeroes = 0
    max_consecutive = 0
    while right < len(nums):
        if nums[right] == 0:
            num_zeroes += 1
        while num_zeroes == 2:
            if nums[left] == 0:
                num_zeroes -= 1
            left += 1
        max_consecutive = max(max_consecutive, right - left + 1)
    return num_zeroes
