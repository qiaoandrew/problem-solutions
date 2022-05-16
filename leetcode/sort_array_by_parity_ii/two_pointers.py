def sort_array_by_parity_ii(nums):
    pointer_odd = 1
    for i in range(0, len(nums), 2):
        if nums[i] % 2 == 1:
            while nums[pointer_odd] % 2 == 1:
                pointer_odd += 2
            nums[pointer_odd], nums[i] = nums[i], nums[pointer_odd]
    return nums


print(sort_array_by_parity_ii([4, 2, 5, 7]))
