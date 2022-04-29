def trapping_rain_water(heights):
    if len(heights) <= 2:
        return 0
    left, right = 0, len(heights) - 1
    max_left, max_right = heights[0], heights[-1]
    total = 0
    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(heights[left], max_left)
            total += max(0, max_left - heights[left])
        else:
            right -= 1
            max_right = max(heights[right], max_right)
            total += max(0, max_right - heights[right])
    return total
