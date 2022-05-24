def subsets(nums):
    subsets = [[]]
    for num in nums:
        n = len(subsets)
        for i in range(n):
            new_set = list(subsets[i])
            new_set.append(num)
            subsets.append(new_set)
    return subsets


print(subsets([1, 2, 3]))
