def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if 0 <= nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return nums[-1] + 1


print(first_missing_positive([3, 4, -1, 1]))
