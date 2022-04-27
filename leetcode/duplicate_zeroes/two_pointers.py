def duplicate_zeroes(nums):
    displacements = 0
    for num in nums:
        if num == 0:
            displacements += 1

    for i in range(len(nums) - 1, -1, -1):
        if i + displacements < len(nums):
            nums[i + displacements] = nums[i]
        if nums[i] == 0:
            displacements -= 1
            if i + displacements < len(nums):
                nums[i + displacements] = nums[i]
