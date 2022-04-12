def trapping_rain_water(arr):
    if len(arr) <= 2: return 0
    left_pointer = 0
    right_pointer = len(arr) - 1
    left_max = arr[0]
    right_max = arr[len(arr) - 1]
    total_rain = 0
    while left_pointer < right_pointer:
        if arr[left_pointer] < arr[right_pointer]:
            if arr[left_pointer] > left_max:
                left_max = arr[left_pointer]
            else:
                total_rain += left_max - arr[left_pointer]
            left_pointer += 1
        else:
            if arr[right_pointer] > right_max:
                right_max = arr[right_pointer]
            else:
                total_rain += right_max - arr[right_pointer]
            right_pointer -= 1
    return total_rain


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 3, 2, 1, 2, 1]))