def remove_duplicates(arr):
    slow, fast = 1, 1
    while fast < len(arr):
        if arr[fast] != arr[fast - 1]:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    return slow
