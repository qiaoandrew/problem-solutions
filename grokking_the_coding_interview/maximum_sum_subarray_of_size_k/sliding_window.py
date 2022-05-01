def max_sub_array_of_size_k(k, arr):
    if k > len(arr):
        return -1
    cur_sum = max_sum = 0
    left = 0
    for right in range(len(arr)):
        cur_sum += arr[right]
        if right >= k - 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= arr[left]
            left += 1
    return max_sum
