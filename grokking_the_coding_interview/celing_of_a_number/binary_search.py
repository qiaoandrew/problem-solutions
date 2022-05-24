def search_ceiling_of_a_number(arr, key):
    if key > arr[len(arr) - 1]:
        return -1

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return start
