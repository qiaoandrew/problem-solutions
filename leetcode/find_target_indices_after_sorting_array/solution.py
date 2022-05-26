def target_indices(nums, target):
    less_than_count, equal_to_count = 0, 0
    for num in nums:
        if num < target:
            less_than_count += 1
        elif num == target:
            equal_to_count += 1
    return list(range(less_than_count, less_than_count + equal_to_count))
