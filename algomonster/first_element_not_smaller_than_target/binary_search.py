def first_not_smaller(arr, target):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index
