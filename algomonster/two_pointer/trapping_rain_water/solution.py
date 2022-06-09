def trapping_rain_water(elevations):
    highest_left = [0] * len(elevations)
    max_left = 0
    for i in range(len(elevations)):
        highest_left[i] = max_left
        max_left = max(max_left, elevations[i])

    highest_right = [0] * len(elevations)
    max_right = 0
    for i in reversed(range(len(elevations))):
        highest_right[i] = max_right
        max_right = max(max_right, elevations[i])

    total_water = 0
    for i in range(len(elevations)):
        total_water += max(
            min(highest_left[i], highest_right[i]) - elevations[i], 0)
    
    return total_water
