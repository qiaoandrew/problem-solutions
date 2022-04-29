def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total_sum - num - left_sum: return i
        left_sum += num
    return -1


print(pivot_index([2, 1, -1]))