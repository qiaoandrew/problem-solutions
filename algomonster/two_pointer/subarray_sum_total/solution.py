def subarray_sum_total(arr, target):
    prefix_sums = {0: 1}
    cur_sum = 0
    count = 0

    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            count += prefix_sums[complement]
        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

    return count
