def find_max_consecutive_ones(nums):
    counter_1 = 0
    counter_2 = 0
    max_consecutive = 0
    next_to_end = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            if next_to_end == 1:
                max_consecutive = max(max_consecutive, counter_1)
                counter_1 = 0
                counter_2 += 1
                next_to_end = 2
            else:
                max_consecutive = max(max_consecutive, counter_2)
                counter_2 = 0
                counter_1 += 1
                next_to_end = 1
        else:
            counter_1 += 1
            counter_2 += 1
    return max(max_consecutive, counter_1, counter_2)


print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
