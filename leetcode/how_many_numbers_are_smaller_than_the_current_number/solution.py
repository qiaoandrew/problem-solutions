def smaller_numbers_than_current(nums):
    temp_nums = sorted(nums)
    placement = {}
    for i in range(len(temp_nums)):
        if nums[i] in placement:
            placement[temp_nums[i]] += 1
        else:
            placement[temp_nums[i]] = i
    result = []
    for num in nums:
        result.append(placement[num])
    return result


def smaller_numbers_than_current_prefix(nums):
    count = [0] * 102
    for num in nums:
        count[num + 1] += 1
    for i in range(1, 102):
        count[i] += count[i - 1]
    return [count[num] for num in nums]
