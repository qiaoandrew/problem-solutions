def longest_subarray(nums):
    left = 0
    longest = 0
    zero_index = -1
    for right in range(len(nums)):
        if nums[right] == 0:
            if zero_index != -1:
                left = zero_index + 1
            zero_index = right
        longest = max(longest, right - left)
    return longest
