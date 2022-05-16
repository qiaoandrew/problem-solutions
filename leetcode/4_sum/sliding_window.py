def four_sum(nums, target):

    def k_sum(nums, target, k):
        result = []
        if not nums:
            return result
        average_value = target // k
        if average_value < nums[0] or average_value > nums[-1]:
            return result
        if k == 2:
            return two_sum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in k_sum(nums[i + 1:], target - nums[i], k - 1):
                    result.append([nums[i]] + subset)
        return result

    def two_sum(nums, target):
        result = []
        low, high = 0, len(nums) - 1
        while low < high:
            cur_sum = nums[low] + nums[high]
            if cur_sum < target or (low > 0 and nums[low] == nums[low - 1]):
                low += 1
            elif cur_sum > target or (high < len(nums) - 1
                                      and nums[high] == nums[high + 1]):
                high -= 1
            else:
                result.append([nums[low], nums[high]])
                low += 1
                high -= 1
        return result

    nums.sort()
    return k_sum(nums, target, 4)
