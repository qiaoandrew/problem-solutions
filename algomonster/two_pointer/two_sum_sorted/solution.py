def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        num_sum = arr[left] + arr[right]
        if num_sum > target:
            right -= 1
        elif num_sum < target:
            left += 1
        else:
            return left, right
    return -1, -1
