def trapping_rain_water(arr):
    if len(arr) <= 2: return 0
    # Calculate highest wall on the left
    highest_left = {}
    cur_highest_left = arr[0]
    for i in range(len(arr[1:-1])):
        cur_index = i + 1
        cur_highest_left = max(cur_highest_left, arr[cur_index - 1])
        highest_left[cur_index] = cur_highest_left
    # Calculate highest wall on the right
    highest_right = {}
    cur_highest_right = arr[-1]
    index = len(arr) - 2
    while index > 0:
        cur_highest_right = max(cur_highest_right, arr[index + 1])
        highest_right[index] = cur_highest_right
        index -= 1
    # Calculate total rain
    total_rain = 0
    for i, cur_height in enumerate(arr[1:-1]):
        cur_index = i + 1
        total_rain += max(
            min(highest_left[cur_index], highest_right[cur_index]) -
            cur_height, 0)
    return total_rain


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 3, 2, 1, 2, 1]))