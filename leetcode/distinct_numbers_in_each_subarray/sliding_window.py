def distinct_numbers(nums, k):
    distinct = []
    numbers = {}
    left = 0
    for right in range(len(nums)):
        numbers[nums[right]] = numbers.get(nums[right], 0) + 1
        if right - left + 1 == k:
            distinct.append(len(numbers))
            numbers[nums[left]] -= 1
            if numbers[nums[left]] == 0:
                numbers.pop(nums[left])
            left += 1
    return distinct


print(distinct_numbers([1, 2, 3, 2, 2, 1, 3], 3))
