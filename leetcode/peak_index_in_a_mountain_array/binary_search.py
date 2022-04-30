def peak_of_mountain_array(arr):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(peak_of_mountain_array([0, 1, 3, 10, 8, 6, 4, 3, 1, 0]))
