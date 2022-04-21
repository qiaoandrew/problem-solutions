def find_disappeared_nums(nums):
    for num in nums:
        index_to_mark = abs(num) - 1
        if nums[index_to_mark] > 0:
            nums[index_to_mark] *= -1
    disappeared_nums = []
    for i in range(len(nums)):
        if nums[i] > 0:
            disappeared_nums.append(i + 1)
    return disappeared_nums
