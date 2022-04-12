def find_disappeared_numbers(nums):
    for i in range(len(nums)):
        marked_index = abs(nums[i]) - 1
        if nums[marked_index] > 0:
            nums[marked_index] *= -1
    ans = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            ans.append(i)
    return ans
