def single_number(nums):
    missing = 0
    for num in nums:
        missing ^= num
    return missing
