def remove_element(nums, val):
    p_l = 0
    p_r = len(nums)
    total = len(nums)

    while p_l < p_r:
        if nums[p_l] == val:
            for i in range(p_l, p_r - 1):
                nums[i] = nums[i + 1]
            p_r -= 1
            nums[p_r] = '_'
            total -= 1
        else:
            p_l += 1
    return total


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
