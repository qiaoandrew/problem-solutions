def find_max_consecutive(nums):
    left, right = 0, 0
    max_consecutive = 0
    zeroes = 0

    while right < len(nums):
        if nums[right] == 0:
            zeroes += 1

        while zeroes == 2:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        max_consecutive = max(max_consecutive, right + 1 - left)
        right += 1

    return max_consecutive