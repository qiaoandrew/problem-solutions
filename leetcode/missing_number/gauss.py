def missing_number(nums):
    expected = len(nums) * (len(nums) + 1) // 2
    actual = sum(nums)
    return expected - actual