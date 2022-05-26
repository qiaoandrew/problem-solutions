def count_negatives(grid):
    left, bottom = 0, len(grid) - 1
    count = 0
    while bottom >= 0 and left < len(grid[0]):
        if grid[bottom][left] < 0:
            count += len(grid[0]) - left
            bottom -= 1
        else:
            left += 1
    return count
