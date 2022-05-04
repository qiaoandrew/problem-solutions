def sorted_squares(arr):
    left, right = 0, len(arr) - 1
    squares = [0] * len(arr)
    cur_index = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            squares[cur_index] = arr[left]**2
            left += 1
        else:
            squares[cur_index] = arr[right]**2
            right -= 1
        cur_index -= 1
    return squares


print(sorted_squares([-3, -1, 0, 1, 2]))