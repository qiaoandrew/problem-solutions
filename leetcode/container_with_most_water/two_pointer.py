def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water,
                        (right - left) * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water
