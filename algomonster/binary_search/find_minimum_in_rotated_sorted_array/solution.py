def find_min_rotated(arr):
    start, end = 0, len(arr) - 1
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= arr[-1]:
            index = mid
            end = mid - 1
        else:
            start = mid + 1
    return index
