def three_sum_smaller(nums, target):
    nums.sort()
    counter = 0
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if total_sum < target:
                counter += (right - left)
                left += 1
            else:
                right -= 1
    return counter


print(three_sum_smaller([-2, 0, 1, 3], 2))
