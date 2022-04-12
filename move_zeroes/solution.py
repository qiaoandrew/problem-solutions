def move_zeroes(nums):
    pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pointer] = nums[i]
            pointer += 1
    for i in range(pointer, len(nums)):
        nums[i] = 0
    return nums


print(move_zeroes([0]))
