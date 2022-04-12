import math


def max_area(height):
    largest_area = -math.inf
    for i in range(len(height)):
        for j in range(i, len(height)):
            largest_area = max(largest_area,
                               (j - 1) * min(height[i], height[j]))
    return largest_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
