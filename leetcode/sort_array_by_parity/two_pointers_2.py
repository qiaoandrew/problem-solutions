def sort_array_by_parity(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] % 2 > nums[j] % 2:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] % 2 == 0: i += 1
        if nums[j] % 2 == 1: j -= 1
    return nums


print(sort_array_by_parity([0]))
