def third_max(nums):

    def next_maximum(nums, seen_maximums):
        maximum = None
        for num in nums:
            if num in seen_maximums:
                continue
            if maximum == None or num > maximum:
                maximum = num
        return maximum

    seen_maximums = set()
    for _ in range(3):
        cur_maximum = next_maximum(nums, seen_maximums)
        if cur_maximum == None:
            return max(seen_maximums)
        seen_maximums.add(cur_maximum)
    return min(seen_maximums)