def trapping_rain_water(heights):
    if len(heights) <= 2: return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[0], heights[len(heights) - 1]
    total = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > left_max:
                left_max = heights[left]
            else:
                total += left_max - heights[left]
            left += 1
        else:
            if heights[right] > right_max:
                right_max = heights[right]
            else:
                total += right_max - heights[right]
            right -= 1
    return total


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 3, 2, 1, 2, 1]))