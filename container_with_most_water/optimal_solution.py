import math


def max_area(height):
    left_pointer = 0
    right_pointer = len(height) - 1
    largest_area = -math.inf
    while left_pointer < right_pointer:
        largest_area = max(largest_area, (right_pointer - left_pointer) *
                           min(height[left_pointer], height[right_pointer]))
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        elif height[right_pointer] < height[left_pointer]:
            right_pointer -= 1
        else:
            if height[left_pointer + 1] > height[right_pointer - 1]:
                left_pointer += 1
            else:
                right_pointer -= 1
    return largest_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
