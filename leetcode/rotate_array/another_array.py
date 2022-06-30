def rotate(nums, k):
    rotated_array = [0] * len(nums)
    k %= len(nums)
    for i in range(len(nums)):
        rotated_array[(i + k) % len(nums)] = nums[i]
    nums[:] = rotated_array
