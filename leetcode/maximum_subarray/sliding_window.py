def max_sub_array(nums):
    current_subarray = max_subarray = nums[0]
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
    return max_subarray
