def find_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    duplicates = []
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            duplicates.append(nums[i])
    return duplicates
