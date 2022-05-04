def three_sum(nums):
    nums.sort()
    combinations = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            left, right = i + 1, len(nums) - 1
            while left < right:
                total_sum = nums[left] + nums[right] + nums[i]
                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    combinations.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
    return combinations