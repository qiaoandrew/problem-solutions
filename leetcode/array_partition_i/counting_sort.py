def array_pair_sum(nums):
    counting_sort = [0] * 20001
    for num in nums:
        counting_sort[num + 10000] += 1

    pair_sum = 0
    is_even_index = True
    for element in range(len(counting_sort)):
        while counting_sort[element] > 0:
            if is_even_index:
                pair_sum += element - 10000
            counting_sort[element] -= 1
            is_even_index = not is_even_index

    return pair_sum
