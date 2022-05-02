def longest_ones(nums, k):
    left, counter, max_len = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 1:
            counter += 1
        if right - left + 1 > counter + k:
            if nums[left] == 1:
                counter -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
