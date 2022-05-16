def contains_nearby_duplicate(nums, k):
    occurences = {}
    for i in range(len(nums)):
        if nums[i] in occurences and i - occurences[nums[i]] <= k:
            return True
        occurences[nums[i]] = i
    return False
