def find_min(nums):
  low, high = 0, len(nums) - 1
  while low < high:
    pivot = low + (low + high) // 2
    if nums[pivot]
