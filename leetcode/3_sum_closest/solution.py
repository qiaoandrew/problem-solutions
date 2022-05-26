def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if abs(total_sum - target) < abs(closest_sum - target):
                closest_sum = total_sum
            if total_sum - target > 0:
                right -= 1
            elif total_sum - target < 0:
                left += 1
            else:
                return closest_sum
    return closest_sum


print(three_sum_closest([0, 0, 0], 1))
