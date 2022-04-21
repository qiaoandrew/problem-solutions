def height_checker(heights):
    sorted_heights = sorted(heights)
    wrong = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            wrong += 1
    return wrong
