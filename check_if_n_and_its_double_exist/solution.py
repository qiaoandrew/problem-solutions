def check_if_exist(arr):
    nums = {}
    for num in arr:
        if num / 2 in nums or num * 2 in nums:
            return True
        else:
            nums[num] = 0
    return False
