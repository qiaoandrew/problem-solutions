def find_min(nums):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= nums[-1]:
            index = mid
            right = mid - 1
        else:
            left = mid + 1

    return nums[index]
