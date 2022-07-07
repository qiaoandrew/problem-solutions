def find_max_consecutive_ones(nums):
    max_consecutive = 0
    cur, prev, seen_zero = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] == 0:
            seen_zero = 1
            prev = cur
            cur = 0
        else:
            cur += 1
        max_consecutive = max(max_consecutive, cur + prev + seen_zero)

    return max_consecutive