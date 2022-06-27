def find_largest_subset(nums):
    nums.sort()
    max_subsets = []

    for i, num in enumerate(nums):
        max_subset = 0
        for j in range(i):
            if num % nums[j] == 0:
                max_subset = max(max_subset, max_subsets[j])
        max_subsets.append(max_subset + 1)

    return max(max_subsets)