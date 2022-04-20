def trapping_rain_water(heights):
    if len(heights) <= 2: return 0

    highest_left = [0] * len(heights)
    cur_highest_left = 0
    for i in range(len(heights) - 1):
        cur_highest_left = max(cur_highest_left, heights[i])
        highest_left[i + 1] = cur_highest_left

    highest_right = [0] * len(heights)
    cur_highest_right = 0
    for i in range(len(heights) - 1, 0, -1):
        cur_highest_right = max(cur_highest_right, heights[i])
        highest_right[i - 1] = cur_highest_right

    total = 0
    for i in range(len(heights)):
        total += max(min(highest_left[i], highest_right[i]) - heights[i], 0)
    return total


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
