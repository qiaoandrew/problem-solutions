def num_identical_pairs(nums):
    numbers = {}
    good_pairs = 0
    for i in range(len(nums)):
        if nums[i] in numbers:
            good_pairs += numbers[nums[i]]
        numbers[nums[i]] = numbers.get(nums[i], 0) + 1
    return good_pairs


print(num_identical_pairs([1, 2, 3]))
