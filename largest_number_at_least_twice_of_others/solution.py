def dominant_index(nums):
    if len(nums) < 2: return 0
    maximum = max(nums)
    dominant_index = -1
    for i, num in enumerate(nums):
        if num == maximum: dominant_index = i
        elif num * 2 > maximum: return -1
    return dominant_index


print(dominant_index([3, 6, 1, 0]))
