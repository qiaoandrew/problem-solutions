def min_swaps(data):
    num_ones = sum(data)
    if num_ones == 0:
        return 0
    left = 0
    cur_zeroes = 0
    min_zeroes = float('inf')
    for right in range(len(data)):
        if data[right] == 0:
            cur_zeroes += 1
        if right - left + 1 == num_ones:
            min_zeroes = min(min_zeroes, cur_zeroes)
            if data[left] == 0:
                cur_zeroes -= 1
            left += 1
    return min_zeroes
