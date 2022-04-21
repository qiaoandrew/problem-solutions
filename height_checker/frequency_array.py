def height_checker(heights):
    frequencies = [0] * (max(heights) + 1)
    for height in heights:
        frequencies[height] += 1

    misplaced = 0
    cur_frequency = 0
    for i in range(len(heights)):
        while frequencies[cur_frequency] == 0:
            cur_frequency += 1
        if heights[i] != heights[cur_frequency]:
            misplaced += 1
        frequencies[cur_frequency] -= 1
    return misplaced
