def replace_elements(arr):
    greatest = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = greatest
        greatest = max(temp, greatest)
    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
