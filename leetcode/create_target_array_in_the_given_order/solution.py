def create_target_array(nums, index):
    result = []
    for i in range(len(nums)):
        if index[i] >= len(result):
            result.append(nums[i])
        else:
            result.insert(index[i], nums[i])
    return result
