def find_disappeared_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    ans = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            ans.append(i + 1)
    return ans
