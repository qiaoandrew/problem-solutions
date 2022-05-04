def remove_element(nums, key):
    left = 0
    for right in range(len(nums)):
        if nums[right] != key:
            nums[left] = nums[right]
            left += 1
    return left
