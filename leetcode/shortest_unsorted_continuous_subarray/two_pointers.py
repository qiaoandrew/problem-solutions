def find_unsorted_subarray(nums):
    low, high = 0, len(nums) - 1
    while low < len(nums) and nums[low] <= nums[low + 1]:
        low += 1
    if low == len(nums) - 1:
        return 0
    while high > 0 and nums[high] >= nums[high - 1]:
        high -= 1
    subarray_max = -float('inf')
    subarray_min = float('inf')
    for i in range(low, high + 1):
        subarray_max = max(subarray_max, nums[i])
        subarray_min = min(subarray_min, nums[i])
    while low > 0 and nums[low - 1] > subarray_min:
        low -= 1
    while high < len(nums) - 1 and nums[high + 1] < subarray_max:
        high += 1
    return high - low + 1


print(find_unsorted_subarray([1, 3, 2, 4, 5]))
