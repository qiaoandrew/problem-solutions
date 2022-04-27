def height_checker(heights):
    frequencies = [0] * (max(heights) + 1)
    for height in heights:
        frequencies[height] += 1
    for i in range(1, len(frequencies)):
        frequencies[i] += frequencies[i - 1]

    sorted_heights = [0] * len(heights)
    for height in heights:
        sorted_heights[frequencies[height] - 1] = height
        frequencies[height] -= 1

    misplaced = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            misplaced += 1
    return misplaced
