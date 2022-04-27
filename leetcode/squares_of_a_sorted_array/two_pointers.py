def sorted_squares(nums):
    squares = []
    left, right = 0, len(nums) - 1
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            squares.append(nums[right]**2)
            right -= 1
        else:
            squares.append(nums[left]**2)
            left += 1
    squares.reverse()
    return squares


print(sorted_squares([-4, -1, 0, 3, 10]))
