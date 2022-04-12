def replace_elements(arr):
    greatest = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > greatest:
            temp = arr[i]
            arr[i] = greatest
            greatest = temp
        else:
            arr[i] = greatest
    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
