def trapping_rain_water(heights):
    total = 0
    for i in range(len(heights)):
        left_max, right_max = 0, 0
        for left in range(i):
            left_max = max(left_max, heights[left])
        for right in range(i + 1, len(heights)):
            right_max = max(right_max, heights[right])
        total += max(min(left_max, right_max) - heights[i], 0)
    return total


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
