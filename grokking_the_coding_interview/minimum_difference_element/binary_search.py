def search_min_difference(arr, key):
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    if arr[start] - key < arr[end] - key:
        return arr[start]
    else:
        return arr[end]
