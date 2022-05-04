def sort_colors(nums):
    boundary_0, boundary_2 = 0, len(nums) - 1
    i = 0
    while i <= boundary_2:
        if nums[i] == 0:
            nums[i], nums[boundary_0] = nums[boundary_0], nums[i]
            boundary_0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[boundary_2] = nums[boundary_2], nums[i]
            boundary_2 -= 1
        else:
            i += 1
