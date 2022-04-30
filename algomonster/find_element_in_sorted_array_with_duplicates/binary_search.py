def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            left = mid + 1
        else:
            if arr[mid] == target:
                index = mid
            right = mid - 1
    return index


print(find_first_occurrence([2, 3, 5, 7, 11, 13, 17, 19], 6))